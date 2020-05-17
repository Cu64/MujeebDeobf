#-*- coding: utf-8 -*-

import os
import sys
import time
import colorama
from colorama import *
import sys

def slowprint(s):
    for c in s + '
':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 100)

def again():
      run = raw_input("\033[1;91m
=> [l]\033[1;92m exit\033[1;96m or \033[1;91m[Enetr]\033[1;92m continue ? [l / enter] =\033[1;96m  ")
      if run=='l':
         print('Exiting......')
         time.sleep(0.5)
         print("             \033[1;92mThank You For Using T-Speak !")
         time.sleep(1)
         print("")
         os.system("echo ---------------------------------------------- | lolcat")
         os.system("echo [ ------T-Speak By Mujeeb ------] | lolcat")
         print("")
      else:
         os.system("clear")
         logo()
         main()

def td():
     time.sleep(1)

os.system("clear")
time.sleep(0.5)
def logo():
      print("\033[0;34m")
      print("\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 v1.0")
      print("\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d")
      print("   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d")
      print("   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97")
      print("   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97")
      print("   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d")
      print("\033[1;97m----------------\033[44mTermux-Speak-Engin\033[00m\033[1;97m------------------")
      print("")

def author():
           pt()
           os.system("echo -------[ Author Information ]------- | lolcat")
           print("\033[1;96m")
           print("Name    : Mujee)
           print("Youtube : www.youtube.com/TechnicalMujee)
           print("Github  : https://github.com/TechnicalMujeeb/Termux-speak.git")
           pt()
           os.system("echo ------[ Technical Mujeeb ]------| lolcat -a -d 120")
           pt()

def pt():
      print("")

def main():
      print("\033[1;94m(1)..\033[1;36m speak Engin Info ")
      pt()
      print("\033[1;94m(2)..\033[1;36m Speak Now ")
      pt()
      print("\033[1;94m(3)..\033[1;36m Author ")
      pt()
      time.sleep(0.2)
      op = raw_input("\033[1;93m \033[1;91mT-SPEAK\033[1;94m@\xe2\x94\x80\xe2\x9d\xaf \033[1;92m ")
     
      if op=='1':
           pt()
           slowprint("using this command you get information about the 
 text-to-speach (TTS) engines. 
 And the name of an engin may be given to the 
 termux-tts-speak.") 
           pt()
           pr = raw_input("\033[1;96mPress \033[1;91mENTER \033[1;96mto see (TTS) Engin Inforamation. ")
           os.system("termux-tts-engines")
           os.system("echo -----------------------------------------| lolcat -a -d 30")
           again()
      elif op=='3':
           author()
           again()
      elif op=='2':
           pt()
           slowprint("Lets speak with engin...")
           pt()
           speak = raw_input(Fore.CYAN + " Enter Your Text :\033[1;92m ")
           pt()
           print("\033[4;93mSelect Pitch \033[00m")
           pt()
           print("\033[1;91m(1)..\033[1;92m 1.0 ")
           print("\033[1;91m(2)..\033[1;92m 2.0 ")
           print("\033[1;91m(3)..\033[1;92m 3.0 ")
           print("\033[1;91m(4)..\033[1;92m 4.0 ")
           print("\033[1;91m(5)..\033[1;92m 5.0 ")
           print("\033[1;91m(6)..\033[1;92m custom ")
           pt()
           pitch = raw_input(Fore.CYAN + "Enter Pitch : \033[1;92m")
           if pitch=='1':
               a = ("-p 1.0")
           elif pitch=='2':
               a = ("-p 2.0")
           elif pitch=='3':
               a = ("-p 3.0")
           elif pitch=='4':
               a = ("-p 4.0")
           elif pitch=='5':
               a = ("-p 5.0")
           elif pitch=='6':
               cu = raw_input(Fore.CYAN +"Enter custom pitch :\033[1;92m ")
               a = ("-p " +cu)

           pt()
           print("\033[4;93mSelect Rate\033[00m")
           pt()
           print("\033[1;91m(1)..\033[1;92m 0.5 ")
           print("\033[1;91m(2)..\033[1;92m 0.8 ")
           print("\033[1;91m(3)..\033[1;92m 1.0 ")
           print("\033[1;91m(4)..\033[1;92m 2.0 ")
           print("\033[1;91m(5)..\033[1;92m 3.0 ")
           print("\033[1;91m(6)..\033[1;92m custom ")
           pt()
           rate = raw_input(Fore.CYAN +"Enter Rate : \033[1;92m")
           if rate=='1':
              b = ("-r 0.5")
              td()
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           elif rate=='2':
              b = ("-r 0.8")
              td()
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           elif rate=='3':
              b = ("-r 1.0")
              td()
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           elif rate=='4':
              b = ("-r 2.0")
              td()
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           elif rate=='5':
              b = ("-r 3.0")
              td()
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           elif rate=='6':
              kkk = raw_input(Fore.CYAN +"Enter custom rate value :\033[1;92m")
              b = ("-r " +kkk)
              os.system('termux-tts-speak '+ a + ' ' + b + ' ' +speak)
              again()
           else:
              td()
              logo()
              main()
      else:
           td()
           os.system('clear')
           logo()
           main()

logo()
main()
