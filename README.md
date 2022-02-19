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
