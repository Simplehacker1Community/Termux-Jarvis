import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("......",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak",'the time is',t])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])

     elif "YouTube" in inp:
         subprocess.call(["termux-tts-speak","wait sir YouTube is opening now"])
         os.system("termux-open https://youtube.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now YouTube is successful open sir "])

 
     elif "Instagram" in inp:
         subprocess.call(["termux-tts-speak","wait sir instagram is opening now"])
         os.system("termux-open https://instagram.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now instagram is successful open sir "])


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

     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir what about you"])

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
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
 
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")
