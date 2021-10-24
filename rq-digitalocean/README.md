This was my first experience with redis queue. 3 droplets are used. 1 server and 2 worker droplets.

server setup commands:
apt update && sudo apt upgrade
apt install python3-pip, redis
pip install rq
mkdir app
cd app
cp count_words.py, main.py
sed -i 's/bind 127.0.0.1/0.0.0.0/g' /etc/redis/redis.conf
systemctl restart redis
python main.py

worker setup commands:

apt update && sudo apt upgrade -y
apt install phthon3-pip
pip install rq
cp count_words.py
rq worker -u redis://143.198.177.144:6379

Essentially you install the update/install packages, copy over the files, and run the process. Client receives a copy of the function to run. Must be installed on both server & client.
