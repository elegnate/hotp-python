
import struct, time
import base64

from Crypto.Hash import SHA256, HMAC



class OTP(object):

    def __init__(self, secret, digits = 8, period = 30):
        self.secret = secret
        self.period = period
        self.digits = digits


    def Verify(self, code):
        code = int(code)
        ts = int(time.time())
        for i in range(-self.period, self.period + 1):
            counter = ts + i
            if self.GenerateOtp(counter) == code:
                return True
        return False


    def GenerateOtp(self, counter = None):
        # https://tools.ietf.org/html/rfc4226
        if counter == None:
            counter = int(time.time())

        msg = struct.pack('>Q', counter)
        digest = HMAC.new(self.secret, msg, SHA256).digest()

        pos = digest[19] & 15
        base = struct.unpack('>I', digest[pos:pos + 4])[0] & 0x7fffffff
        token = base % pow(10, digits)
        return token


    def _CompareDigest(self, a, b):
        rv = 0
        for x, y in zip(a, b):
            rv |= x ^ y
        return rv == 0
