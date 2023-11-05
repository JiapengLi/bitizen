import asyncio
import websockets
import json
import os
import sys

connected_clients = []

async def handle_connection(websocket, path):
    # Add the websocket to a list of connected clients
    connected_clients.append(websocket)
    try:
        while True:
            # Receive a message from the client
            message = await websocket.recv()

            # Broadcast the message to all connected clients
            for client in connected_clients:
                ws_msg = json.loads(message)
                print("receive msg", ws_msg['key'])
                await client.send(message)
    except websockets.exceptions.ConnectionClosedOK:
        pass
    finally:
        # Remove the websocket from the list of connected clients
        connected_clients.remove(websocket)

if len(sys.argv) != 2:
    print("usage: ", sys.argv[0], "websocket_port")
    print("example: ", sys.argv[0], "8000")
    os._exit(1)

websocket_port = sys.argv[1]

# Start the WebSocket server
start_server = websockets.serve(handle_connection, '0.0.0.0', websocket_port)
# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
