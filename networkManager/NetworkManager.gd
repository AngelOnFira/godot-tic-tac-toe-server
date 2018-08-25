extends Node

var HOST_IP = "127.0.0.1"
var HOST_PORT = "6000"
var POLL_FREQ = 1000

var client = null
var wrappedClient = null
var clientConnected = false

var lastPoll

func _ready():
	lastPoll = util.millis()
	_connectToHost()

func _process(delta):
	if (util.millis() - lastPoll > POLL_FREQ and clientConnected):
		print("polling")
		client.poll()
		lastPoll = util.millis()

func _connectToHost():
	client = WebSocketClient.new()
	client.connect_to_url("ws://" + HOST_IP + ":" +  HOST_PORT)
	
	wrappedClient = PacketPeerStream.new()
	wrappedClient.set_stream_peer(client)
	
	client.connect("connection_established", self, "_connection_established")
	client.connect("connection_error", self, "_connection_error")
	client.connect("connection_closed", self, "_connection_closed")
	
	client.poll()
	
func _connection_established(protocol):
	clientConnected = true
	print("Connection established with protocol: ", protocol)
	
func _connection_closed():
	print("Connection closed")

func _connection_error():
	print("Connection error")