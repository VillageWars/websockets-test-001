import asyncio
import websockets
import json

# To test, run python -m websockets wss://websockets-test-001-91c83418594c.herokuapp.com/

#URI = 'wss://websockets-test-001-91c83418594c.herokuapp.com/'
URI = 'ws://localhost:8001'

async def connect():
    print('Connecting...')
    async with websockets.connect(URI) as websocket:
        print('Connected!')
        while True:
            message = input("Enter a message to send: ")
            try:
                dic = eval(message)
            except SyntaxError:
                dic = str(message)
            if type(dic)!= dict:
                dic = {'type':'text', 'text':dic}
            event = json.dumps(dic)
            await websocket.send(event)
            try:
                message = await websocket.recv()
                event = json.loads(message)
            except websockets.ConnectionClosedOK:
                print('Connection closed')
                break
            print()
            print('INCOMING MESSAGE\n')
            print('Type:', event['type'])
            print('Data:\n', event)
            print()
            #event = {
            #    "type": "confirm",
            #}
            #await websocket.send(json.dumps(event))
            #message = await websocket.recv()
            #event = json.loads(message)
            #assert event['type'] == 'confirm'


asyncio.get_event_loop().run_until_complete(connect())
