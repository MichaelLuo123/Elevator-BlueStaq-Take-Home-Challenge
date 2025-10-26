class Elevator:
    def __init__(self, lowest_floor=1, highest_floor=10, start_floor=1, door_open_time=3):
        # Set the bounds of the building
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = start_floor # Where the elevator starts

        self.direction = 0   # 1 = going up, -1 = going down, 0 = idle
        self.state = "IDLE"  # could be "IDLE", "MOVING", or "DOORS_OPEN"

        self.up_queue = set()   # Floors requested in each direction
        self.down_queue = set() # Floors requested in each direction

        self.door_timer = 0     # Time remaining for doors to stay open
        self.door_open_time = door_open_time # Time doors stay open

    def request(self, floor):
        """Handle a floor request from either inside or outside the elevator."""
        if floor < self.lowest_floor or floor > self.highest_floor:
            print(f"Ignoring invalid floor request: {floor}")
            return

        if floor > self.current_floor:
            self.up_queue.add(floor)
        elif floor < self.current_floor:
            self.down_queue.add(floor)
        else:
            self.state = "DOORS_OPEN"
            self.door_timer = self.door_open_time

        if self.state == "IDLE":
            if self.up_queue:
                self.direction = 1
            elif self.down_queue:
                self.direction = -1
            self.state = "MOVING"

    def tick(self):
        """Advance the simulation by one step."""
        if self.state == "DOORS_OPEN":
            self.door_timer -= 1
            if self.door_timer <= 0:
                self._close_doors()
            return

        if self.state == "MOVING":
            self.current_floor += self.direction

            # stop if this floor was requested
            if self.direction == 1 and self.current_floor in self.up_queue:
                self.up_queue.remove(self.current_floor)
                self._open_doors()
            elif self.direction == -1 and self.current_floor in self.down_queue:
                self.down_queue.remove(self.current_floor)
                self._open_doors()

            # adjust direction if we hit limits or run out of stops
            if self.current_floor == self.highest_floor:
                self.direction = -1 if self.down_queue else 0
            elif self.current_floor == self.lowest_floor:
                self.direction = 1 if self.up_queue else 0

            if not self.up_queue and not self.down_queue:
                if self.state != "DOORS_OPEN":
                    self.state = "IDLE"
                    self.direction = 0

    def _open_doors(self):
        self.state = "DOORS_OPEN"
        self.door_timer = self.door_open_time

    def _close_doors(self):
        if self.up_queue or self.down_queue:
            self.state = "MOVING"
            # keep direction if possible
            if self.direction == 0:
                self.direction = 1 if self.up_queue else -1
        else:
            self.state = "IDLE"
            self.direction = 0

    def __repr__(self):
        return (f"[Floor {self.current_floor}] "
                f"State={self.state}, Dir={self.direction}, "
                f"Up={sorted(self.up_queue)}, Down={sorted(self.down_queue)}")


if __name__ == "__main__":
    lift = Elevator()

    lift.request(3)
    lift.request(7)

    for t in range(20):
        print(f"Tick {t}: {lift}")
        if t == 5:
            print("Passenger pressed floor 9.")
            lift.request(9)
        lift.tick()
