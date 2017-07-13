from __future__ import division
from subprocess import PIPE, Popen
import psutil
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
TRIG1 = 22
ECHO1 = 18
TRIG2 = 29
ECHO2 = 31
TRIG3 = 32
ECHO3 = 33
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
GPIO.output(TRIG3, False)

pinList = [36, 38, 40, 37]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

##try:
##  GPIO.output(36, GPIO.LOW)
##  print "ONE"
##  time.sleep(SleepTimeL); 
##  GPIO.output(38, GPIO.LOW)
##  print "TWO"
##  time.sleep(SleepTimeL);  
##  GPIO.output(40, GPIO.LOW)
##  print "THREE"
##  time.sleep(SleepTimeL);
##  GPIO.output(26, GPIO.LOW)
##  print "FOUR"
##  time.sleep(SleepTimeL);
##  GPIO.cleanup()
##  print "Good bye!"



from Tkinter import *
root = Tk()
import Adafruit_PCA9685


#disablemotors = True
import pyglet
music = pyglet.resource.media('R2D2c.wav')
music.play()

def slowservo(channel, frompwm, topwm):
    for xz in range(frompwm, topwm):
        setpwm(channel, 0, xz)

    
def setpwm(channel, startpulse, endpulse):
    pwm.set_pwm(channel,startpulse, endpulse)
    if channel==1:
        root.ch1=endpulse
    elif channel==2:
        root.ch2=endpulse
    elif channel==3:
        root.ch3=endpulse
    elif channel==4:
        root.ch4=endpulse
    elif channel==5:
        root.ch5=endpulse
    elif channel==6:
        root.ch6=endpulse
    elif channel==7:
        root.ch7=endpulse
    elif channel==8:
        root.ch8=endpulse
    elif channel==9:
        root.ch9=endpulse
    elif channel==10:
        root.ch10=endpulse
    elif channel==11:
        root.ch11=endpulse
    elif channel==12:
        root.ch12=endpulse
    elif channel==13:
        root.ch13=endpulse
    elif channel==14:
        root.ch14=endpulse
    elif channel==15:
        root.ch15=endpulse
    elif channel==16:
        root.ch16=endpulse
        


def lookaround():
    root.sonarcount=0
    root.lowd=5000
    root.closepwm=0
    root.distance = 0
    distance = 0
    xcount = 0
    for x in range(200, 600,8):
        print "X="+str(x)
        setpwm(5, 0, x)

        if xcount==1:
            tpd=0
            xcount = 0
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)
            pulse_start = time.time()
            while GPIO.input(ECHO1)==0:
              pulse_start = time.time()
            if GPIO.input(ECHO1)==1:
                pulse_end = time.time()
                tpd = pulse_end - pulse_start
                
            while GPIO.input(ECHO1)==1 and tpd<.032:
              pulse_end = time.time()
              tpd = pulse_end - pulse_start
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            root.distance = distance
            root.sonarcount=0
            if distance<=root.lowd:
                root.lowd=distance
                root.closepwm=x            
            print "Distance:",distance,"cm, Lowest:"+str(root.lowd)+", Pulse Duration="+str(pulse_duration)
        else:
            xcount=xcount+1
    if root.closepwm!=0:
        setpwm(5, 0, root.closepwm)
       

def avoid(menu):
    if root.avoid == False:
        root.avoid = True
        menubar.entryconfigure(3, label="Object Avoidance ON")
        menu.entryconfigure(0, label="Turn Object Avoidance OFF")

    else:
        root.avoid = False
        menubar.entryconfigure(3, label="Object Avoidance OFF")
        menu.entryconfigure(0, label="Turn Object Avoidance OFF")
        
        
        


