#!/usr/bin/python3

import subprocess
from termcolor import colored

def change_mac_address(interface, mac):
    subprocess.call(["ifconfig",interface ,"down"])
    subprocess.call(["ifconfig", interface , "hw","ether",mac])
    subprocess.call(["ifconfig", interface , "up"])

def main():
    interface= input("[+] Enter Interface To change Mac Address On: ")
    new_mac=input("[*] Enter New Mac Address To change To: ")
    before_change=subprocess.check_output(["ifconfig", interface])
    change_mac_address(interface, new_mac)
    after_change=subprocess.check_output(["ifconfig", interface])

    if before_change==after_change:
        print(colored("[!!] Failed to Change Mac Address!", 'red'))
    else:
        print(colored(f"[+] Mac Address changed To: {new_mac} {interface}", 'green'))
try:
    main()
except KeyboardInterrupt as e:
    print("[!!] Quiting...")
except:
    print("[!!] Error")
