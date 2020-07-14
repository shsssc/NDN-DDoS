
#!/bin/bash
#Usage ./genlog.sh <command to rum> <file to write> <time between log in seconds>
true > $2
while true
do
    $1 | tee -a $2
    sleep $3
done

