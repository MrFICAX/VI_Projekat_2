import re
import time
import Alexa2 as A2
import speech_recognition as sr
import radsafajlom as RF
#import FaceRecognition as FR
r = sr.Recognizer()
alexa = A2.Alexa2()




def UnesiSifru():
    counter = 0
    TopCounter = 3
    ime = ""
    imeNaloga = ""
    sifra = ""
    while counter < TopCounter:
        if languageSet == "en-US":
            if counter == 0:
                imeFlag = True
                while imeFlag:
                    print("Say your name:")
                    alexa.SaySomething(
                        "Say your name ", languageType, languageSpeedIsSlow)

                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Input name is  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            ime = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeFlag = False
                        else:
                            alexa.SaySomething(
                                " Name not recognized", languageType, languageSpeedIsSlow)
            elif counter == 1:
                imeNalogaFlag = True
                while imeNalogaFlag:
                    print("Say account name:")
                    alexa.SaySomething(
                        "Say account name ", languageType, languageSpeedIsSlow)
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Input account name is  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            imeNaloga = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeNalogaFlag = False
                        else:
                            alexa.SaySomething(
                                " Account name not recognized", languageType, languageSpeedIsSlow)

            elif counter == 2:
                sifraFlag = True
                while sifraFlag:
                    print("Input password:")
                    alexa.SaySomething(
                        "Input password ", languageType, languageSpeedIsSlow)
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Input password is  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            sifra = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                sifraFlag = False
                        else:
                            alexa.SaySomething(
                                " Account password not recognized", languageType, languageSpeedIsSlow)
        else:
            if counter == 0:
                imeFlag = True
                while imeFlag:
                    print("Unesite vase ime:")
                    alexa.SaySomething(
                        "Unesite vase ime ", languageType, languageSpeedIsSlow)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Uneto ime je " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            ime = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeFlag = False
                        else:
                            alexa.SaySomething(
                                " Ime nije prepoznato", languageType, languageSpeedIsSlow)
            if counter == 1:
                profilFlag = True
                while profilFlag:
                    print("Unesite ime profila:")
                    alexa.SaySomething(
                        "Unesite ime profila ", languageType, languageSpeedIsSlow)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Ime unetog profila je  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            imeNaloga = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                profilFlag = False

                        else:
                            alexa.SaySomething(
                                " Ime profila nije prepoznato", languageType, languageSpeedIsSlow)

            if counter == 2:
                sifraFlag = True
                while sifraFlag:
                    print("Unesite sifru:")
                    alexa.SaySomething(
                        "Unesite sifru ", languageType, languageSpeedIsSlow)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:

                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                            r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            text = ""
                            for i in PrepoznatiTekst.split(" "):
                                    text = text + i
                            PrepoznatiTekst = text
                            if " " not in PrepoznatiTekst:
                                alexa.SaySomething(
                                    "Uneta sifra je " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                                sifra = PrepoznatiTekst
                                if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                    counter += 1
                                    sifraFlag = False
                            else:
                                alexa.SaySomething(
                                    " Sifra ne sme da sadrzi razmak", languageType, languageSpeedIsSlow)
                        else:
                            alexa.SaySomething(
                                " Nije prepoznata sifra", languageType, languageSpeedIsSlow)
    if counter == TopCounter:
        RF.unesiStanje(ime, imeNaloga, sifra)

def PribaviSifru():
    counter = 0
    TopCounter = 2
    ime = ""
    imeNaloga = ""
    sifra = ""
    while counter < TopCounter:
        if languageSet == "en-US":
            if counter == 0:
                imeFlag = True
                while imeFlag:
                    print("Say your name:")
                    alexa.SaySomething(
                        "Say your name ", languageType, languageSpeedIsSlow)

                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                              r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Input name is  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            ime = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeFlag = False
                        else:
                            alexa.SaySomething(
                                " Name not recognized", languageType, languageSpeedIsSlow)
            elif counter == 1:
                imeNalogaFlag = True
                while imeNalogaFlag:
                    print("Say account name:")
                    alexa.SaySomething(
                        "Say account name ", languageType, languageSpeedIsSlow)
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                              r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Input account name is  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            imeNaloga = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeNalogaFlag = False
                        else:
                            alexa.SaySomething(
                                " Account name not recognized", languageType, languageSpeedIsSlow)

        else:
            if counter == 0:
                imeFlag = True
                while imeFlag:
                    print("Unesite vase ime:")
                    alexa.SaySomething(
                        "Unesite vase ime ", languageType, languageSpeedIsSlow)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                              r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Uneto ime je " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            ime = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                imeFlag = False
                        else:
                            alexa.SaySomething(
                                " Ime nije prepoznato", languageType, languageSpeedIsSlow)
            if counter == 1:
                profilFlag = True
                while profilFlag:
                    print("Unesite ime profila:")
                    alexa.SaySomething(
                        "Unesite ime profila ", languageType, languageSpeedIsSlow)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    try:
                        print("Google Speech Recognition thinks you said " +
                              r.recognize_google(audio, language=languageSet))
                        recognized = True
                        PrepoznatiTekst = str(r.recognize_google(
                            audio, language=languageSet)).lower()
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        recognized = False
                    except sr.RequestError as e:
                        print(
                            "Could not request results from Google Speech Recognition service; {0}".format(e))
                    finally:
                        if recognized == True:
                            alexa.SaySomething(
                                "Ime unetog profila je  " + PrepoznatiTekst, languageType, languageSpeedIsSlow)
                            imeNaloga = PrepoznatiTekst
                            if potvrdiUlaz(languageSet, languageType, languageSpeedIsSlow):
                                counter += 1
                                profilFlag = False

                        else:
                            alexa.SaySomething(
                                " Ime profila nije prepoznato", languageType, languageSpeedIsSlow)

    if counter == TopCounter:
        povratnaVrednost = RF.vratiKljucem(ime, imeNaloga)
        if povratnaVrednost[0]:
            if languageSet == "en-US":
                alexa.SaySomething(
                    " Password is" + str(povratnaVrednost[1]), languageType, languageSpeedIsSlow)
            else:
                alexa.SaySomething(
                    " Sifra je " + str(povratnaVrednost[1]), languageType, languageSpeedIsSlow)

def potvrdiUlaz(languageSet, languageType, languageSpeed):

    while(True):

        if languageSet == "en-US":
            alexa.SaySomething(
                " Do you agree with the input, say YES OR NO", languageType, languageSpeedIsSlow)
        else:
            alexa.SaySomething(
                " Da li se slazete sa ulazom, recite DA ILI NE", languageType, languageSpeedIsSlow)
        # for i in range(3, 0, -1):
        #     time.sleep(1)
        #     print("Start speaking in:" + str(i))
        print("Say something!")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " +
                  r.recognize_google(audio, language=languageSet))
            recognized = True
            PrepoznatiTekst = str(r.recognize_google(
                audio, language=languageSet)).lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            recognized = False
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        finally:
            if recognized == True:

                if(languageSet == "sr-SP"):
                    if PrepoznatiTekst.startswith("da"):
                        alexa.SaySomething(
                            "Potvrđeno!", languageType, languageSpeedIsSlow)
                        return True
                    if PrepoznatiTekst.startswith("ne"):
                        alexa.SaySomething(
                            "Nije potvrdjeno!", languageType, languageSpeedIsSlow)
                        return False   
                else:
                    if PrepoznatiTekst.startswith("yes"):
                        alexa.SaySomething(
                            "Proceed with the input!", languageType, languageSpeedIsSlow)
                        return True

                    if PrepoznatiTekst.startswith("no"):
                        alexa.SaySomething(
                            "Say again ", languageType, languageSpeedIsSlow)
                        return False
            else:
                return False


