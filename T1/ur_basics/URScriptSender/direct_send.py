import socket
 
UR_SERVER_PORT = 30002
 
def send_script(ur_ip, script):
    global UR_SERVER_PORT
    s = socket.create_connection((ur_ip, UR_SERVER_PORT), timeout=2) 
    s.send(script)
    print "Script sent to %s on port %i" % (ur_ip, UR_SERVER_PORT)
    s.close()
 
send_script(ur_ip, script)