# hotp-python
<br>
<h2>Example</h2>
<br>
<h3>Generate OTP code</h3>
secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()<br>
code = OTP(secret, 8, 180).GenerateOtp()<br>
<br>
<h3>Verify OTP code</h3>
secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()<br>
otp = OTP(secret, 8, 180)<br>
testCode = 123123<br>
<br>
if otp.Verify(testCode):<br>
&nbsp;&nbsp;&nbsp;&nbsp;// success<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;// fail<br>
