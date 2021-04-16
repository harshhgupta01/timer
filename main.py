import time


def countdown(t):
    while t:
        # divide the time into minutes and seconds
        mins, secs = divmod(t, 60)
        # define the format of the timer
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # end="\r" is used to replace the previous value with the new value
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Way to go!")


t = int(input('Enter the time in seconds: '))

countdown(t)