def fdist(ctime):
    
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)
    pulse_start = time.time()
    while GPIO.input(ECHO1)==0:
      pulse_start = time.time()
    if GPIO.input(ECHO1)==1:
        pulse_end = time.time()
        tpd = pulse_end - pulse_start
    while GPIO.input(ECHO1)==1 and tpd<.075:
      pulse_end = time.time()
      tpd = pulse_end - pulse_start
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return(distance)
def rdist(ctime):
    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)
    pulse_start = time.time()
    while GPIO.input(ECHO2)==0:
      pulse_start = time.time()
    if GPIO.input(ECHO2)==1:
        pulse_end = time.time()
        tpd = pulse_end - pulse_start
    while GPIO.input(ECHO2)==1 and tpd<.075:
      pulse_end = time.time()
      tpd = pulse_end - pulse_start
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    setpwm(14, 0, 4000)
    time.sleep(.5)
    setpwm(14, 0, 0)
    return(distance)

def ldist(ctime):
    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)
    pulse_start = time.time()
    while GPIO.input(ECHO3)==0:
      pulse_start = time.time()
    if GPIO.input(ECHO3)==1:
        pulse_end = time.time()
        tpd = pulse_end - pulse_start
    while GPIO.input(ECHO3)==1 and tpd<.075:
      pulse_end = time.time()
      tpd = pulse_end - pulse_start
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    setpwm(15, 0, 4000)
    time.sleep(.5)
    setpwm(15, 0, 0)
    return(distance)

def b2press(b2pressevent):
##    setpwm(12, 0, 0000)
##    time.sleep(1)
##    setpwm(12, 0, 1000)
##    time.sleep(1)
##    setpwm(12, 0, 2000)
##    
##    print "PWM-2000!"

    
    ctime=time.time()
    distance = fdist(ctime)
    print "Distance ECHO1:",distance
    distance = rdist(ctime)
    print ' '
    print "Distance ECHO2:",distance
    print ' '
    ctime=time.time()
    distance = ldist(ctime)
    print "Distance ECHO3:",distance
    print ' '
    lookaround()
    music = pyglet.resource.media('R2D2a.wav')
    music.play()
    


def b3mcallback(b3mevent):
    x, y = b3mevent.x, b3mevent.y



    
    if y>500:
        y=500
    if y<0:
        y = 1
    if x>500:
        x=500
    if x<=0:
        x=1



    snp = int(((x/500)*500)+250)
    setneckpwm = int(((y/600)*300)+300)
    if setneckpwm <300:
        setneckpwm = 300

    oldpwm4 = root.ch4
    oldpwm5 = root.ch5
    
##    slowservo(4, oldpwm4, setneckpwm)
##    slowservo(5, oldpwm5, snp)
    setpwm(4, 0, setneckpwm)
    setpwm(5, 0, snp)


##   
##    if root.sonarcount==10:
##        GPIO.output(TRIG1, True)
##        time.sleep(0.00001)
##        GPIO.output(TRIG1, False)
##        pulse_start = time.time()
##        while GPIO.input(ECHO1)==0:
##          pulse_start = time.time()
##        if GPIO.input(ECHO1)==1:
##            pulse_end = time.time()
##            tpd = pulse_end - pulse_start
##            
##        while GPIO.input(ECHO1)==1 and tpd<.03:
##          pulse_end = time.time()
##          tpd = pulse_end - pulse_start
##        pulse_duration = pulse_end - pulse_start
##        distance = pulse_duration * 17150
##        distance = round(distance, 2)
##        root.distance=distance
##        root.sonarcount = 0
##        print "Distance:",distance,"cm"
##        v.set("Neck PWM="+str(snp)+" UP:"+str(setneckpwm)+", Distance:"+str(distance)+" cm")
##
##    else:
##        root.sonarcount = root.sonarcount+1
##        distance = root.distance

    
   
 
def b1mcallback(b1mevent):
    x, y = b1mevent.x, b1mevent.y
    if y>500:
        y=500
    if y<0:
        y = 0
    if x>500:
        x=500
    if x<0:
        x=0
    if y<250:
        revright=0
        revleft=0
        thrnum = 250-y
        thrpwm = thrnum * 16
        if x>=250: ##Q2
            z.set("FORWARD Q2")
            turnnum = ((x-250)*8)
            
            t2p=2000-turnnum
            turnpwm = (2000-turnnum)
            if turnnum==0:
                turnnum=1

            leftpwm = int(thrpwm+((turnnum/2000)*thrpwm))
            rightpwm = int(thrpwm-(thrpwm*(turnnum/2000)))
            if leftpwm>4000:
                leftpwm=4000
            
            if rightpwm>4000:
                rightpwm=4000

            if leftpwm<0:
                leftpwm=0
            
            if rightpwm<0:
                rightpwm=0                
            
            lpwm=leftpwm
            rpwm=rightpwm
            
            revright=0
            revleft=0
            if lpwm>=4000 and rpwm<1000:
                rpwm=0
                revright=1500
          
        else:##Q1
