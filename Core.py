from __future__ import unicode_literals
from gtts import gTTS
import recieve_sms
from twilio.rest import Client
import os
import json

#import pyttsx
#engine = pyttsx.init()  #initiliazing pyttsx
#engine.say('hello world.')  # add all the text you want to convert to speech
#engine.say('How are you.')
#engine.runAndWait()  #start converting.this will automatically play the speech the response

owners = []

class AuthorizedUser():
    def __init__(self, name, owner, phoneNumber):
        self.name = name
        self.owner = owner
        self.preferences = []
        if owner:
            o = {'phone number': phoneNumber, 'name': name}
            owners.append(o)

    def setUpHouse(self):
        for pref in self.preferences:
            pref()

    def addPref(self, pref):
        self.preferences.append(pref)

def Enter(usr):
    print 'Door Unlocked'
    usersHome.append(usr)
    usr.setUpHouse()
    os.system("say Hi " + usr.name + ". Welcome home")

def Deny():
    print 'Door Locked'
    os.system("say You have been denied entry. Please leave the premises immediately")


def Leave(usr):
    usersHome.remove(usr)


def unauthorizedUserAtDoor():
    account_sid = "ACa87fd6d5a2c8d63346d60fc3399d036e"
    auth_token = "147c37d7b50171110f8996a67c0e0dab"
    client = Client(account_sid, auth_token)
    for owner in owners:
        toNumber = owner["phone number"]
        text = "Hi " + owner['name']
        body = text + ". " + getKnockerName() + " is at your door. Do you want to let them in? Respond 'Yes' or 'No'"
        #message = client.api.account.messages.create(to=toNumber,
        #                                     from_="+14159935014",
        #                                     body=body,
        #                                     media_url = [getKnockerImage()])
        print 'sent message "' + body + '"'
    letIn = recieve_sms.sms()
    if letIn:
        Enter(AuthorizedUser(getKnockerName(), False, None))
    else:
        Deny()


def getKnockerImage():
    return "https://github.com/margotduek/smartdoor/raw/unstable/saul_pic.JPG"

def getKnockerName():
    return 'Saul'

authorizedUsers = []
usersHome = []

jesse = AuthorizedUser('Jesse', True, "+972534264710")
authorizedUsers.append(jesse)

Enter(jesse)
unauthorizedUserAtDoor()

