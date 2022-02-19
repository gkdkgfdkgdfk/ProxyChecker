# ProxyChecker
Check if your IP can be tunneled through a proxy which supports the HTTP or HTTPS protocol.

# Usage
```elixir
// checking http is much faster than https
python3 check.py http
python3 check.py https
```
```elixir
// Drop down all your proxies inside of check.txt
// The software will automaticly save the good proxies in goods.txt

// There is no chance for fail as shown under. It will only SAVE the proxies with which you could be tunneled!
def start():
    proxytype = Type() 
    
    objectproxies = ReadProxies(file='check.txt')
    for proxiesd in objectproxies:
        try:
            r = requests.get('https://httpbin.org/ip', proxies={f'{proxytype}' : f'{proxiesd}'},timeout=200)
            data = json.loads(r.text)
            if data['origin'] == proxiesd:
                print("\033[32mGood Proxy: ", proxiesd)
                with open("goods.txt","a+")as w:
                    w.write(f"{proxiesd}\n")
                pass
            else:
                print("\033[31mBad Proxy ",proxiesd)
        except:
            print("\033[31mBad Proxy ",proxiesd)

```
