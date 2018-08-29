# hotp-python
## Example
### Generate OTP code
```python
secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()
code = OTP(secret, 8, 180).GenerateOtp()
```

### Verify OTP code
```python
secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()
otp = OTP(secret, 8, 180)
testCode = 123123

if otp.Verify(testCode):
  // success
else:
  // fail
```
