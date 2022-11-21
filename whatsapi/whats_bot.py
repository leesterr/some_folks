from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from wiki import wiki_queries

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'


@app.route('/sms', methods=['POST'])
def sms_reply():
    """Responding incoming message with simple text"""
    # Fetch the message
    msg = request.form.get('Body')

    # Create a reply
    resp = MessagingResponse()
    resp.message(body=wiki_queries(msg))
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
