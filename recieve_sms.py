from flask import Flask, request
from twilio import twiml
from twilio.rest import Client


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    print "number is " + number
    print "message_body is " + message_body

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))

    account_sid = "ACa87fd6d5a2c8d63346d60fc3399d036e"
    auth_token = "147c37d7b50171110f8996a67c0e0dab"
    client = Client(account_sid, auth_token)
    if str(resp) == 'Yes' or str(resp) == 'yes':
        message = client.api.account.messages.create(to=number,
                                                     from_="+14159935014",
                                                     body="Ok. We let him in")
        print "found" + str(resp)
        return True
    elif str(resp) == 'No' or str(resp) == 'no':
        message = client.api.account.messages.create(to=number,
                                                     from_="+14159935014",
                                                     body="Ok. We'll lock the door")
        print "found" + str(resp)
        return False
    else:
        message = client.api.account.messages.create(to=number,
                                                     from_="+14159935014",
                                                     body="Please respond Yes or no")
        print "found" + str(resp)
        sms()

if __name__ == '__main__':
    app.run()
