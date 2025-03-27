'''
Docu String Stuff here 
'''
import qi
import time
import sys
import argparse
import os
import paramiko
import FileDownloadTest






# IMPORTANT MOLLY USE .WAIT WHEN MAKING THE RUN() FUNCTION ITLL SAVE YOU SO MUCH PAIN
class TalkingPepper(object):
    ''' Docu'''
    def __init__(self, app):
        ''' docu'''
        super(TalkingPepper, self).__init__()
        app.start()
        session = app.session
        self.memory = session.service("ALMemory")
        self.subscriber = self.memory.subscriber("FaceDetected")
        self.subscriber2 = self.memory.subscriber("SoundDetected")
        self.tts = session.service("ALTextToSpeech")
        self.face_detection = session.service("ALFaceDetection")
        self.face_detection.subscribe("TalkingPepper")
        self.got_face = False
        self.sound_detection = session.service("ALSoundDetection")
        self.sound_detection.subscribe("TalkingPepper")
        self.audio_recorder = session.service("ALAudioRecorder")
        self.heard_sound = False
        self.recording_location = "home/nao/PepperGPT/temp_recording/temp.wav"

    def on_human_tracked(self, value):
        """
        Callback for event FaceDetected.
        """
        if value == []:  # empty value when the face disappears
            self.got_face = False
        elif not self.got_face:  # only speak the first time a face appears
            self.got_face = True
            
            
    
    def on_sound_heard(self, val):
        if val == []:
            self.heard_sound = False
        else:
            self.heard_sound = True

    def record(self):
        self.audio_recorder.startMicrophonesRecording(self.recording_location, "wav", 16000, (0, 0, 1, 0))
        time.sleep(10)
            

#THIS MIGHT WORK???????
    def download_file(self):
        self.get_file()

my_thing = TalkingPepper(app)
my_thing.download_file()
