import pyttsx3
en = pyttsx3.init()
en.setProperty('voice',b'brazil')
en.say("fala ae Christian")
en.runAndWait()
