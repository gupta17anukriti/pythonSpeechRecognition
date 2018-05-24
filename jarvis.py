#!/usr/bin/python3

from gtts import gTTS
import speech_recognition as sr
import os,random

dout = os.popen('date "+%c"').read()
store = dout.split()

def speak(msg):
	tts = gTTS(text=msg, lang='en')
	tts.save('jarvis.mp3')
	os.system('mpg321 -q jarvis.mp3')
	os.remove('jarvis.mp3')
	print(msg)

# get audio from the microphone
def stt():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak:")
		audio = r.listen(source)
	msg = ''
	try:
		msg = r.recognize_google(audio)
		print(msg)

	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

	return msg	


def audio():
	os.system('python3 play.py')

def time():
	msg = 'the time is '+ ' '.join(store[4:6])
	speak(msg)

def date():
	msg = 'today is '+ ' '.join(store[0:4])
	speak(msg)

def place(location):
	speak('Hold on Uddipta, I will show you where ' + location + ' is.')
	os.system('google-chrome https://www.google.nl/maps/place/' + location + '/&amp;')

def name():
	name = os.popen('whoami').read()
	speak('you are '+name)

def mood():
	speak('I am always good')

def weather():
	speak('Hold on Uddipta, I will show you the weather report')
	os.system('google-chrome https://goo.gl/c9sYBe')


def terminate():
	speak('Still you have any question ?')
	data = stt()
	if 'yes' in data:
		speak('Ask me !')
		jarvis()
	else:
		quit()
		os.system('exit')


def allinone(data):
	if 'music' or 'song' in data:
		audio()
		terminate()

	if 'time' in data:
		time()
		terminate()

	if 'date' in data:
		date()
		terminate()

	if 'name' in data:
		name()
		terminate()

	if 'how' in data:
		mood()
		terminate()

	if 'where' in data:
		data = data.split(' ')
		location = data[2]
		place(location)
		terminate()

	if 'weather' in data:
		weather()
		terminate()

	else:
		speak("I think you slept. ha! ha!")
		quit()
		os.system('exit')



def jarvis():
	data = stt()
	allinone(data)


speak('Hi Uddipta, what can I do for you?')
jarvis()