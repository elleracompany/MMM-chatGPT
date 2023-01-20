
Learn more

Message List
Mahamud Ismail (External) added Per Erik Kattai-Eira and Ga Kin Chi (External) to the chat.
Mahamud Ismail (External) added Per Erik Kattai-Eira and Ga Kin Chi (External) to the chat.
Profile picture of Mahamud Ismail.
Message by Mahamud Ismail
Mahamud Ismail (External)Yesterday 14:29
Text
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Home Page</title>
</head>
<body>
<! -- Calls a function on the page load. -- >
<element onload="myfunction_onload">
<button type="submit" onclick='myfunction_clickevent()'>Run my Python!</button>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
<! -- This script runs the python script on the page load -->
<script>
    function myfunction_onload(){
        $.ajax({
            url: "app.py",
             context: document.body
            })
        }
    </script>
<! -- This script runs the python script when the button is clicked -->
<script>
    function myfunction_clickevent(){
        $.ajax({
            url:"/test",
            context: document.body});}
</script>
</body>
</html>
Profile picture of Mahamud Ismail.
Message by Mahamud Ismail
Mahamud Ismail (External)Yesterday 14:57
Text
import speech_recognition as sr
r = sr.Recognizer()
speech = sr.Microphone(device_index=1)
with speech as source:
    print("say something!…")
    audio = r.adjust_for_ambient_noise(source)
    print("started to record..")
    audio = r.listen(source)
try:
    recog = r.recognize_google(audio, language = 'nb-NO')
    print("You said: " + recog)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
Today
Profile picture of Mahamud Ismail.
Link https://github.com/SikandAlex/MMM-Porc... by Mahamud Ismail
Mahamud Ismail (External)09:01
https://github.com/SikandAlex/MMM-Porcupine

Url Preview for GitHub - SikandAlex/MMM-Porcupine: Magic Mirror module that implements Picovoice Porcupine wake word detection
GitHub - SikandAlex/MMM-Porcupine: Magic Mirror module that implements Picovoice Porcupine wake word detection
Magic Mirror module that implements Picovoice Porcupine wake word detection - GitHub - SikandAlex/MMM-Porcupine: Magic Mirror module that implements Picovoice Porcupine wake word detection

github.com
Profile picture of Mahamud Ismail.
Hei, jeg må gjøre noe i 4min. Kommer tilbak... by Mahamud Ismail
Mahamud Ismail (External)10:02
Hei, jeg må gjøre noe i 4min. Kommer tilbake til rommet snart
Profile picture of Mahamud Ismail.
hei Ga   Kin   Chi , Kan du gi meg json bo... by Mahamud Ismail
Mahamud Ismail (External)11:11
hei Ga Kin Chi,

Kan du gi meg json body eksempel på hva flow forventer?

Last read
Profile picture of Mahamud Ismail.
Message by Mahamud Ismail
Mahamud Ismail (External)14:15
Python

Text
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