# this was solved with much help from the adventofcode 
# subreddit.  I did switch to using deques, but was
# performing some expensive, unnecessary operations

import collections
import itertools
import re

with open('input.txt') as f:
    line = f.read()

reg = '(\d+) players; last marble is worth (\d+) points'

m = re.match(reg, line)
player_count = int(m.group(1))
marble_count = int(m.group(2)) * 100

players = {str(k):0 for k in range(player_count)}
player_cycle = itertools.cycle(players)

marbles = collections.deque([0])
current = 0

#print('[0]  (0)')
length = 1
for i in range(1, marble_count + 1):
#    print(i, marble_count + 1)
    player = next(player_cycle)
    if i % 23 != 0:
        current = i
        marbles.rotate(-1)
        marbles.append(current)
    else:
        marbles.rotate(7)
        players[player] += marbles.pop() + i
        marbles.rotate(-1)
    #print('[{i}]   {marbles}'.format(i=i, marbles='  '.join([str(m) if m != i else '('+str(m)+')' for m in marbles])))
print(max(players.values()))
