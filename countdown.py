# %%
import datetime
import time


def countdown(time_seconds):
    while time_seconds > 0:
        # show_time = str(datetime.timedelta(seconds=time_seconds))
        # print(show_time)
        minute, second = divmod(time_seconds, 60)
        print("{:02d}:{:02d}".format(minute, second))
        time.sleep(1)
        time_seconds -= 1
    print("Time is up!")
    return None


# %%
countdown(100)

# %%