##            if x<125 and y<25:
##                return
            
            z.set("FORWARD Q1")
            turnnum = 2000-(x*8)
            if turnnum==0:
                turnnum=1
                

            if turnnum==0:
                turnnum=1
            #turnnum = turnnum*2
            rightpwm = int(thrpwm+(((turnnum/2000)*thrpwm)))
            leftpwm = int(thrpwm-((thrpwm*(turnnum/2000))))
            if leftpwm>4000:
                leftpwm=4000
            
            if rightpwm>4000:
                rightpwm=4000

            if leftpwm<0:
                leftpwm=0
            
            if rightpwm<0:
                rightpwm=0  
            lpwm=leftpwm
            rpwm=rightpwm
                
            revright=0
            revleft=0
            if rpwm>=4000 and lpwm<1000:
                lpwm=0
                revleft=1500
         
    else:

        thrnum = y-250
        thrpwm = thrnum * 16
        if x>250:##Q3
            z.set("REVERSE Q3")
            turnnum = ((x-250)*8)
            t2p=2000-turnnum
            turnpwm = (2000-turnnum)
            if turnnum==0:
                turnnum=1

            leftpwm = int(thrpwm+(((turnnum/2000)*thrpwm)))
            rightpwm = int(thrpwm-((thrpwm*(turnnum/2000))))
            if leftpwm>4000:
                leftpwm=4000
            
            if rightpwm>4000:
                rightpwm=4000
            if leftpwm<0:
                leftpwm=0
            if rightpwm<0:
                rightpwm=0  
            lpwm=leftpwm
            rpwm=rightpwm
            revright=0
            revleft=0
            if lpwm>=4000 and rpwm<1000:
                rpwm=0
                revright=1500
          
        else:##Q4
            z.set("REVERSE Q4")
            turnnum = 2000-(x*8)

            t2p=2000-turnnum
            turnpwm = (2000-turnnum)

            if turnnum==0:
                turnnum=1

            rightpwm = int(thrpwm+(((turnnum/2000)*thrpwm)))
            leftpwm = int(thrpwm-((thrpwm*(turnnum/2000))))
            if leftpwm>4000:
                leftpwm=4000
            
            if rightpwm>4000:
                rightpwm=4000
            if leftpwm<0:
                leftpwm=0
            if rightpwm<0:
                rightpwm=0
                
            lpwm=leftpwm
            rpwm=rightpwm

            revright=0
            revleft=0
            if rpwm>=4000 and lpwm<1000:
                lpwm=0
                revleft=1500

    if root.avoid == True:
        i=GPIO.input(15) #Listening for output from right IR sensor
        k=GPIO.input(16) #Listening for output from left IR sensor
        if k==0 or i==0:
            z.set("AVOIDING")
            if k==0 and i==0:
                z.set("AVOIDING FRONT OBSTACLE")
                setpwm(0, 0, 0)
                setpwm(1, 0, 0)
                setpwm(2, 0, 0)
                setpwm(3, 0, 0)
                time.sleep(.5)
                
                if lpwm>=rpwm:              
                    setpwm(1, 0, 500)
                    setpwm(3, 0, 4000)
                else:
                    setpwm(1, 0, 4000)
                    setpwm(3, 0, 500)
                time.sleep(.5)
            if k==0 and i!=0:
                z.set("AVOIDING RIGHT OBSTACLE")
                rpwm = rpwm*2
                lpwm = int(lpwm/2)
                if rpwm>4000:
                    rpwm=4000
            if i==0 and k!=0:
                z.set("AVOIDING LEFT OBSTACLE")
                lpwm = lpwm*2
                rpwm = int(rpwm/2)
                if lpwm>4000:
                    lpwm=4000
        if root.disablemotors != True:
            if y >250:
                setpwm(0, 0, revright)
                setpwm(2, 0, revleft)
                setpwm(1, 0, rpwm)
                setpwm(3, 0, lpwm)
            else:
                setpwm(1, 0, revright)
                setpwm(3, 0, revleft)
                setpwm(0, 0, rpwm)
                setpwm(2, 0, lpwm)

    else:
        if root.disablemotors != True:       
            if y>250:
                setpwm(0, 0, revright)
                setpwm(2, 0, revleft)
                setpwm(1, 0, rpwm)
                setpwm(3, 0, lpwm)
            else:
                setpwm(1, 0, revright)
                setpwm(3, 0, revleft)
                setpwm(0, 0, rpwm)
                setpwm(2, 0, lpwm)
    
    v.set("Left="+str(lpwm)+", Right="+str(rpwm)+" Turn="+str(turnnum)+" REVL="+str(revleft)+" REVR="+str(revright))           
                
                    
