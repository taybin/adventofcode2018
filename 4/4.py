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
        print(guard)
    elif 'falls asleep' in line:
        m = time.match(line)
        fell_asleep = int(m.group(1))
        print(fell_asleep)
    elif 'wakes up' in line:
        m = time.match(line)
        woke_up = int(m.group(1))
        print(woke_up)
        print(guards[guard])
        for i in range(fell_asleep, woke_up):
            guards[guard][i] += 1

for guard in guards:
    highest_min = 0
    highest_value = 0
    for i in range(60):
        if guards[guard][i] > highest_value:
            highest_min = i
            highest_value = guards[guard][i]
    print(guard, sum(guards[guard]), highest_min)
    print(guards[guard])


