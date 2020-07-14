# Instructions

## Start server

```bash
python3 app.py
```

Flask will ask about the passphrase of the private key. Type `1234` for the test-use-only key.
Note that this key/cert only works for domain name `localhost`.

## Start client

Test whether the HTTPS server works.

```bash
curl https://localhost:6000/ --cacert rsa-4096-cert.pem
```

Load generator

```bash
./tls-load-gen.sh 10 https://localhost:6000/
```

## Setup files to host

```bash
./generate-files.sh
```

## Start generating load

This script will make use of client.

```bash
./generate-load.sh

```

## Log squid performance

```bash
./measure-performance.sh <squid-pid>
```

this will log the squid performance every 0.5 seconds to squid-measurement.log
