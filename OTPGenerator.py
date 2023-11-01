import hmac
import hashlib
import time


class OTPGenerator:
    def __init__(self, secret_key, hash_algorithm=hashlib.sha256):
        self.secret_key = secret_key
        self.hash_algorithm = hash_algorithm
   
    def _generate_hmac(self, counter):
        counter_bytes = counter.to_bytes(8, byteorder='big')
        hmac_digest = hmac.new(self.secret_key.encode(), counter_bytes, self.hash_algorithm).digest()
        return hmac_digest
   
    def generate_totp(self, time_step=30):
        current_time = int(time.time())
        hmac_digest = self._generate_hmac(current_time)
        offset = hmac_digest[-1] & 0x0F
        otp_value = hmac_digest[offset:offset+4]
        totp = int.from_bytes(otp_value, byteorder='big') % (10 ** 6)
        return totp
   
    def generate_hotp(self, counter):
        hmac_digest = self._generate_hmac(counter)
        offset = hmac_digest[-1] & 0x0F
        otp_value = hmac_digest[offset:offset+4]
        hotp = int.from_bytes(otp_value, byteorder='big') % (10 ** 6)
        return hotp
