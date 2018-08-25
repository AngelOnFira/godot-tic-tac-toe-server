import asyncio
import socket
import websockets
import uuid
from tasker import Tasker

#LOCAL = socket.gethostbyname(socket.gethostname())
LOCAL = "127.0.0.1"
PORT = 6000

class GameServer:
	def __init__(self):
		print("Server started on %s:%s." % (LOCAL, PORT))
		self.loop = None
		self.lobby = Tasker()

if __name__ == '__main__':
	server = GameServer()
	server.loop = asyncio.get_event_loop()
	server.loop.run_until_complete(websockets.serve((lambda websocket, address: server.lobby._connectPlayer(websocket, address)), LOCAL, PORT))
	server.loop.run_forever()