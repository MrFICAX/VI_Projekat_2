#from msilib import text
from cryptography.fernet import Fernet
import os

def dekodiraj():
    if os.path.isfile('passw.txt'):
        f=open('passw.txt','r')
        message = f.read()
        textEnc=''
        number=0
        for line in message.splitlines():
            if number!=0:
                textEnc=textEnc+line
            else:
                keyFinnal=line
            number=number+1
        keyFinnal=bytes(keyFinnal,'utf-8')
        textEnc=bytes(textEnc, 'utf-8')
        fernet = Fernet(keyFinnal)  
        textDec = fernet.decrypt(textEnc).decode()
        f.close()
        return (textDec,keyFinnal)

def vratiDict(stringic):
    pom=dict()
    for line in stringic.splitlines():
        if line=='zeljko' or line=='filip' or line=='veljko':
            #pom[line]=list()
            pomm=line
        elif line!='':
            pommm=dict()
            pommm[line.split(' ')[0]]=line.split(' ')[1]
            pom[pomm]=pommm
    return pom

def generisiText(dct):
    stringic=str()
    for d in dct:
        stringic=stringic+'\n'+d
        for i in dct[d]:
            stringic=stringic+'\n'+i+' '+dct[d][i]
    return stringic

def unesiStanje(kome, writeIn, writePass):
    if os.path.isfile('passw.txt'):
        textDec = dekodiraj()[0]
        keyFinnal = dekodiraj()[1]
        fernet = Fernet(keyFinnal) 
        sve=vratiDict(textDec)

        if kome in sve:
            for i in list(sve[kome]):
                print(i)
                if i==writeIn:
                    sve[kome].pop(i)
                    sve[kome][i]=writePass
            if writeIn not in list(sve[kome]):
                sve[kome][writeIn] = writePass
        else:
            pom=dict()
            pom[writeIn]=writePass
            sve[kome]=pom
        textDec=generisiText(sve)
    else:
        keyFinnal = Fernet.generate_key()
        fernet = Fernet(keyFinnal) 
        textDec=kome+'\n'+writeIn+' '+writePass+'\n'

    f=open('passw.txt','w+')
    encMessage=keyFinnal.decode("utf-8") +'\n'+fernet.encrypt(textDec.encode()).decode('utf-8')
    f.write(encMessage)
    f.close()
    return True

def vratiKljucem(ko, sta):
    if os.path.isfile('passw.txt'):   
        textDec = dekodiraj()[0]
        pom=vratiDict(textDec)
        
        if ko in pom:
            if sta in pom[ko]:
                return (True, pom[ko][sta])
        return (False, '')
    else:
        return (False, '')


unesiStanje("filip","facebook", "komp123")
a = vratiKljucem("filip", "facebook")
print(a)