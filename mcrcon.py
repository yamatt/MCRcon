import socket
import select
import struct
import re

class MCRcon (object):
    GAMEMODE_SURVIVAL = 0
    GAMEMODE_CREATIVE = 1
    GAMEMODE_ADVENTURE = 2
    
    TIME_MIDDAY = 6000
    TIME_DUSK = 12000
    TIME_MIDNIGHT = 18000
    TIME_DAWN = 0
    
    def __init__(self, host, port, password):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((host, port))
        self._send(3, password)
        
    def save_all(self):
        return self.send("save-all")
        
    def save_off(self):
        return self.send("save-off")
        
    def save_on(self):
        return self.send("save-on")
        
    def say(self, message):
        return self.send("say %s" % message)
        
    def stop(self):
        return self.send("stop")
        
    def give(self, player, item, amount=1, damage=0):
        return self.send("give %s" % " ".join([player, item, amount, damage]))
        
    def whitelist_on(self):
        return self.send("whitelist on")
        
    def whitelist_off(self):
        return self.send("whitelist off")
        
    def whitelist_add(self, name, reload_list=True):
        message = self.send("whitelist add %s" % name)
        if reload_list:
            message += self.whitelist_reload()
        return message
        
    def whitelist_remove(self, name, reload_list=True):
        message = self.send("whitelist remove %s" % name)
        if reload_list:
            message += self.whitelist_reload()
        return message
        
    def whitelist_reload(self):
        return self.send("whitelist reload")
        
    def gamemode(self, mode, player=None):
        if not player:
            return self.send("gamemode %d" % mode)
        else:
            return self.send("gamemode %d %s" % (mode, player))
            
    def time_set(self, time):
        return self.send("time set %d" % time)
        
    def time_add(self, time):
        return self.send("time add %d" % time)
    
    def close(self):
        self.__socket.close()
    
    def send(self, command):
        return self._send(2, command)
    
    def _send(self, out_type, out_data):
        #Send the data
        buff = struct.pack('<iii', 
            10+len(out_data),
            0,
            out_type) + out_data + "\x00\x00"
        self.__socket.send(buff)
        
        #Receive a response
        in_data = ''
        ready = True
        while ready:
            #Receive an item
            tmp_len, tmp_req_id, tmp_type = struct.unpack('<iii', self.__socket.recv(12))
            tmp_data = self.__socket.recv(tmp_len-8) #-8 because we've already read the 2nd and 3rd integer fields

            #Error checking
            if tmp_data[-2:] != '\x00\x00':
                raise Exception('protocol failure', 'non-null pad bytes')
            tmp_data = tmp_data[:-2]
            
            #if tmp_type != out_type:
            #    raise Exception('protocol failure', 'type mis-match', tmp_type, out_type)
           
            if tmp_req_id == -1:
                raise Exception('auth failure')
           
            m = re.match('^Error executing: %s \((.*)\)$' % re.escape(out_data), tmp_data)
            if m:
                raise Exception('command failure', m.group(1))
            
            #Append
            in_data += tmp_data

            #Check if more data ready...
            ready = select.select([self.__socket], [], [], 0)[0]
        
        return in_data
