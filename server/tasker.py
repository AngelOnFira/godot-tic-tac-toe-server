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
		print(websocket)
		print(address)