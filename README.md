# hotp-python
<br>
<h2>Example</h2>
<br>
<h3>Generate OTP code</h3>
<code>secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()</code><br>
<code>code = OTP(secret, 8, 180).GenerateOtp()</code><br>
<br>
<h3>Verify OTP code</h3>
<code>secret = HMAC.new(b'plain messange', b'secret information', SHA256).digest()</code><br>
<code>otp = OTP(secret, 8, 180)</code><br>
<code>testCode = 123123</code><br>
<br>
<code>if otp.Verify(testCode):</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;// success<br>
<code>else:</code><br>
&nbsp;&nbsp;&nbsp;&nbsp;// fail<br>
