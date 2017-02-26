import webbrowser
import time


print ("The program has started on " + time.ctime())
times = 0
while (times<3):
    time.sleep (5)
    webbrowser.open("https://www.youtube.com/watch?v=35gheud5xBo")
    times = times + 1

print ("All done")


