import sys

def retaddr(addr):
	return "\\x%s\\x%s\\x%s\\x%s" % (addr[6:8], addr[4:6], addr[2:4], addr[0:2])


addr = ""
if len(sys.argv) < 2:
	print "usage: " + sys.argv[0] + "address in hex format (e.g. 1A2B3C4D, 0142DDEF)"
	addr = raw_input("Enter addr: ")
else:
	addr = argv[1]
	

print "Retrn addr: " + retaddr(addr)