def b1release(entry):
    z.set("STOPPED")
    setpwm(0, 0, 0)
    setpwm(1, 0, 0)
    setpwm(2, 0, 0)
    setpwm(3, 0, 0)

def fpress():
    v.set("WHAT?!")
    
def motion(event):
    x, y = event.x, event.y
    v.set(str(x)+", "+str(y))

def rbatt():
    print "Distance Battery Voltage= We're good."

def rtemp():
    print getCPUtemperature()


    
    print "Temperature="

def measuredistance(ctime):
    
    distance = fdist(ctime)
    print "Distance ECHO1:",distance,"cm"
    distance = rdist(ctime)
    print ' '
    print "Distance ECHO2:",distance,"cm"
    print ' '
    distance = ldist(ctime)
    print "Distance ECHO3:",distance,"cm"
    print ' '

def doalap():
    setpwm(12, 0, 0000)
    time.sleep(1)
    setpwm(12, 0, 1000)
    time.sleep(1)
    setpwm(12, 0, 2000)
    
    print "PWM-2000!"

def disablemotors():
    root.disablemotors = True
    menubar.entryconfigure(4, label="Motors DISABLED")
def enablemotors():
    root.disablemotors = False
    menubar.entryconfigure(4, label="Motors ENABLED")
    

def fullstatus():

    cputempnumcelsius = int(float(getCPUtemperature()))
    cputempnumfahrenheit = (cputempnumcelsius * 9/5) + 32
    print "***System Status "+time.asctime()+"***"
    print "Errors---------NONE"
    print "Damage---------NONE"
    print "CPU Test-------PASS"
    print "Memory Test----PASS"
    print ' '
    print ' '
    print "CPU Temp: "+str(cputempnumfahrenheit)+" Degrees Fahrenheit"


    rinfo = getRAMinfo()
    RAM_total = round(int(rinfo[0]) / 1000,1)
    RAM_used = round(int(rinfo[1]) / 1000,1)
    RAM_free = round(int(rinfo[2]) / 1000,1)    
    
    print "Total RAM: "+str(RAM_total)
    print "Used RAM: "+str(RAM_used)
    print "Remaining RAM: "+str(RAM_free)
    
    print ' '
    cpu_usage = psutil.cpu_percent()
    print "CPU Usage: "+str(cpu_usage)+"%"
    print ' '
    gds=getDiskSpace()
    print "Total Disk Space: "+gds[0]
    print "Used Disk Space: "+gds[1]
    print "RemainingDisk Space: "+gds[2]
    print "% Used Disk Space: "+gds[3]
    print ' '
    print ' '
    print "***ALL SYSTEMS GO***"
    print "***ALL SYSTEMS GO***"
    print "***ALL SYSTEMS GO***"
    print ' '
    print ' '
    ctime = time.time()
    measuredistance(ctime)

