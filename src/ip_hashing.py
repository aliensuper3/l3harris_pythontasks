from cryptography.fernet import Fernet
import netaddr
key = Fernet.generate_key()
f = Fernet(key)

def encryptIP(ip_address):
    return f.encrypt(ip_address.encode())

def decryptIP(ip_address):
    return f.decrypt(ip_address).decode()

def obfuscateIP(ip_address):
    strToIP = encryptIP(ip_address)
    strToIP = strToIP.decode()[15:19]
    ipAddressToReturn = ""
    for letter in strToIP:
        ipAddressToReturn += str(ord(letter)) + "."
    
    ipAddressToReturn = ipAddressToReturn[:len(ipAddressToReturn) -1]
    return ipAddressToReturn


#print(encryptIP("192.168.1.33"))

print(obfuscateIP("2.220.44.33"))

#print(decryptIP(encryptIP("192.168.1.33")))