import datetime as t
import winsound

time=t.datetime.now()
time_m=time.minute
time_h=time.hour
time_start=time_h*60+time_m
#print(time_start)

a=int(input("ideal time minute only >>"))
if a>=60:
    print("Given number minutes in 59 Below")
    print("Try Again ")

time_stop=time_h*60+time_m+a

while(1):
    time_c=t.datetime.now()
    timem_c=time_c.minute
    timeh_c=time_c.hour
    time_current=timeh_c*60+timem_c
    time_show=str(time_c.hour)+':'+str(time_c.minute)+':'+str(time_c.second)
    print(time_show)
    while(time_current==time_stop):
        print("times up pls check ideal time")
        winsound.PlaySound('Welcome1.wav', winsound.SND_FILENAME)   
