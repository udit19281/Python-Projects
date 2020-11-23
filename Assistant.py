import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from time import sleep
from selenium import webdriver
import os
import smtplib
import pywhatkit as kit

#Update chrome web driver path
driverpath="C:\\Chromedriver"

eng=pyttsx3.init('sapi5')

def say(aud):
    print(aud)
    eng.say(aud)
    eng.runAndWait()

def greet():
    d=datetime.datetime.now()
    if(d.hour>5 and d.hour<12): say("GOOD MORNING ")
    elif(d.hour>12 and d.hour<17): say("GOOD AFTERNOON ")
    else :say('GOOD EVENING ')
    say('HOW MAY I HELP YOU ?')

def date():
    d=datetime.datetime.now()
    s="Date is "+str(d.day)+" "+str(d.month)+" "+str(d.year)
    say(s)
    t="Time is "+str(d.hour)+":"+str(d.minute)
    if(d.hour<12): t=t+"A" +"M"
    else: t=t+"P"+"M"
    say(t)
    if(d.hour>7 and d.hour<12): say("GOOD MORNING")
    elif(d.hour<7): say("DARK NIGHT GO AND SLEEP")
    elif(d.hour>=12 and d.hour<18): say(" GOOD EVENING WHAT ARE YOU GOING TO DO TODAY ?")
    else : say("TIME TO SLEEP")

def sendmail(sendto,content): 
    ser=smtplib.SMTP("smtp.gmail.com",587)
    ser.ehlo()
    ser.starttls()
    email=input("Enter Email: ")
    password=input("Enter Password: ")
    ser.login(email,password)
    ser.sendmail(email,sendto,content)
    ser.close()

def takecomm(): 
    #obtain audio from microphone
    r=sr.Recognizer()
    with sr.Microphone() as source:
        say("Listening")
        #sleep(0.5)
        r.pause_threshold=1
        audio=r.listen(source,timeout=60,phrase_time_limit=10)
    try:
        q=r.recognize_google(audio,language='en-in')
        print("[+] RECOGNIZING....")
        say("COMMAND RECEIVED "+q)
    except Exception as e:
        #say(e.message)
        print(e)
        print("NO COMMAND RECEIVED")
        return "None"
    return q


if __name__ == "__main__":
    greet()
    r=0
    while r==0:
        query=takecomm().lower()
        if(query=="None"):
            print("No Command given")
        elif 'wikipedia' in query:
            say("SEARCHING WIKIPEDIA :")
            q=query.replace('wikipedia',"")
            try:
                results=wikipedia.summary(q,sentences=3)
                say(results)
                #sleep(5)
            except:
                say('COULD NOT LOAD RESULTS PLEASE TRY AGAIN ')

        elif "shutdown" in query:
             say("shutting down computer")
             os.system("shutdown /s /t 1")
             r=1
             break 

        elif 'exit' in query or "stop" in query:
            say("exiting the code good bye :) ")
            r=1
            break

        elif "wait" in query:
            sleep(600)
            
        elif "open youtube" in query :
            say("Opening youtube")
            query=query.replace('open youtube',"")
            driver=webdriver.Chrome(driverpath)

            if "and search for" in query:
                query=query.replace("and search for","")
            elif "search for" in query:
                query=query.replace("search for","")
            elif "play" in query:
                query=query.replace("play","")
            else: query=query.replace("search","")
            query=query.strip()
            driver.get("https://www.youtube.com/results?search_query=" + str(query))
            say("searching for"+query)
            driver.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()
            sleep(5)

        elif "what can you do" in query or "who are you" in query or "introduce yourself" in query or "about yourself" in query:
            print("Hye, I am your Assistant made with love by udit")
            print("List of Commands: ")
            print("Open Instagram")
            print("Gooogle search for _topic__")
            print("play spotify")  
            print("open youtube and search for __topic_")
            print("Open youtube and search for _topic__")
            print("Open youtube and play __topic_")
            print("wikipedia __topic__")
            print("shutdown")
            print("date")
            print("wait") #pause Assitant
            print("exit") #exit from code

        elif "google" in query  or "search" in query:
            driver=webdriver.Chrome(driverpath)
            if "open google" in query:query=query.replace('open google',"")
            if "and search for" in query:query=query.replace('search for',"")
            if "google" in query:query=query.replace('google',"")
            if "search on" in query:query=query.replace('search',"")
            if "search" in query:query=query.replace('search on',"")
            if "about" in query:query=query.replace('about',"")
            #if "search" in query:query=query.replace('search for',"")
            #if "and search for" in query:query=query.replace('and search for',"")
            query=query.strip()
            s=query
            query=query.replace(' ','+')
            say("opening google with query"+s)
            driver.get("https://www.google.com/search?q="+query)
            sleep(0.5)
            driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/a/h3").click()

        elif "open instagram" in query or "instagram" in query:
            #q=query.replace('open instagram',"")
            driver=webdriver.Chrome(driverpath)
            driver.get("https://www.instagram.com/")
            say("opening instagram")
            sleep(1.5)
            seluser="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
            selpass="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
            sellogin="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button/div"
            say("Enter login details ")
           
            try:
                username=input("Enter username: ")
                driver.find_element_by_xpath(seluser).send_keys(username)
                password=input("Enter password: ")
                driver.find_element_by_xpath(selpass).send_keys(password)
                driver.find_element_by_xpath(sellogin).click()
                sleep(4)
                say('Instagram logged in successfully')
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
                sleep(2)
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
                sleep(2)
               
            except Exception as e:
                print(e)
                say("Instagram login failed")
           

        elif "play spotify" in query or "spotify" in query:
            driver=webdriver.Chrome(driverpath)
            driver.get("https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg")
            say("opening spotify")
            #sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]").click()
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[1]/div[2]/p/button").click()
            sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/a").click()
            sleep(1)
            say("enter login details")
            usernamespotify=input("Enter spotify user name ")
            passwordspotify=input("Enter spotify password")
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(usernamespotify)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(passwordspotify)
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button").click()
            except Exception as e:
                say("Login failed")
            sleep(10)
            #sleep(60000)
        elif "date and time" in query or "time" in query or "date" in query:
            date()
        
            
       
#code by udit19281