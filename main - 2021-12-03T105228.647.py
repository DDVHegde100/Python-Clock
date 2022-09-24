import time
timerstop = str(input("Do you want to use the Timer or Stopwatch? "))
if(timerstop=="Timer"):
    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1
    
        print("Time is Up! Thanks and please use again 😀")
    time2 = int(input("Enter Seconds To Start Timer: "))
    countdown(time2)
else:
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

