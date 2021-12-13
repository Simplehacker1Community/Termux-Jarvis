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
print("\033[95m You said: ",str(inp))

def system():
     if inp == "hello Jarvis":
         subprocess.call(["termux-tts-speak","hallow sir"])

     elif "how are you Jarvis" in inp:
         subprocess.call(["termux-tts-speak","i am good what about you sir"])
     
     elif "I am also good fine" in inp:
         subprocess.call(["termux-tts-speak","that's good sir"])

     elif "who are you Jarvis" in inp:
         subprocess.call(["termux-tts-speak","I am Jarvis version 2.0 your personal assistanct sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing Jarvis" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you sir "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you sir"])
     
     elif "what is your name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Jarvis "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by shubhamg0sain"])

     elif "Jarvis open YouTube" in inp:
         subprocess.call(["termux-tts-speak","wait sir YouTube is opening now"])
         os.system("termux-open https://youtube.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now YouTube is successful open sir "])

 
     elif "Jarvis open instagram" in inp:
         subprocess.call(["termux-tts-speak","wait sir instagram is opening now"])
         os.system("termux-open https://instagram.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now instagram is successful open sir "])


     elif "Jarvis open facebook" in inp:
         subprocess.call(["termux-tts-speak","wait sir Facebook is opening now"])
         os.system("termux-open https://facebook.com")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now Facebook is successful open sir "])

     elif "Jarvis open Google browser" in inp:
         subprocess.call(["termux-tts-speak","wait sir Google is opening now"])
         os.system("termux-open https://www.google.co.in/")
         time.sleep(3)
         subprocess.call(["termux-tts-speak","now Google is successful open sir "])

     elif "Jarvis close Jarvis" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute Jarvis is closing"])
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

     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")
