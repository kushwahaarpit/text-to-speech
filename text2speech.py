import pyttsx3

data = input("Enter text which you want to convert:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
