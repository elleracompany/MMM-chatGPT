# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:52:28 2023

@author: MahamudIsmail
"""

import speech_recognition as sr
import subprocess



def recordAudio():
    # initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # start listening for audio
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=None)
        try:
            # check if keyword is detected
            transcribed_text = r.recognize_google(audio)
            if "start" in transcribed_text:
                print("Keyword detected, starting recording...")
                # start recording with arecord command and wait for 5 seconds
                subprocess.run(["arecord", "--buffer-time=5000000", "---threshold=50", "--duration=5", "-f","cd","-t", "wav", "-r", "44100", "-c", "1", "recording.wav"])
                print("Recording saved as 'recording.wav'")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    


if __name__ == "__main__":  
    recordAudio()    