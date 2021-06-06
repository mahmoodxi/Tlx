echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections
apt-get update
apt-get install python3-pip git net-tools -y
pip3 install requests flask names
git clone https://github.com/mahmoodxi/Tele /var/MTProxy
chmod +x /var/MTProxy/objs/bin/mtproto-proxy
wget https://raw.githubusercontent.com/mahmoodxi/Tlx/main/run.py -P /root
wget https://raw.githubusercontent.com/mahmoodxi/Tlx/main/run.service -P /etc/systemd/system
systemctl daemon-reload
systemctl restart run.service
systemctl enable run.service
