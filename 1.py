import pyttsx3
friend=pyttsx3.init()
friend.say("hello shivam")
speech=input("Say something")
friend.say(speech)
friend.runAndWait()
