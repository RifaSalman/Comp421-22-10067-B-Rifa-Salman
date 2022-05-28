print("    Name: Rifa Salman----------Roll No.: 22-10067------------Assignment:2")                          
import rsa

#generating public and private keys and righting them to files
def ppKeys():
    (keyPublic, keyPrivate) = rsa.newkeys(1024)
    p=open('keys/keyPublic.pem', 'wb')
    p.write(keyPublic.save_pkcs1('PEM'))
    p=open('keys/keyPrivate.pem', 'wb')
    p.write(keyPrivate.save_pkcs1('PEM'))

#reading the generated public and private keys from the files 
def readKeys():
    p=open('keys/keyPublic.pem', 'rb')
    keyPublic = rsa.PublicKey.load_pkcs1(p.read())
    p=open('keys/keyPrivate.pem', 'rb')
    keyPrivate = rsa.PrivateKey.load_pkcs1(p.read())
    return keyPrivate, keyPublic

#encryting the text
def encryption(text, key):
    return rsa.encrypt(text.encode('ascii'), key)

#decrypting the text
def decryption(encodedText, key):
    try:
        return rsa.decrypt(encodedText, key).decode('ascii')
    except:
        return False


#driver code
ppKeys()
keyPrivate, keyPublic =readKeys()

choice=input("Press (A) to enter message\nPress (B) to read from a file")

while choice!="A" or choice!="a" or choice!="B" or choice!="b":
    if choice=="A" or choice=="a":
        x = input('Write your message here:')
        break
    elif choice=="B" or choice=="b":
         filename = input('Please enter filename:')
         if not filename.endswith('.txt'):
             f=open(filename+'.txt',"r")
         else:
             f=open(filename,"r")
         x=f.read()
         break
    else:
        choice=input("Please enter appropriate option")
encodedText = encryption(x, keyPublic)

decryptedText = decryption(encodedText, keyPrivate)

print('\nCipher text:',encodedText)
print('Public Key:',keyPublic)

if decryptedText:
    print('\nDecrypted text:',decryptedText)
    print('Private Key:', keyPrivate)
else:
    print('Message decryption failed!.')
