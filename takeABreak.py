import time
import webbrowser

total_breaks = 4
break_count = 0

print("This program started on " +time.ctime())
while(break_count < total_breaks):
    if break_count > 0:
        time.sleep(300)
    if break_count == 0:
        webbrowser.open("https://www.youtube.com/watch?v=ZzKzp76dElM")
    if break_count == 1:
        webbrowser.open("https://www.youtube.com/watch?v=JpZ74bJcX0U")
    if break_count == 2:
        webbrowser.open("https://www.youtube.com/watch?v=BIQK4-9YFW0")
    if break_count == 3:
        webbrowser.open("https://www.youtube.com/watch?v=GwrnjtW-rfk")
        
    break_count = break_count + 1
