import requests
import socket
from multiprocessing import Process
import json, sys


'''
Proxy Checker
Z3NTL3
t.me/lowkeypanelme

Usage:
dropdown all your proxies in check.txt

Usage Example:
python3 check.py http ms
python3 check.py https ms
'''
try:
    if sys.argv[2].isnumeric:
        mst = int(sys.argv[2])
    else:
        sys.exit("\033[31mPlease only use integer values")
except:
    sys.exit("\033[31mPlease only use integer values")

if type(mst) == int:
    pass
else:
    sys.exit("MS value can only be a integer!")


def Type():
    try:
        protocol = sys.argv[1]
    
        if protocol == "https":
            return protocol
        if protocol == "http":
            return "http"
        if protocol == "HTTP":
            return "http"
        if protocol == "HTTPS":
            return "https"
        else:
            sys.exit("Invalid protocol type! Only https and http")
       
    except:
        sys.exit("Usage examples:\npython3 check.py https\npython3 check.py http")


def Hosts():
    try:
        with open(f"check.txt","r")as f:
            filedata = f.read()
            filedatalist = filedata.split("\n")
        global hosts
        hosts = {}
        for i in filedatalist:
            host, port = i.split(":")
            hosts[host] = port
        return hosts
    except:
        sys.exit("\033[31mRemove all white space newlines in check.txt\033[0m")

def start():
    proxytype = Type()
    proxiesz3ntl3 = Hosts()

    if proxytype == "http":
        
        for host,port in proxiesz3ntl3.items():
            try:
                print(f"\033[36mChecking Proxy: \033[0m{host}:{port}")  
                r = requests.get('http://ip-api.com/json', proxies={f'http' : f'{host}:{port}'},timeout=mst)

                data = json.loads(r.text) 
                
                if data['query'] == host:
                    print(f"\033[32mGood Proxy: \033[0m{host}:{port}")
                    with open("goods.txt","a+")as w:
                        w.write(f"{host}:{port}\n")
                else:   
                    print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
            except:
                print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
    if proxytype == "https":
        
        for host,port in proxiesz3ntl3.items():
            try:
                print(f"\033[36mChecking Proxy: \033[0m{host}:{port}")  
                r = requests.get('https://httpbin.org/ip', proxies={f'https' : f'{host}:{port}'},timeout=mst)

                data = json.loads(r.text) 
                
                if data['origin'] == host:
                    print(f"\033[32mGood Proxy: \033[0m{host}:{port}")
                    with open("goods.txt","a+")as w:
                        w.write(f"{host}:{port}\n")
                else:   
                    print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
            except:
                print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
if __name__ == '__main__':
    print("Made by Z3NTL3")
    start()
