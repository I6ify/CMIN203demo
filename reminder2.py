import time
import winsound

count = 5

while count >= 1:
    winsound.PlaySound("Attendance.wav", winsound.SND_ASYNC)
    print ("Your attendance is due in " + str(count), "minutes!")
    time.sleep(5)
    count -= 1

while count == 0:
    winsound.PlaySound("Attendance.wav", winsound.SND_ASYNC)
    print ("Your attendance is due!")
    break
