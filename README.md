# DDos your API

### GET requests to URL
- arg 0: app.py
- arg 1: host address (always only use your own servers)
- arg 2: port
- arg 3: number of threads (should be equals your logical processors count) \

run:
``python3 app.py "https://myserver.com" 80 8``

### POST requests to URL
- arg 0: app.py
- arg 1: host address (always only use your own servers)
- arg 2: port
- arg 3: number of threads (should be equals your logical processors count) \
- arg 4: valid json to be sent in the body as application/json

run:
``python3 app.py "https://myserver.com" 80 8 "{'a': 'a','b': 'b','c': 'c'}"``
