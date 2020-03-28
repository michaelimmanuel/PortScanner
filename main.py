
# -*- coding: utf-8 -*-

import sys
from socket import *
import subprocess
from datetime import datetime

# port_scan.py <host> <start_port>-<end_port>

host = sys.argv[1]
portstrs = sys.argv[2].split("-")
start_port = int(portstrs[0])
end_port = int(portstrs[1])
target_ip = gethostbyname(host)


subprocess.call('clear', shell=True)

t1 = datetime.now()

try : 
	for port in range(start_port, end_port+1):
	
		sock = socket(AF_INET, SOCK_STREAM)
		sock.settimeout(10)
		result = sock.connect_ex((target_ip, port))

		if result == 0:
			print "Port {}:Open".format(port)
        sock.close()


except KeyboardInterrupt:
    print "Exited"
    sys.exit()

except socket.gaierror:
    print "Host Couldn't Be Resolved"
    sys.exit()

except socket.error:
    print "Connection Closed"
    sys.exit()


t2 = datetime.now()

total =  t2 - t1


print 'Scan Finished in : ', total




