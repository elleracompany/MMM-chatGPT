import speech_recognition as sr
import time
import requests
def AudioWakeWord():
    r = sr.Recognizer()
    trigger = False
    with sr.Microphone(device_index=1) as source:
        print("Listing...")
        time.sleep(3)
        audio = r.listen(source)
        try:
            transcribed_text = r.recognize_google(audio, language = 'nb-NO')
            if "start" in transcribed_text:
                trigger = True
        except sr.UnknownValueError:
             print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
             print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return trigger
def ListenToX():
    r = sr.Recognizer()
    textToAPI = ""
    with sr.Microphone(device_index=1) as source:
        print("Listing...")
        audio = r.listen(source)
        try:
            textToAPI = r.recognize_google(audio, language = 'nb-NO')
        except sr.UnknownValueError:
             print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
             print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return textToAPI
def sendAPI(text):
    pass
if __name__ == "__main__":
    a = AudioWakeWord()
    print("A:",a)
    if a == False:
        ListenToX()