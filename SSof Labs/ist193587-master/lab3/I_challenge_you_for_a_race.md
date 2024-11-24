# ist193587

## Vulnerabilty

Problem of concurrency/lack of proper synchronization

## Where

Situated in the verification of the access to read file

## Impact

Allows to read a file that the user doesn't have permission to do it

## Steps to Reproduce

1. Open two terminals, in which one of them do the ssh connection with the user and then place the password
2. Since we can write in the tmp folder we make a directory with a random name, example used: mine, and inside it create 2 bash scripts 1 that has 'challenge_for_a_race.sh' content the other that has 'run_chalenge.sh' content. Do 'chmod a+x {name_of_script}' so we can run them.
3. With the scripts placed we run 1 in one machine and the other script in the other, when we can see the content of the file /challenge/flag we can stop the scripts.
4. Explaining the scripts: 'run_challenge.sh' tries to read content from a pointer named 'good.txt', 'challenge_for_a_race.sh' creates a txt file in the directory /tmp/mine and from there indefinitely switches the pointer from the file it created (since the user can read it) and the flag, if we get lucky since it is a race the user will be able to read from the pointer when this one is pointing to the flag