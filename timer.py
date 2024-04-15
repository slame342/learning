import time

hours = 0
minutes = 0
seconds = 0

while True:
    # seconds = seconds + 1 вариант записи,увеличения
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0
        if minutes > 59:
            hours += 1
            minutes = 0
            if hours > 23:
                seconds = 0
                minutes = 0
                hours =0
    time.sleep(1)
    print("hours:", hours, "minutes:", minutes, "second:", seconds)
    # print(f"{hours}:{minutes}" + ":" + str(seconds))
    # print(f"{'hours'}:{hours} {'minutes'}:{minutes} {'seconds'}:{seconds}")