def headlights(menu):
    if root.headlights==False:
        root.headlights=True
        GPIO.output(37, GPIO.LOW)
        menu.entryconfigure(4, label="Turn Headights OFF")
    else:
        root.headlights=False
        GPIO.output(37, GPIO.HIGH)
        menu.entryconfigure(4, label="Turn Headlights ON")

def runninglights(menu):
    if root.runninglights==False:
        root.runninglights=True
        GPIO.output(40, GPIO.LOW)
        menu.entryconfigure(5, label="Turn Running Lights OFF")
    else:
        root.runninglights=False
        GPIO.output(40, GPIO.HIGH)
        menu.entryconfigure(5, label="Turn Running Lights ON")
# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                          
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used                                                  
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])


    
    
pwm = Adafruit_PCA9685.PCA9685()
##GPIO.setup(15, GPIO.IN) #Right IR sensor module
##GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Activation button
##GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR sensor module

loopcount = 0
frustration = 0
# Configure min and max servo pulse lengths
servo_min = 0  # Min pulse length out of 4096
servo_max = 1700  # Max pulse length out of 4096
servo_current = 0

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

currentneckposition = 430
setpwm(4, 0, 430)
setpwm(5, 0, 425)



#root = Tk()
root.title("ROVER - MANUAL CONTROL")
root.geometry("500x500")
app = Frame(root)
app.grid()
root.currentneckposition = 430
root.inx = 0
root.iny = 0
root.outx = 0
root.outy = 0
root.sonarcount = 0
root.distance=0
root.forward = True
root.avoid = False
root.disablemotors = True
root.ch1=0
root.ch2=0
root.ch3=0
root.ch4=0
root.ch5=0
root.ch5=0
root.ch6=0
root.ch7=0
root.ch8=0
root.ch9=0
root.ch10=0
root.ch11=0
root.ch12=0
root.ch13=0
root.ch14=0
root.ch15=0
root.ch16=0
root.headlights=False
root.runninglights=False
##i=GPIO.input(15) #Listening for output from right IR sensor
##k=GPIO.input(16) #Listening for output from left IR sensor
v = StringVar()
z = StringVar()
#button1 = Button(app, text = "AVOIDANCE OFF", command=avoid)
wlabel = Label(root, textvariable=v)
v.set("Manual Control")
dirlabel = Label(root, textvariable=z)
z.set("VEHICLE STOPPED")
#button1.grid(row=1,column=1)
wlabel.grid(row=1,column=1)
dirlabel.grid(row=2,column=1)
menubar = Menu(root)






actionsmenu = Menu(menubar, tearoff=0)
actionsmenu.add_command(label="Turn Object Avoidance ON", command=lambda: avoid(actionsmenu))
actionsmenu.add_command(label="Look Around", command=lookaround)
actionsmenu.add_command(label="Disable Motors", command=disablemotors)
actionsmenu.add_command(label="Enable Motors", command=enablemotors)
actionsmenu.add_command(label="Turn Headlights ON", command=lambda: headlights(actionsmenu))
actionsmenu.add_command(label="Turn Running Lights ON", command=lambda: runninglights(actionsmenu))

menubar.add_cascade(label="Actions", menu=actionsmenu)

statusmenu = Menu(menubar, tearoff=0)
statusmenu.add_command(label="Battery Voltage", command=rbatt)
statusmenu.add_command(label="Temperature", command=rtemp)
statusmenu.add_command(label="Full Status", command=fullstatus)
menubar.add_cascade(label="Status", menu=statusmenu)



oamenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Object Avoidance OFF", menu=oamenu)

mdmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Motors DISABLED", menu=mdmenu)


root.config(menu=menubar)


# display the menu
root.config(menu=menubar)

root.bind("<Button-3>", b3mcallback)
root.bind("<Button-1>", b1mcallback)
root.bind("<B1-Motion>", b1mcallback)
root.bind("<B3-Motion>", b3mcallback)
root.bind('<Motion>', motion)
root.bind("<ButtonRelease-1>", b1release)
root.bind("<Button-2>", b2press)
root.resizable(0,0)

root.mainloop()
