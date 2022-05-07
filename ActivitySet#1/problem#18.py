import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input('Enter a URL: ')
data = urllib.request.urlopen(inp, context=ctx).read()
info = json.loads(data)["comments"]

sum = 0
for count in info:
    sum += count["count"]

print(f"Sum: {sum}")