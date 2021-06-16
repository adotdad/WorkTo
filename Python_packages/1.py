from urllib.request import urlopen, Request
import time

url = Request('https://www.varzesh3.com/')

while True:
    response = urlopen(url).read()
    time.sleep(10)
    new_response = urlopen(url).read()

    if response != new_response:
        print('something has changed')
