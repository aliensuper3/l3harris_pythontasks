from cryptography.fernet import Fernet
import netaddr
key = Fernet.generate_key()
f = Fernet(key)

class encryptdecrypt:


    def __init__(self):
        key = Fernet.generate_key()
        self.f = Fernet(key)

    def encryptIP(self, ip_address):
        return self.f.encrypt(ip_address.encode())

    def decryptIP(self, ip_address):
        return self.f.decrypt(ip_address).decode()

    def obfuscateIP(self, ip_address):
        strToIP = self.encryptIP(ip_address)
        strToIP = strToIP.decode()[15:19]
        ipAddressToReturn = ""
        for letter in strToIP:
            ipAddressToReturn += str(ord(letter)) + "."
    
        ipAddressToReturn = ipAddressToReturn[:len(ipAddressToReturn)-1]
        return ipAddressToReturn

if __name__ == "__main__":
    hash = encryptdecrypt()
    print(hash.encryptIP("192.168.1.33"))

    print(hash.obfuscateIP("192.168.1.33"))

    print(hash.decryptIP(encryptIP("192.168.1.33")))