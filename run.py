"""

This is lite version!!!!!!
made by adjidev
Full version will be released as soon possible

"""

import sys
import os
from colorama import init, Fore, Style

# Plugins
from plugins.checkCarrier import LookupCarrier
from plugins.TrackUser import TrackSocial
from plugins.whois import WhoisIp
from plugins.nmapScan import NmapScan

init()

banner = f"""             
{Fore.RED} _____       _    {Style.RESET_ALL} _____          
{Fore.RED}| __  |___ _| |___{Style.RESET_ALL}|   __|_ _ ___  1.0.1#github
{Fore.RED}|    -| -_| . |- _{Style.RESET_ALL}|   __| | | -_| https://t.me/adjidev
{Fore.RED}|__|__|___|___|___{Style.RESET_ALL}|_____|_  |___| 
{Fore.RED}                  {Style.RESET_ALL}      |___|    
"""

menu = f"""
{Fore.GREEN}1. {Style.RESET_ALL}NIK PARSER
{Fore.GREEN}2. {Style.RESET_ALL}PHONE NUMBER LOOKUP        
{Fore.GREEN}3. {Style.RESET_ALL}TRACK USERNAME             
{Fore.GREEN}4. {Style.RESET_ALL}WHOIS LOOKUP
{Fore.GREEN}5. {Style.RESET_ALL}NMAP SCAN
{Fore.GREEN}6. {Style.RESET_ALL}EXIT
"""

def ClearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Utama():
    ClearScreen()
    print(banner)
    print(menu)
    while True:
        try:
            shell = input("Type a valid number\nredzeye@2024~# ")
            
            if shell == "1":
                nik = input("Type a valid NIK\n~# ")
                os.system(f"node plugins/adji.js -n {nik}")
            elif shell == "2":
                nomer = input("Type a valid phone number starts with +62\n~# ")
                hasilnya = LookupCarrier(phone=nomer)
                print(f"\n{hasilnya}")
            elif shell == "3":
                username = input("Type a username to track\n~# ")
                hasilnya = TrackSocial(username=username)
                print(f"\n{hasilnya}")
            elif shell == "4":
                ip = input("Type a valid IP address or domain\n~# ")
                hasilnya = WhoisIp(ip=ip)
                print(f"\n{hasilnya}")
            elif shell == "5":
                target = input("Type a valid IP address or domain to scan\n~# ")
                hasilnya = NmapScan(target=target)
                print(f"\n{hasilnya}")
            elif shell == "6":
                print(f"{Fore.YELLOW}[*] Exiting the program...{Style.RESET_ALL}")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[!] Invalid option! Please try again.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[*] Keyboard interrupt detected. Exiting...{Style.RESET_ALL}")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}[!] An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    Utama()
