# 
# This is a basic discord webhook written for a linux OS,
# BUT has added functionality to parse host IP address, for debugging

import sys
import requests
from discord import Webhook, RequestsWebhookAdapter
from subprocess import Popen, PIPE
from time import sleep

# looking for an active Ethernet or WiFi device
def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name

# find an active IP on the first LIVE network device
def parse_ip():
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip

# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

# before start of main loop - detect active network device and ip address
sleep(2)
interface = find_interface()
ip_address = parse_ip()
last_set = ip_address[11:]


def send ( message):
    webhook = Webhook.from_url("WEBHOOK URL GOES HERE!", adapter=RequestsWebhookAdapter())
    webhook.send(message)
#    webhook.send(ip_address)

send( sys.argv[1] + " x.x.x." + last_set )
