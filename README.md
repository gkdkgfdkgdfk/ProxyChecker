# ProxyChecker
Check if your IP can be tunneled through a proxy which supports the HTTP or HTTPS protocol.

The checking is strict, and therefore will only save the proxies in the file goods if they have less than 200ms and if you could be tunneled successfully through the proxies.
# Usage
```
checking http is much faster than https
python3 check.py http
python3 check.py https

Correct format in check.txt:
ip:port

NOT http://ip:port or https://ip:port
```

