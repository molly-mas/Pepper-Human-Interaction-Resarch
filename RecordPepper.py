import naoqi
import FileDownloadTest
import os
import time
import qi
import sys

class PepperTalks():
    def __init__(self,IP,port,app,text_file_name):
        super(PepperTalks,self).__init__()
        app.start()
        session = app.session
        self.IP = IP
        self.port = port
        self.text_file = text_file_name
        self.memory = session.service("ALMemory")
        #Molly maybe add basic awarness move contextually???
        self.basic_awareness = session.service("ALBasicAwareness")
        self.basic_awareness.setEngagementMode("SemiEngaged")
        self.basic_awareness.setStimulusDetectionEnabled("People", True)
        self.basic_awareness.setStimulusDetectionEnabled("Sound", True)
        self.background_movement = session.service("ALBackgroundMovement")
        self.background_movement.setEnabled(True)
        self.animated_tts = session.service("ALAnimatedSpeech")
        self.values = session.service("ALValue")
        #enable in methods
        self.listening_movement = session.service("ALListeningMovement")
        #enable in methods
        self.speaking_movement = session.service("ALSpeakingMovement")
        self.speaking_config = {"bodyLanguageMode":"random"}
        self.audio_recorder = session.service("ALAudioRecorder")
        self.people_perception = session.service("ALPeoplePerception")
        self.people_perception.subscribe("PepperTalks")


# MOLLY IMPORTANT FOR PEPPER TO TALK AND MOVE INSTEAD OF TTS YOU NEED TO USE ALAnimatedSpeech!!!!
    #KEEP WORKING ON THIS!!! ITS GONNA WORK

#ALSO LOOK INTO PAUSING UNPAUSING BASIC AWARENESS!!!!!

    def pepper_get_file(self):
        '''Calls the program that downloads the audio file from Pepper'''
        self.get_file()
    
    def pepper_record(self):
        ''' '''
        channels = (1,1,1,1)
        #Set up the call to channels here for the method
        self.audio_recorder.startMicrophonesRecording("~/recordings/microphones/HiPepperTwo.wav","wav",48000, channels)
        #time here
        time.sleep(10)
        self.audio_recorder.stopMicrophonesRecording()
    
    def say_response(self):
        ''' '''
        file = open(self.text_file, "r")
        content = file.read()
        self.animated_tts.say(content,self.speaking_config)
    

# MOLLY ADD IN MOVEMENT STUFF INTO LISTENING AND SPEAKING!


    

        
 #OK PEOPLE DETECTION UPDATE MOLLY WE MIGHT BE ABLE TO USE THE DISTANCE FROM THE 
 #ROBOT TO TRIGGER THE ACTION USING ALEngagementZones!!!!!

 ''' THE ENGAGEMENT ZONES ARE THE KEY FOR TRIGGERING EVENTS THIS IS SO HYPE'''