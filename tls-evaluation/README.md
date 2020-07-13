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



