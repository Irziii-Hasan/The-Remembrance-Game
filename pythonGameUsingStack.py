""" Irza Hasan 2021/Comp/BS(SE)/27037
 Object: Heap sorting
 Date:May 2022"""
from tkinter import *
import tkinter
import time
import sys
import random
from tkinter import ttk

def Instructions():         #step 2a
    wind=tkinter.Tk()
    wind.title("Remembrance Game")
    wind.geometry("800x550")
    wind.configure(bg="#ba042b")
    exit1=Label(wind, text="Instructions Here...!",
                 bg="Black",
                 fg="White",
                 font="KdamThmorPro 40 bold",
                 justify="center").pack(pady=25)

    label1=Label(wind, text="5 digit will show to you for 5 second \n you have to remember these digits\n after 5 second the digit will disappear\n now you have to write these digits \n through your keyboard\n if all of them are correct \n you will win the game!",
                 bg="#d9ba79",
                 fg="Black",
                 font="KdamThmorPro 22 ",
                 justify="center").pack(ipady=10,ipadx=10)


    exitButton=Button(wind,text="Exit",font="KdamThmorPro 25 bold",bg="Black",fg="White", command=wind.destroy).pack(side=BOTTOM,pady=40, ipady=10,ipadx=30)



        



#startGame
def startGame():            #step 2b
    wind=tkinter.Tk()
    wind.title("Remembrance Game")
    wind.geometry("1000x600")
    wind.configure(bg="#d9ba79")

    label1=Label(wind, text="The Remembrance Game",
                 bg="#d9ba79",
                 fg="Black",
                 font="KdamThmorPro 45 ",
                 justify="center").pack(ipady=30,ipadx=10)
    
    exit1=Label(wind, text="Game Begins",
                 bg="Black",
                 fg="White",
                 font="KdamThmorPro 20 bold",
                 justify="center").pack(pady=25)


    exitButton=Button(wind,text="Exit",font="KdamThmorPro 25 bold",bg="Black",fg="White", command=wind.destroy).pack(side=BOTTOM,pady=10, ipady=10,ipadx=30)


        
    def shownum():          #creating random number
        stack=[]
        CompVal=0
        for x in range(0,5):
            compVal=random.randint(0,9)
            #print(val)
            stack.append(compVal)
        print(stack)
        return stack

    computerStack=shownum()     #calling random Number's function(shownum)

    #showing random numbers to user
    li=Label(wind,text=computerStack,width=20,font="KdamThmorPro 40 bold",bg="White",fg="Black").pack(pady=2,padx=10, ipady=1,ipadx=3)

    #set timer
    def countdown():
        
        wind.update()
        
        t=5
        minutes=0
        wind.after(5000,lambda:wind.destroy())
        for x in range(5,0,-1):
            if t==0:
                li=Label(wind,text=x,width=20,font="KdamThmorPro 11 bold",bg="White",fg="Black").pack(side=LEFT,pady=3,padx=3, ipady=3,ipadx=3)
            s=str(t)
            if(len(s)==1):
                li=Label(wind,text=x,width=20,font="KdamThmorPro 11 bold",bg="White",fg="Black").pack(side=LEFT,pady=3,padx=3, ipady=3,ipadx=3)

            else:
                li=Label(wind,text=x,width=20,font="KdamThmorPro 11 bold",bg="White",fg="Black").pack(side=LEFT,pady=3,padx=3, ipady=3,ipadx=3)

            wind.update()
            time.sleep(1)

    start=Label(wind,text="Time start",width=20,font="KdamThmorPro 11 bold",bg="White",fg="Black").pack(pady=3,padx=2, ipady=3,ipadx=1)
    
    countdown()         #calling timer
    stop=Label(wind,text="time stop",width=20,font="KdamThmorPro 11 bold",bg="White",fg="Black").pack(pady=3,padx=2, ipady=3,ipadx=1)
            
    
    def resultWind():       #now working for taking numbers from user
        win=tkinter.Tk()
        win.title("Remembrance Game")
        win.geometry("1000x600")
        win.configure(bg="#d9ba79")
        
        label1=Label(win, text="The Remembrance Game",
                     bg="#d9ba79",
                     fg="Black",
                     font="KdamThmorPro 45 ",
                     justify="center").pack(ipady=30,ipadx=10)
        
        lr=Label(win,text="DID YOU REMEMBER???",width=20,font="KdamThmorPro 25",bg="White",fg="Black").pack(pady=3,padx=10, ipady=1,ipadx=3)

        Label(win, text="What are the numbers? ",width=30,font="KdamThmorPro 30 bold",bg="#d9ba79",fg="Black").pack(padx=20,pady=10, ipady=1,ipadx=3)
        a=Entry(win, width=30)
        a.pack(pady=3,padx=10, ipady=5,ipadx=3)

        def Calculating():          #here the main work perform
            compStk=computerStack   #computerStack
            userStk=a.get()         #user Numbers
            inn=len(userStk)
            print("length of user string",inn)
            
            if inn!=5:              #check if length is greater then 5 then turn automatically wrong entry
                print("wrong")
                Label(win, text="You Loose",width=30,font="Broadway 45 bold",bg="#d9ba79",fg="Red").pack(padx=20,pady=15, ipady=1,ipadx=3)
                tryAgain=Button(win,text="Try Again",font="KdamThmorPro 20 bold",bg="White",fg="Black", command=win.destroy).pack(side=RIGHT,padx=5,pady=10, ipady=5,ipadx=20)
                return
            
            unumStk=[]              #userStack
            for l in range(5):
                unumStk.append(int(userStk[l]))
            print(unumStk)
            
            for x in range(5):
                if compStk.pop() != unumStk.pop():       #poping from both stack and compare
                    #print(x)
                    print("Wrong")
                    Label(win, text="You Loose",width=30,font="Broadway 45 bold",bg="#d9ba79",fg="Red").pack(padx=20,pady=15, ipady=1,ipadx=3)
                    tryAgain=Button(win,text="Try Again",font="KdamThmorPro 20 bold",bg="White",fg="Black", command=win.destroy).pack(side=RIGHT,padx=5,pady=10, ipady=5,ipadx=20)

                    #return "Wrong"
                    return
                
            Label(win, text="YOU WON!",width=30,font="Broadway 45 bold",bg="#d9ba79",fg="Blue").pack(padx=20,pady=15, ipady=1,ipadx=3)
            Next=Button(win,text="Next",font="KdamThmorPro 20 bold",bg="White",fg="Black", command=win.destroy).pack(side=RIGHT,padx=5,pady=10, ipady=5,ipadx=20)

            return 
                
                
 
        
        
        Button(win, text="Confirm", command=Calculating).pack()

        print("I'm Result")

       
        #exit button
        exitButton=Button(win,text="Exit",font="KdamThmorPro 20 bold",bg="White",fg="Black", command=win.destroy).pack(side=LEFT,padx=5,pady=10, ipady=5,ipadx=20)



        win.mainloop()


    #Call to operate result 
    resultWind()
    wind.mainloop()
        
