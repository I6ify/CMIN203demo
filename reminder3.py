import time
import winsound

count = 5

while input("Have you completed your attendance? (Y/N) ").upper() == "N":
        winsound.PlaySound("Attendance.wav", winsound.SND_ASYNC)
        print ("Your attendance is due in " + str(count), "minutes!")
        time.sleep(5)
        count -= 1
else:
    print("Thank you for submitting your attendance!")
    
