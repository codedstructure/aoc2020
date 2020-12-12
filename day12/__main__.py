from utils import get_lines


class Navigation:
    def __init__(self, lines):
        self.actions = [(line[0], int(line[1:])) for line in lines]
        # We use a lat-long system where 'north east' is the positive
        # quadrant, and a heading of 0 degrees is due east.
        self.dir = 0  # East
        self.lat = 0
        self.long = 0
        self.wp_lat_offset = 1  # North
        self.wp_long_offset = 10  # East

    def step(self, instruction):
        action, amount = instruction
        if action == 'N':
            self.lat += amount
        elif action == 'S':
            self.lat -= amount
        elif action == 'E':
            self.long += amount
        elif action == 'W':
            self.long -= amount
        elif action == 'L':
            self.dir += amount
        elif action == 'R':
            self.dir -= amount
        elif action == 'F':
            heading = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}[self.dir % 360]
            self.step((heading, amount))

    def navigate(self):
        for act in self.actions:
            self.step(act)

    def waypoint_step(self, instruction):
        action, amount = instruction
        if action == 'N':
            self.wp_lat_offset += amount
        elif action == 'S':
            self.wp_lat_offset -= amount
        elif action == 'E':
            self.wp_long_offset += amount
        elif action == 'W':
            self.wp_long_offset -= amount
        elif action == 'L':
            for cycle in range(amount // 90):
                self.wp_lat_offset, self.wp_long_offset = (
                        self.wp_long_offset, -self.wp_lat_offset)
        elif action == 'R':
            for cycle in range(amount // 90):
                self.wp_lat_offset, self.wp_long_offset = (
                        -self.wp_long_offset, self.wp_lat_offset)
        elif action == 'F':
            self.lat += amount * self.wp_lat_offset
            self.long += amount * self.wp_long_offset

    def waypoint_nav(self):
        for act in self.actions:
            self.waypoint_step(act)

    def manhattan(self):
        return abs(self.lat) + abs(self.long)


def puzzle1():
    lines = get_lines('day12')
    nav = Navigation(lines)
    nav.navigate()
    print(nav.manhattan())


def puzzle2():
    lines = get_lines('day12')
    nav = Navigation(lines)
    nav.waypoint_nav()
    print(nav.manhattan())


if __name__ == '__main__':
    puzzle1()
    puzzle2()
