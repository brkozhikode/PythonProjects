from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set in 24 hour format:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]

if int(alarm_hour) < 0 or int(alarm_hour) > 24 or int(alarm_minute) < 0 or int(alarm_minute) > 59 or int(alarm_seconds) < 0 or int(alarm_seconds) > 59:
    print("invalid input")
    exit()

print("Setting up alarm for.." + alarm_time)
while True:
    now = datetime.now()
    #print(now)
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    #print(alarm_hour+current_hour)
    if(alarm_hour==current_hour):
        #print(alarm_minute)
        if(alarm_minute==current_minute):
            #print(alarm_seconds)
            if(alarm_seconds==current_seconds):
                print("Wake Up!")
                playsound('resources/alarm.mp3')
                break