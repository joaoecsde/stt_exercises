# ist193587

## Vulnerabilty

Endpoint is vulnerable to brute-force attack

## Where

Situated at mustard.stt.rnl.tecnico.ulisboa.pt Port 22055

## Impact

Allows to get the server's guess by multiple tries

## Steps to Reproduce

1. Run the file 'PwnTools_Sockets.py' 
2. This file what it does is make a remote process to the server and then after some interaction with the server we are able to see that the connection falls down after a while. So using 'recvline()' and splitting it we are able to get the target number, going through a while cycle we can type 'MORE' till we have the same number has the target, and type 'FINISH' as soon has we get it.