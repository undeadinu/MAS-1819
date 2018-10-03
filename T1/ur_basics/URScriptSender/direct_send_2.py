__author__ = "jennyd"
__version__ = "2018.10.02"


import socket

file_path = 'C:\\Users\\jennyd\\Desktop\\URScriptSender\\'
file_name = 'test_script.txt'

robot_ip = '192.168.10.10'
script = ''

UR_SERVER_PORT = 30002

def send_script(ur_ip, script):
    global UR_SERVER_PORT
    s = socket.create_connection((ur_ip, UR_SERVER_PORT), timeout=2)
    s.send(script)
    print "Script sent to %s on port %i" % (ur_ip, UR_SERVER_PORT)
    s.close()


if execute:
    print "in"
    path = file_path+file_name

    file = open(file_path+file_name, 'r')
    file_lines = file.readlines()
    file.close()

    for line in file_lines:
        script += line

    print file_lines
    print script

    send_script(robot_ip,script)
