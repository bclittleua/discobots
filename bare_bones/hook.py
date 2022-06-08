# This is a basic discord webhook written for a linux OS,
# surround argument with quotes if longer than 1 word, i.e. "hello world"

from discord import Webhook, RequestsWebhookAdapter

def send (message):
    webhook = Webhook.from_url("WEBHOOK URL GOES HERE!", adapter=RequestsWebhookAdapter())
    webhook.send(message)

send( sys.argv[0] )
