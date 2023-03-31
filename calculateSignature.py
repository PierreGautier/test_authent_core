
import hmac
import hashlib, base64

def create_signature(key, data):
    sig_hash =  hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha512).digest()
    base64_message = base64.b64encode(sig_hash).decode()
    return base64_message

class SignatureManager:

    def getSignature(requestMethod, url, partner, salt):

        mySignature = create_signature(salt, requestMethod + ' ' + url)

        print(salt + " " + requestMethod + ' ' + url + ' => ' + mySignature)

        return mySignature



