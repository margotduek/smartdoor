from gtts import gTTS
import os

class AuthorizedUser():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.preferences = []

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

usersHome = []

