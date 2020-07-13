#! /bin/bash

curlpersecond="$1"
url=$2
date
echo "url: $url
rate: $curlpersecond calls / second"

get () {
  curl -s -v "$url" --cacert rsa-4096-cert.pem 2>&1 | tr '\r\n' '\\n' | awk -v date="$(date +'%r')" '{print $0"\n-----", date}' >> /tmp/perf-test.log
}

while true
do
  echo $(($(date +%s) - START)) | awk '{print int($1/60)":"int($1%60)}'
  sleep 1

  for i in `seq 1 $curlpersecond`
  do
    get $2 &
  done
done