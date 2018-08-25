extends Node

var timeSinceLastRequest = _millis()
var checkFreq = 2000

func _ready():
	pass

func _process(delta):
	if (_millis() - timeSinceLastRequest > checkFreq):
		_checkForUpdates()
		timeSinceLastRequest = _millis()
	
func _checkForUpdates():
	print("update")

func _millis():
	return OS.get_ticks_msec()