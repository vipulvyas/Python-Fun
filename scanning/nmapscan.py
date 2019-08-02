import nmap
import sys
import time

nm_scan = nmap.PortScanner()
print('\n Running.....\n')
nm_scanner =nm_scan.scan(sys.argv[1],'80',arguments='-O')

host_is_up = "the host is :"+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port_open = "the port 80 is :"+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method_scan = "the method of scanning is :"+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
guessed_os = "there is a %s persent chance to that host is running %s "%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])

with open("%s.txt"%sys.argv[1],'w') as f:
    f.write(host_is_up+port_open+method_scan+guessed_os)
    f.write("\nReport generated "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))
    
    
print("\n Finished.....\n")
