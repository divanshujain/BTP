from pygame import mixer
import random
import time

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = _GetchUnix()

Test = [(1,6),(11,7),(12,12),(2,5)]
D1 = [(4,1),(5,8),(9,12),(1,1),(5,2)]
D2 = [(3,5),(6,8),(11,9),(4,4),(12,10)]
D3 = [(1,2),(4,5),(8,7),(11,10),(13,13)]

def startTest(File, D):
    if D==0:
        d = Test
    elif D==1:
        d = D1
    elif D==2:
        d = D2
    elif D==3:
        d = D3
    print(D)
    for a in d:

        base = a[0]
        change = a[1]
        if change>base:
            ans = "Up"
        elif change<base:
            ans = "Down"
        else:
            ans = "Same"
        print("Press Enter to move to next set\n")
        key = ord(getch())
        if key == 27: #ESC
            break
        elif key == 13: #Enter
            mixer.init()
            mixer.music.load('./Sounds/testsound'+str(base)+'.ogg')
            mixer.music.play()

            while mixer.music.get_busy():
                continue

            for i in range(3):
                print(i+1)
                time.sleep(1)

            mixer.music.load('./Sounds/testsound'+str(change)+'.ogg')
            mixer.music.play()

            key = ord(getch())
            if key == 27: #ESC
                mixer.music.stop()
            elif key == 52: #Down arrow
                a = "Down"
            elif key == 54: #Up arrow
                a = "Up"
            elif key == 53:
                a = "Same"

            if a == ans:
                print("Correct")
                File.write("Correct\n")
            else:
                print("Wrong")
                print(ans)
                File.write("Wrong Correct:"+ans+" Inputted:"+a+"\n")
    return

Name = raw_input("Enter name : ")
Age = input("Enter Age : ")
Gender = raw_input("Gender (M/F/NB) : ")
Med = raw_input("Any hearing disablities : ")
Train = raw_input("Musical training (None/Mod/Adv) : ")
Fam = raw_input("Family members with musical training (Y/N) : ")
f = open(Name+'.txt',"w+")
f.write("Age : "+str(Age)+"\n")
f.write("Gender : "+Gender+"\n")
f.write("Medical Conditions : "+Med+"\n")
f.write("Musical Training : "+Train+"\n")
f.write("Family BG : "+Fam+"\n")

for d in range(0,4):
    print("Press Enter to start Test Or Escape to Exit\n")
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        f.write(str(d)+'\n')
        startTest(f, d)

f.close()
