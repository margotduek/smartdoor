from __future__ import unicode_literals
import recieve_sms
import upload_to_google
from twilio.rest import Client
import os


owners = []
authorizedUsers = []
usersHome = []

#People allowed entry
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
            os.system("Say the " + pref.appliance + " is set to " + str(pref.value))

    def addPref(self, pref):
        self.preferences.append(pref)

class Preference():
    def __init__(self, appliance, value):
        self.appliance = appliance
        self.value = value


#To let someone enter
def Enter(usr):
    print 'Door Unlocked'
    usersHome.append(usr)
    os.system("say Hi " + usr.name + ". Welcome home")
    usr.setUpHouse()

#To deny someone entey
def Deny():
    print 'Door Locked'
    os.system("say You have been denied entry. Please leave the premises immediately")

#Called when someone leaves house
def Leave(usr):
    usersHome.remove(usr)

#Texts each owner the name and picture of person at the door to see if they should be allowed entry
#Gets response via text message and calls Enter(usr) or Deny(usr) based on repsonce
def unauthorizedUserAtDoor():
    account_sid = "ACa87fd6d5a2c8d63346d60fc3399d036e"
    auth_token = "147c37d7b50171110f8996a67c0e0dab"
    client = Client(account_sid, auth_token)
    for owner in owners:
        toNumber = owner["phone number"]
        text = "Hi " + owner['name']
        body = text + ". " + getKnockerName() + " is at your door. Do you want to let them in? Respond 'Yes' or 'No'"
        image = [getKnockerImage()]
        print image[0]
        message = client.api.account.messages.create(to=toNumber,
                                             from_="+14159935014",
                                             body=body,
                                             media_url = getKnockerImage())
        print 'sent message "' + body + '"'
    letIn = recieve_sms.run()
    if letIn:
        Enter(AuthorizedUser(getKnockerName(), False, None))
    else:
        Deny()


MY_HOST_URL = "109.11.212.22"

def getKnockerImage():
    upload_to_google.run()
    return "https://storage.googleapis.com/images-smartdoor/face_pic_4.jpg"

def getKnockerName():
    return 'Jesse'


jesse = AuthorizedUser('Jesse', True, "+19105089100")
jesse.addPref(Preference("TV", "Channel 4"))
jesse.addPref(Preference("Air Conditioning", "Off"))
jesse.addPref(Preference("Stereo", "Play Funk"))
authorizedUsers.append(jesse)

Enter(jesse)
print "unauthorized at door"
unauthorizedUserAtDoor()

