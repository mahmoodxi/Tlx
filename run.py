import requests
from time import sleep
import subprocess
import os
import flask
from flask import request

priv = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE).stdout
privip =  priv.read()
priv8 = privip.decode()
privfinish = priv8.replace("\n","")

app=flask.Flask(__name__)
@app.route("/check")
def main():
  secret = request.args.get('secret')
  tag = request.args.get('tag')
  tag2 = request.args.get('tag2')
  tls = request.args.get('tls')
  get = requests.get("https://icanhazip.com/")
  ip = str(get.text)
  ipfinish = ip.replace("\n","")

  os.system("systemctl stop mtp2")
  os.system("rm -rf /etc/systemd/system/mtp2.service")
  os.system("systemctl daemon-reload")
  with open("/etc/systemd/system/mtp2.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/MTProxy/objs/bin
ExecStart=/var/MTProxy/objs/bin/mtproto-proxy -u nobody -p 5000 -H 443 -S """+str(secret)+""" -P """+str(tag2)+""" -D """+str(tls)+""" --aes-pwd proxy-secret proxy-multi.conf -M 1
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp2.service")
  return "Its OK"

app.run(host="0.0.0.0",port=4444,debug=True)
