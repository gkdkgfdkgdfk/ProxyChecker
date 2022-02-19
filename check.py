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
python3 check.py http
python3 check.py https
'''

def Type():
    try:
        protocol = sys.argv[1]
        if protocol == "http":
            return protocol
        if protocol == "https":
            return protocol
        if protocol == "HTTPS":
            return "https"
        if protocol == "HTTP":
            return "http"
        else:
            sys.exit("Invalid protocol type! Only http or https")
    except:
        sys.exit("Usage examples:\npython3 check.py http\npython3 check.py https")

socket.timeout(200)

def ReadProxies(*, file):
    with open(f"{file}","r")as f:
        filedata = f.read()
        filedatalist = filedata.split()
    return filedatalist


def start():
    proxytype = Type() 
    with open(f"check.txt","r")as f:
        filelenght = len(f.readlines())
    print(f"\033[0mChecking {filelenght} proxies\n")

    objectproxies = ReadProxies(file='check.txt')
    for proxiesd in objectproxies:
        try:
            r = requests.get('https://httpbin.org/ip', proxies={f'{proxytype}' : f'{proxiesd}'},timeout=200)
            data = json.loads(r.text)   
            if data['origin'] == proxiesd:
                print("\033[32mGood Proxy: \033[0m", proxiesd)
                with open("goods.txt","a+")as w:
                    w.write(f"{proxiesd}\n")
                pass
            else:
                
                print("\033[31mBad Proxy \033[0m",proxiesd)
        except:
            print("\033[31mBad Proxy 033[0m",proxiesd)

if __name__ == '__main__':
    thread = Process(target=start(), name="Checking Thread")
    thread.start()
    thread.join()

