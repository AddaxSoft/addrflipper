import sys

def retaddr(addr):
	addr = str(addr)
	return "\\x%x\\x%x\\x%x\\x%x" % (int(addr[6:8],16), int(addr[4:6],16), int(addr[2:4],16), int(addr[0:2],16))


addr = 0
if len(sys.argv) < 2:
	print "usage: " + sys.argv[0] + "address in hex format (e.g. 1A2B3C4D, 0142DDEF)"
	addr = raw_input("Enter addr: ")
else:
	addr = argv[1]
	

print "Retrn addr: " + retaddr(addr)
