import naoqi
from naoqi import ALProxy
IP = "192.168.3.137"
asr = ALProxy("ALSpeechRecognition", IP, 9559)
asr.setLanguage("English")