import time

def countdown(minutes, seconds):
    # Convert minutes and seconds to total seconds
    t = minutes * 60 + seconds

    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer completed!")

# Set the countdown time (in minutes and seconds)
minutes = 1  # 1 minute
seconds = 30  # 30 seconds
countdown(minutes, seconds)
