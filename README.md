# MCRon
Is a fork of github.com/barneygale/MCRcon designed to allow easier command line access to a Minecraft Server via the RCon interface.

# Why?
If you're running MineCraft as a daemon it is likely that it will be running in screen. While this is not a problem, it adds an overhead.
RCon is an interface built in to the newer MineCraft Servers that allow you to connect to the server via a socket and run the normal commands where previously you used the `-X stuff` command with screen.
The advantage of this is that it should be more scriptable and you could do some more complicated things with it.
