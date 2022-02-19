# ProxyChecker
Check if your IP can be tunneled through a proxy which supports the HTTP or HTTPS protocol.

The checking is strict, and therefore will only save the proxies in the file goods if they have less than ms you defined and if you could be tunneled successfully through the proxies.
# Usage
```elixir
checking http is much faster than https
python3 check.py http ms
python3 check.py https ms

Example usage:
python3 check.py https 2 
> means 2 seconds timeout how more how slower check

Correct format in check.txt:
ip:port

NOT http://ip:port or https://ip:port
```
For faster https check performance, to be as fast as HTTP check replace lines:
```elixir
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
```
Replace with:
```elixir
if proxytype == "https":
        
        for host,port in proxiesz3ntl3.items():
            try:
                print(f"\033[36mChecking Proxy: \033[0m{host}:{port}")  
                r = requests.get('https://ip-api.com/json', proxies={f'https' : f'{host}:{port}'},timeout=mst)

                data = json.loads(r.text) 
                
                if data['origin'] == host:
                    print(f"\033[32mGood Proxy: \033[0m{host}:{port}")
                    with open("goods.txt","a+")as w:
                        w.write(f"{host}:{port}\n")
                else:   
                    print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
            except:
                print(f"\033[31mBad Proxy: \033[0m {host}:{port}")
```
