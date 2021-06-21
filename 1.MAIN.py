#-----------MODULES IMPORT--------------------------------------
from tkinter import *
import ttk
import pymsgbox
import mail
import random
import time
import datetime
import face_recognize

#------------FUNCTIONS-----------------------------------------------

count1=0
count2=0
count3=0
count4=0

def can_name(name,c,r):
    one = ttk.Label(content, width=25, text=name)
    one.grid(column=c, row=r)
    
def party_name(party,c,r):
    two = ttk.Label(content, width=25, text=party)
    two.grid(column=c, row=r)

def party1():
  global count1
  count1=count1+1
  now = datetime.datetime.now()
  now = str(now)
  data=(str(count1)+" - Vote Registered"+ '\n')
  open('party1.txt', 'a').write(data)
  root.destroy()
  
def party2():
  global count2
  count2=count2+1
  now = datetime.datetime.now()
  now = str(now)
  data=(str(count2)+" - Vote Registered"+ '\n')
  open('party2.txt', 'a').write(data)
  root.destroy()
  
def party3():
  global count3
  count3=count3+1
  now = datetime.datetime.now()
  now = str(now)
  data=(str(count3)+" - Vote Registered"+ '\n')
  open('party3.txt', 'a').write(data)
  root.destroy()

def party4():
  global count4
  count4=count4+1
  now = datetime.datetime.now()
  now = str(now)
  data=(str(count4)+" - Vote Registered"+ '\n')
  open('party4.txt', 'a').write(data)
  root.destroy()

#---------------MAIN LOOP--------------------------
  
voters=[]

while 1:
    otp=random.randint(1000,9999)
    pymsgbox.alert(text="Shall I Start Face Recognition", title='Starting......!')
    voter= face_recognize.recognition()
    print (voter)
    if voter not in voters:
                if voter != None:
                    voters.append(voter)
                    print (voters)
                    mail_id=pymsgbox.prompt(text="enter your e-mail", title="OTP Verification.!!")
                    mail.send_mail("covai.dsp@gmail.com","cadencedsp",mail_id,message="HAPPY VOTING..!!! Your OTP :"+str(otp))
                    your_otp=pymsgbox.prompt(text="Enter your otp", title="OTP!")
                    
                    if (str(otp)==your_otp): 
                        root = Tk()
                        root.geometry("500x300")
                        root.title("Voting GUI")
                        content = ttk.Frame(root)
                        frame = ttk.Frame(content)
                        content.grid(column=0, row=0)
                        frame.grid(column=0, row=0, columnspan=3, rowspan=2)
                        
                        can_name("Erra",0,0)
                        party_name("madurai",1,0)
                        click = ttk.Button(content, width=15, text="Click", command=party1)
                        click.grid(column=2, row=0)
                        
                        can_name("Dinesh",0,1)
                        party_name("coimbatore",1,1)
                        click = ttk.Button(content, width=15, text="Click", command=party2)
                        click.grid(column=2, row=1)
                        
                        can_name("Gopi",0,2)
                        party_name("pollachi",1,2)
                        click = ttk.Button(content, width=15, text="Click", command=party3)
                        click.grid(column=2, row=2)
                        
                        can_name("Ari haran",0,3)
                        party_name("chennai",1,3)
                        click = ttk.Button(content, width=15, text="Click", command=party4)
                        click.grid(column=2, row=3)
                        
                        root.mainloop()
                        
                        pymsgbox.alert(timeout=3000,text="Your Vote Registered. ", title=" ...THANKS...")

                    else:
                       pymsgbox.alert(timeout=1000,text="Sorry... Invalid OTP. ", title=" ERROR..!!!")
                       
                else:
                    print (" Sorry.. You are Not eligible to Voting")
                    pymsgbox.alert(timeout=3000,text=" Sorry.. You are Not eligible to Voting", title=" ...WARNING...")
                    
    else:
        print ("Already your vote was Registered")
        pymsgbox.alert(timeout=3000,text=" Already your vote was Registered", title=" ...ILLEGAL ATEMPT...!!!")
        
         
