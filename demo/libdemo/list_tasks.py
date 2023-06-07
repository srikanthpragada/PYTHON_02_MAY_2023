from datetime import *

f = open('tasks.txt', 'rt')
tasks = []
for line in f.readlines():
    # strip newline at the end and then split with ,
    parts = line.strip().split(",")
    task = parts[0]
    try:
        if len(parts) == 2: # enddate is missing
            enddate = datetime.now()
        else:
            enddate = datetime.strptime(parts[2], "%d-%m-%Y")

        stdate = datetime.strptime(parts[1], "%d-%m-%Y")
        days = (enddate - stdate).days
        # add tuple to list
        tasks.append((task, days))
    except:
        pass   # ignore invalid lines

f.close()

for task, days in sorted(tasks, key=lambda t: t[1]):
    print(f"{task:50} {days:3}")
