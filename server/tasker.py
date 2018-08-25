# Manage all users in a lobby when they start the game
# Manage all users in a room when they join a specific game
import json
import uuid
from random import randint

from player import Player

class Tasker:
	def __init__(self):
		print("Lobby initialized.")

	async def _connectPlayer(self, websocket, address):
		await self._monitorClientRequests(websocket)

	async def _monitorClientRequests(self, websocket):
		# Check if the connection with a websocket is lost

		await websocket.send("test")
		try:	
			print("checking if user is still connected")
		
			while True:
				request = await websocket.recv()

				print(request)

		except:  # What is the type of  the error atm if any error occurs deregister the client
			print("We have an error")