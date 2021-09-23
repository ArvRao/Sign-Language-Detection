# import text
import predict
s=""
s1=""
keys='?\'\().,/":-1234567890abcdefghijklmnopqrstuvwxyz !'
value = keys[-1] + keys[0:-1]
encryptDict = dict(zip(keys,value))
decryptDict = dict(zip(value,keys))
message ='Greetings' #Here e.word() is the orginal word.
print("The Original Message:")
print(message)
newMessage= ''.join([encryptDict[letter] for letter in message.lower()])
newMessage1=newMessage[len(newMessage)//2:]+newMessage[:len(newMessage)//2]
for i in newMessage1:
    b=bin(ord(i))
    s=s+"|"+str(b[2:])
print(" ")
print("The Encoded Message")
print(s)
s=s.split('|')
for i in s:
    if i=="":
        pass
    else:
        d=int(i,2)
        s1=s1+chr(int(d))
newMessage2= ''.join([decryptDict[letter] for letter in s1.lower()])
if(len(newMessage2)%2==0):
    newMessage3=newMessage2[len(newMessage2)//2:]+newMessage2[:len(newMessage2)//2]
else:
    newMessage3=newMessage2[len(newMessage2)//2+1:]+newMessage2[:len(newMessage2)//2+1]
print(" ")
print("The Decoded Message or Original Message:")
print(newMessage3.capitalize())
