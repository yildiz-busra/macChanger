import subprocess
import optparse
import re


def getUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="macAddress", help="new MAC address")
    return parse_object.parse_args()

def changeMAC(interface, macAddress):
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", macAddress])
    subprocess.run(["sudo", "ifconfig", interface, "up"])

def control(interface):
    output = subprocess.check_output(["ifconfig", interface])
    newMAC = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if newMAC:
        return newMAC.group(0)
    else: 
        return None


print("\n\n----------MAC CHANGER----------\n\n")
(userInput, arguments) = getUserInput()
changeMAC(userInput.interface, userInput.macAddress)
finalMAC = control(userInput.interface)

if finalMAC == userInput.macAddress:
    print("\nMAC address successfully changed!")
else:
    print("\nError changing MAC address!")

