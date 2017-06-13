from __future__ import unicode_literals
from gtts import gTTS

from twilio.rest import Client
from django.core.exceptions import MiddlewareNotUsed
import os
import logging
import json

#import pyttsx
#engine = pyttsx.init()  #initiliazing pyttsx
#engine.say('hello world.')  # add all the text you want to convert to speech
#engine.say('How are you.')
#engine.runAndWait()  #start converting.this will automatically play the speech the response

class AuthorizedUser():
    def __init__(self, name, owner, phoneNumber):
        self.name = name
        self.owner = owner
        self.preferences = []
        if owner:
            with open('config/administrators.json', 'w') as adminsFile:
                admins = json.load(adminsFile)
                newOwner = {'phone number' : phoneNumber, 'name' : name}
                admins.append(newOwner)

    def setUpHouse(self):
        for pref in self.preferences:
            pref()

    def addPref(self, pref):
        self.preferences.append(pref)

def Enter(usr):
    print 'Door Unlocked'
    usersHome.append(usr)
    usr.setUpHouse()

    t = "Welcome Home" + usr.name
    tts = gTTS(text=t, lang='en')
    tts.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")

def Leave(usr):
    usersHome.remove(usr)

def unauthorizedUserAtDoor():
    #MESSAGE = getKnockerName() + " is at your door. Do you want to let them in? Respond 'Yes' or 'No'"
    MESSAGE = "Saul is at your door. Do you want to let them in? Respond 'Yes' or 'No'"

    account_sid = "ACa87fd6d5a2c8d63346d60fc3399d036e"
    # account_sid = "PNabca243db30e6e08dd0fc836d4d63f71"
    auth_token = "147c37d7b50171110f8996a67c0e0dab"
    client = Client(account_sid, auth_token)

    with open('config/administrators.json', 'r') as adminsFile:
        admins = json.load(adminsFile)
        print admins
        for admin in admins:
            toNumber = admin["phone_number"]
            MESSAGE = getKnockerName() + " is at your door. Do you want to let them in? Respond 'Yes' or 'No'"
            message = client.api.account.messages.create(to=toNumber,
                                                 from_="+14159935014",
                                                 body=MESSAGE,
                                                 media_url = [getKnockerImage()])
    print 'sent'

def getKnockerImage():
    return "https://github.com/margotduek/smartdoor/raw/unstable/saul_pic.JPG"

def getKnockerName():
    return 'Saul'

authorizedUsers = []
usersHome = []

authorizedUsers[0] = AuthorizedUser('Jesse', True, "+972534264710")

unauthorizedUserAtDoor()





