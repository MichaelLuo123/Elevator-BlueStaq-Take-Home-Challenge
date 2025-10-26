"""
Elevator Simulator - Backend Challenge

What this is:
This is a simple simulation of an elevator. It moves between floors, handles requests 
from inside or outside the elevator, opens and closes doors for a set amount of time, 
and changes direction when it reaches the top or bottom floors or when there are pending stops.

How to use it:
1. Make an Elevator object, e.g.
       lift = Elevator(lowest_floor=1, highest_floor=10, start_floor=1, door_open_time=3)

2. Add floor requests:
       lift.request(3)   # someone wants to go to floor 3
       lift.request(7)   # someone wants to go to floor 7

3. Run the simulation one step at a time:
       lift.tick()

The elevator will automatically stop at requested floors, open doors for a few ticks, 
then keep moving. You can print the elevator object to see its current floor, 
state, direction, and any floors still in the queue.

Notes / assumptions:
- Elevator moves one floor per tick. 
- Multiple requests are queued and handled in order, no fancy prioritization. 
- Doors stay open for a fixed number of ticks (door_open_time). 
- The elevator only knows the range of floors defined when it was created.

Author: Michael Luo
"""
