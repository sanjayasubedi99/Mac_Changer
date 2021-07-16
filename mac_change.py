#Adding requirements
import subprocess
import optparse


parser =  optparse.OptionParser()

##adding options in command line
parser.add_option("-i" , "--interface" , dest="interfaceName" , help="InterfaceName to change mac")

parser.add_option("-m" , "--mac" , dest="newMac" , help="New  mac address")

(options , arguments) = parser.parse_args()

#Mac Changer Inputs
interfaceName = options.interfaceName

newMac = options.newMac


#Printing what's happening

print("[+] Changing Mac Adddress for "+ interfaceName + " to " + newMac)

#Uncomment it if you want yourself to be exploited by running system commands.
# subprocess.call("ifconfig " + interfaceName + " down" , shell=True)

# subprocess.call("ifconfig " + interfaceName + " hw ether " + newMac , shell=True)
	
# subprocess.call("ifconfig " + interfaceName + " up" , shell=True)
#

#Commands to Change given Mac.
subprocess.call(["ifconfig",interfaceName,"down"])

subprocess.call(["ifconfig", interfaceName , "hw", "ether", newMac])

subprocess.call(["ifconfig", interfaceName , "top"])

