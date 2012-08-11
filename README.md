# MCRon
Is a fork of barneygale/MCRcon designed to allow easier object wrapping of a Minecraft Server via the RCon interface. Along with some scripts to allow easier administration.

# Why?
If you're running MineCraft as a daemon it is likely that it will be running in screen. While this is not a problem, it adds an overhead.
RCon is an interface built in to the newer MineCraft Servers that allow you to connect to the server via a socket and run the normal commands where previously you used the `-X stuff` command with screen.
The advantage of this is that it should be more scriptable and you could do some more complicated things with it.

# Enabling RCon
In your Minecraft Server's config file `server.properties` change the line `rcon.enable=false` to `rcon.enable=true` and add the line `rcon.password=<password>` where <password> is the secure password you will be using from the rcon connection. Do not forget that this password will be sent in in the plain.

# Using the script
You need to initialise the object with the password (whatever you set), hostname (recommend using localhost), and the port (usually 25575).

# Using the scripts
Still to come
