import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input('Enter a URL: ')
url = urllib.request.urlopen(inp, context=ctx).read()
tree = ET.fromstring(url) 

commlist = tree.findall('.//count')
total = 0
for count in commlist:
        total += int(count.text)

print(f"Sum {total}...")