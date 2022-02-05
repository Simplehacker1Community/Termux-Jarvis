import subprocess
import os
import time
from datetime import datetime
import sys
from word2number import w2n
from num2words import num2words

now = datetime.now()
nt1 = "speak Your first number"
nt2 = "speak Your second number"
op = "speak Your math operator like addition subtraction multiplication division"
r = "the result is"
t=now.strftime('%I:%M:%p')

print(t)
inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("......",str(inp))


def instagram():
    subprocess.call(["termux-tts-speak","wait sir instagram is opening now"])
    os.system("termux-open https://instagram.com")
    time.sleep(3)
    subprocess.call(["termux-tts-speak","now instagram is successful open sir "])
    system()


def youtube():
    subprocess.call(["termux-tts-speak","wait sir YouTube is opening now"])
    os.system("termux-open https://youtube.com")
    time.sleep(3)
    subprocess.call(["termux-tts-speak","now YouTube is successful open sir "])
    system()


def security():
    os.system("termux-fingerprint")
    system()


def add():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) + w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def sub():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) - w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def mul():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) * w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def div():
    subprocess.call(["termux-tts-speak",nt1])
    n1 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n1))
    subprocess.call(["termux-tts-speak",nt2])
    n2 = subprocess.getoutput("termux-speech-to-text")
    print("......",str(n2))
    res = w2n.word_to_num(n1) / w2n.word_to_num(n2)
    print(res)
    result = num2words(res)
    print(result)
    subprocess.call(["termux-tts-speak",r,result])


def calculator():
    subprocess.call(["termux-tts-speak",op])
    inp = subprocess.getoutput("termux-speech-to-text")
    print("......",str(inp))
    if "addition" in inp:      
        add()
    elif "substraction" in inp:       
        sub()
    elif "multiplication" in inp:      
        mul()
    elif "division" in inp:      
        div()
    else:
        subprocess.call(["termux-tts-speak","wrong operator"])
    system()


def system():
     if inp == "":
         subprocess.call(["termux-tts-speak",'the time is',t])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])

     elif "YouTube" in inp:
         youtube()
 
     elif "Instagram" in inp:
         instagram()


     elif "Facebook" in inp:
         subprocess.call(["termux-tts-speak","wait sir Facebook is opening now"])
         os.system("termux-open https://facebook.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now Facebook is successful open sir "])

     elif "Google" in inp:
         subprocess.call(["termux-tts-speak","wait sir Google is opening now"])
         os.system("termux-open https://www.google.co.in/")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now Google is successful open sir "])

         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()

     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +91")

     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
     

     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am Jarvis version 1.0 your personal assistanct sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Jarvis "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by shubham gosai"])

     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     elif "calculator" in inp:
         calculator()


     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
 
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")
