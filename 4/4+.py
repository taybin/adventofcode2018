import re

with open('input2.txt') as f:
    lines = f.readlines()

guards = {}

guard_id = re.compile('\[.+\] Guard #(\d+) begins shift')
time = re.compile('\[.+ \d\d:(.+)\]')
guard = None
fell_asleep = 0
woke_up = 0
for line in lines:
    if 'begins shift' in line:
        m = guard_id.match(line)
        guard = m.group(1)
        if guard not in guards:
            guards[guard] = [0] * 60
        fell_asleep = 0
        woke_up = 0
    elif 'falls asleep' in line:
        m = time.match(line)
        fell_asleep = int(m.group(1))
    elif 'wakes up' in line:
        m = time.match(line)
        woke_up = int(m.group(1))
        for i in range(fell_asleep, woke_up):
            guards[guard][i] += 1

highest_guard = 0
highest_value = 0
highest_min = 0
for guard in guards:
    for i in range(60):
        if guards[guard][i] > highest_value:
            highest_min = i
            highest_value = guards[guard][i]
            highest_guard = guard
print(highest_guard, highest_min, int(highest_guard) * highest_min)

