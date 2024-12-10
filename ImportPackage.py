import naoqi
#print "IT WORKED AHHHHH AYAYAYAYYAYAYA"
def movePepper(x=0.0,y=0.0,z=0.0):
    '''Move pepper using given data, built for KU lab pepper'''
    from naoqi import ALProxy
    #tts = ALProxy("ALTextToSpeech", "192.168.3.137",9559)
    motion = ALProxy("ALMotion","192.168.3.137",9559 )
    motion.setStiffnesses("Body", 1.0)
    motion.moveInit()
    motion.moveTo(x,y,z)
    #motion.moveTo(0.0, -2.0, 0.0)
    #tts.say("You are such a girl boss molly")

movePepper(y=-1.0)