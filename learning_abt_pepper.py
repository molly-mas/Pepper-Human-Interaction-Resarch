import qi
import sys
import time

#app = qi.Application()
#app.start()
#session = app.session

#tss = session.service("ALAnimatedSpeech")
#tss.say("This is a test run of my animated speech function. Being a robot is really cool!")

#python learning_abt_pepper.py --qi-url=tcp://192.168.3.137

class Test:

    def __init__(self):
        #stuff at the start
        app = qi.Application()
        app.start()
        session = app.session
        self.memory = session.service("ALMemory")
        self.tts = session.service("ALAnimatedSpeech")
        #Entered the cool
        self.people_perception = session.service("ALPeoplePerception")
        self.subscriber = self.memory.subscriber("EngagementZones/PersonEnteredZone1")
        self.subscriber.signal.connect(self.entered_the_cool)
        #left the cool
        self.subscriber2 = self.memory.subscriber("EngagementZones/PersonMovedAway")
        self.subscriber2.signal.connect(self.left_the_cool)
        #pepper hears 
        self.subscriber3 = self.memory.subscriber("ALSoundLocalization/SoundsLocated")
        self.subscriber3.signal.connect(self.pepper_hears)
        self.Led = session.service("ALLeds")
        self.got_person = False
        
        #test recorder
        self.audio_recorder = session.service("ALAudioRecorder")



        #self.got_sound = False
        #self.enterd_zone = False

        #self.subscriber= self.memory.subscriber("FaceDetected")
        #self.subscriber.signal.connect(self.say_hi)
        #self.got_person = False

        #self.status = session.service("ALBasicAwareness")
        #self.status.setTrackingMode("MoveContextually")
        

    
    # def say_hi(self, value):
        
    #     if value == []:
    #         self.got_person = False
    #     elif self.got_person == False:
    #         self.got_person = True
    #         print "I see a person!"
    #         self.tts.say("Hi there!")
    #         time.sleep(5)

    def entered_the_cool(self,value):
        if value == []:
            print "Hi Hi Hi #entered the cool"
        else:
            if value != []:
                #print(value)
                #self.tts.say("Hello there I am pepper, Would you like to have a conversation?")
                #self.enterd_zone = True
                self.got_person = True
            
    
    def left_the_cool(self, value):
        if value == []:
            print "I am here #left the cool"
        else:
            print "you left"
            self.got_person = False
            #self.tts.say("It was nice to meet you, I hope you have an amazing day!")

    def pepper_hears(self, value):
        if self.got_person == True:
            # time.sleep(5)
            if value == []:
                print "YO YO YO you are here #pepper hears"
            else:
                self.subscriber3 = False
                print "Sound heard in zone"
                self.pre_light()
                self.pepper_record()
                self.lights_up()
                self.subscriber3 = self.memory.subscriber("ALSoundLocalization/SoundsLocated")
                self.subscriber3.signal.connect(self.pepper_hears)
                #print(self.got_sound)
                
                #self.tts.say("I hear you! Hi my name is pepper want to have a conversation?")
        else: 
            print "Heard sound not in zone"


        

    def lights_up(self):
        self.Led.rasta(5.0)

    def pre_light(self):
        self.Led.rasta(1.0)


    def pepper_record(self):
        ''' '''
        channels = (1,1,1,1)
        #Set up the call to channels here for the method
        self.audio_recorder.startMicrophonesRecording("~/recordings/microphones/Test.wav","wav",48000, channels)
        #time here
        time.sleep(10)
        self.audio_recorder.stopMicrophonesRecording()




    def run(self):
        print "Starting The test"
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            print " Exiting Program..."
            #self.status.setTrackingMode("Head")
            sys.exit(0)

my_test = Test()
my_test.run()

#Note: pepper runs enter_the_cool twice when the person is sitting?