# try:

# if not FR.recognizeFaceFromCamera():
#     print("Face not recognized")
#     exit


languageSet = ""
languageType = 'en'
languageSetFlag = True
languageSpeedIsSlow = True
languageSpeedIsFast = not languageSpeedIsSlow
while languageSetFlag:
    print("Choose language:")
    print("\tAvailable languages:")
    print("\t\tSERBIAN:")
    print("\t\tENGLISH:")
    alexa.SaySomething(
        "Available languages "+
        " SERBIAN "+
        "ENGLISH"
        , languageType, languageSpeedIsSlow)
    # for i in range(3,0,-1):
    #     time.sleep(1)
    #     print("Start speaking in:" + str(i))
    print("Say something!")

    with sr.Microphone() as source:
        audio = r.listen(source) 

    print(r.recognize_google(audio))
    if str(r.recognize_google(audio)).startswith("Serb"):
        languageSet = "sr-SP"
        languageSetFlag = False
        languageType = 'sr'
    else:
        languageSet = "en-US"
        languageSetFlag = False
        languageType = 'en'


if languageSet == "en-US":
    print("Available commands:")
    print("\tHello friend, my name is:")

    alexa.SaySomething(
        "Available commands "+
        " Hello friend, my name is "+
        " exit application"+
        " Input password"+
        " Get password"
        , languageType, languageSpeedIsSlow)
else:
    print("\tDostupne komande:")
    print("\tPozdrav ja sam:")
    print("\tUgasi aplikaciju:")
    print("\tUnesi Sifru:")

    alexa.SaySomething(
        "Dostupne komande "+
        " Pozdrav ja sam, pa vaše ime"+
        " Ugasi aplikaciju "+
        " Unesi šifru"+
        " Pribavi šifru"            
        , languageType, languageSpeedIsSlow)

while(True): 
    if languageSet == "en-US":
        alexa.SaySomething("Input command", languageType, languageSpeedIsSlow)
    else:
        alexa.SaySomething("Unesite neku komandu", languageType, languageSpeedIsSlow)

    # for i in range(3,0,-1):
    #     time.sleep(1)
    #     print("Start speaking in:" + str(i))
    print("Say something!")
    with sr.Microphone() as source:
        audio = r.listen(source)  
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language=languageSet))
        recognized = True
        PrepoznatiTekst = str(r.recognize_google(audio, language=languageSet)).lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        recognized = False
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        if recognized == True:




            if(languageSet == "sr-SP"):
                if PrepoznatiTekst.startswith("ugasi"):
                    alexa.SaySomething("Doviđenja!", languageType, languageSpeedIsSlow)
                    break
                if PrepoznatiTekst.startswith("pozdrav"):
                    alexa.SaySomething("Pozdrav: " + PrepoznatiTekst.split("sam")[1], languageType, languageSpeedIsSlow)
                if PrepoznatiTekst.startswith("unesi"):
                    UnesiSifru()
                if PrepoznatiTekst.startswith("pribavi"):
                    PribaviSifru()
            else:





                if PrepoznatiTekst.startswith("exit"):
                    alexa.SaySomething("Goodbye!", languageType, languageSpeedIsSlow)
                    break
                if PrepoznatiTekst.startswith("hello"):
                    alexa.SaySomething("hello: " + PrepoznatiTekst.split("is")[1], languageType, languageSpeedIsSlow)
                if PrepoznatiTekst.startswith("input"):
                    UnesiSifru()
                if PrepoznatiTekst.startswith("get"):
                    UnesiSifru()
# except:
#     print("Greška u kodu")
#     alexa.SaySomething("Error in code " if languageType == 'en' else "Greška u kodu", languageType, languageSpeedIsSlow)