def mWindow():          #starts from here
    window=tkinter.Tk()
    backg=PhotoImage(file="cover.png")

    window.title("Remembrance Game")
    window.geometry("1000x600")
    myBackG=Label(window,image=backg).place(x=0,y=0, relwidth=1, relheight=1)

    label1=Label(window, text="THE   REMEMBRANCE   GAME",
                 bg="#d9ba79",
                 fg="Black",
                 font="KdamThmorPro 40 bold",
                 justify="center").pack(pady=80)


    #button
    myFrame=Frame(window).pack(padx=100)
    #1
    insButton=Button(myFrame,text="Instructions",
                        font="KdamThmorPro 25 bold",bg="#d9ba79", command=Instructions).pack(pady=50,ipady=20,ipadx=30)
    #2
    startButton=Button(myFrame,text="Start",
                    font="KdamThmorPro 25 bold",bg="#d9ba79", command=startGame).pack(side=RIGHT,padx=(0,100),ipady=20,ipadx=30)
    #3
    exitButton=Button(myFrame,text="Exit",font="KdamThmorPro 25 bold",bg="#d9ba79", command=window.destroy).pack(side=LEFT,padx=(100,0), ipady=20,ipadx=30)

    window.mainloop()


     

if __name__=="__main__":
    mWindow()
