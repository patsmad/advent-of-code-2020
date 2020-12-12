from get_input import get_input

response = get_input(12)

data = response.text.strip().split('\n')

converted_data = [(a[0], int(a[1:])) for a in data]

class Ship:
    def __init__(self, initial_position, initial_direction_index):
        self.current_position = initial_position
        self.directions = ['N', 'E', 'S', 'W']
        self.direction_index = initial_direction_index

    def move(self, instruction, num):
        if instruction == 'N':
            self.current_position = (self.current_position[0], self.current_position[1] + num)
        elif instruction == 'E':
            self.current_position = (self.current_position[0] + num, self.current_position[1])
        elif instruction == 'S':
            self.current_position = (self.current_position[0], self.current_position[1] - num)
        elif instruction == 'W':
            self.current_position = (self.current_position[0] - num, self.current_position[1])
        elif instruction == 'F':
            self.move(self.directions[self.direction_index], num)
        elif instruction == 'L':
            self.direction_index = (self.direction_index - num // 90) % len(self.directions)
        else:
            self.direction_index = (self.direction_index + num // 90) % len(self.directions)

ship = Ship((0, 0), 1)
for instruction in converted_data:
    ship.move(instruction[0], instruction[1])
print(abs(ship.current_position[0]) + abs(ship.current_position[1]))

class WaypointShip:
    def __init__(self, initial_position, waypoint_position):
        self.current_position = initial_position
        self.waypoint_position = waypoint_position
        self.directions = [((0, 1), (1, 1)), ((1, 0), (1, -1)), ((0, 1), (-1, -1)), ((1, 0), (-1, 1))]

    def move(self, instruction, num):
        if instruction == 'N':
            self.waypoint_position = (self.waypoint_position[0], self.waypoint_position[1] + num)
        elif instruction == 'E':
            self.waypoint_position = (self.waypoint_position[0] + num, self.waypoint_position[1])
        elif instruction == 'S':
            self.waypoint_position = (self.waypoint_position[0], self.waypoint_position[1] - num)
        elif instruction == 'W':
            self.waypoint_position = (self.waypoint_position[0] - num, self.waypoint_position[1])
        elif instruction == 'F':
            self.current_position = (self.current_position[0] + self.waypoint_position[0] * num, self.current_position[1] + self.waypoint_position[1] * num)
        else:
            index = (num // 90) * (-1 if instruction == 'L' else 1)
            direction = self.directions[index]
            self.waypoint_position = (self.waypoint_position[direction[0][0]] * direction[1][0], self.waypoint_position[direction[0][1]] * direction[1][1])

ship = WaypointShip((0, 0), (10, 1))
for instruction in converted_data:
    ship.move(instruction[0], instruction[1])
print(abs(ship.current_position[0]) + abs(ship.current_position[1]))