import os
import math

wires = []

UP = "U"
RIGHT = "R"
DOWN = "D"
LEFT = "L"

def vertical_intersect(wires, wire_index, x, y):
    for i in range(len(wires)):
        if i != wire_index and x in wires[i] and y in wires[i][x]:
            return wires[i][x][y] == "-"

def horizontal_intersect(wires, wire_index, x, y):
    for i in range(len(wires)):
        if i != wire_index and x in wires[i] and y in wires[i][x]:
            return wires[i][x][y] == "|"

def add_intersection(intersections, wire_index, x, y, steps_required):
    index = str(x) + "-" + str(y)
    if not index in intersections:
        intersections[index] = {}
    if not wire_index in intersections[index]:
        intersections[index][wire_index] = steps_required

def update_distance(x, y, current_distance):
    x = abs(x)
    y = abs(y)

    distance = x + y
    return distance if distance < current_distance else current_distance

wires = []
wire_index = 0
closest_intersection_distance = math.inf
intersections = {}

with open(os.path.join("input", "input-1.txt"), "r") as input_file:
    for line in input_file:
        wires.append({})
        wires[wire_index][0] = {}
        wires[wire_index][0][0] = "o"

        tokens = line.split(",")
        
        x = 0
        y = 0
        for token in tokens:
            direction = token[0]
            length = int(token[1:])
            
            if direction == UP:
                for i in range(length):
                    y += 1
                    if vertical_intersect(wires, wire_index, x, y):
                        wires[wire_index][x][y] = "x"
                        closest_intersection_distance = update_distance(x, y, closest_intersection_distance)
                    else:
                        wires[wire_index][x][y] = "|"
            elif direction == RIGHT:
                for i in range(length):
                    x += 1
                    if not x in wires[wire_index]:
                        wires[wire_index][x] = {}
                    if horizontal_intersect(wires, wire_index, x, y):
                        wires[wire_index][x][y] = "x"
                        closest_intersection_distance = update_distance(x, y, closest_intersection_distance)
                    else:
                        wires[wire_index][x][y] = "-"
            elif direction == DOWN:
                for i in range(length):
                    y -= 1
                    if vertical_intersect(wires, wire_index, x, y):
                        wires[wire_index][x][y] = "x"
                        closest_intersection_distance = update_distance(x, y, closest_intersection_distance)
                    else:
                        wires[wire_index][x][y] = "|"
            elif direction == LEFT:
                for i in range(length):
                    x -= 1
                    if not x in wires[wire_index]:
                        wires[wire_index][x] = {}
                    if horizontal_intersect(wires, wire_index, x, y):
                        wires[wire_index][x][y] = "x"
                        closest_intersection_distance = update_distance(x, y, closest_intersection_distance)
                    else:
                        wires[wire_index][x][y] = "-"

            if not x in wires[wire_index]:
                wires[wire_index][x] = {}
            wires[wire_index][x][y] = "+"

        wire_index += 1

print("The closest intersection distance from the origin point is " + str(closest_intersection_distance))

wire_index = 0
with open(os.path.join("input", "input-1.txt"), "r") as input_file:
    for line in input_file:
        tokens = line.split(",")

        x = 0
        y = 0
        steps_required = 0

        for token in tokens:
            direction = token[0]
            length = int(token[1:])
            
            if direction == UP:
                for i in range(length):
                    y += 1
                    steps_required += 1
                    if wires[wire_index][x][y] == "x":
                        add_intersection(intersections, wire_index, x, y, steps_required)
                    for j in range(len(wires)):
                        if j != wire_index and x in wires[j] and y in wires[j][x] and wires[j][x][y] == "x":
                            add_intersection(intersections, wire_index, x, y, steps_required)

            elif direction == RIGHT:
                for i in range(length):
                    x += 1
                    steps_required += 1
                    if wires[wire_index][x][y] == "x":
                        add_intersection(intersections, wire_index, x, y, steps_required)
                    for j in range(len(wires)):
                        if j != wire_index and x in wires[j] and y in wires[j][x] and wires[j][x][y] == "x":
                            add_intersection(intersections, wire_index, x, y, steps_required)
                    
            elif direction == DOWN:
                for i in range(length):
                    y -= 1
                    steps_required +=1
                    if wires[wire_index][x][y] == "x":
                        add_intersection(intersections, wire_index, x, y, steps_required)
                    for j in range(len(wires)):
                        if j != wire_index and x in wires[j] and y in wires[j][x] and wires[j][x][y] == "x":
                            add_intersection(intersections, wire_index, x, y, steps_required)
                    
            elif direction == LEFT:
                for i in range(length):
                    x -= 1
                    steps_required += 1
                    if wires[wire_index][x][y] == "x":
                        add_intersection(intersections, wire_index, x, y, steps_required)
                    for j in range(len(wires)):
                        if j != wire_index and x in wires[j] and y in wires[j][x] and wires[j][x][y] == "x":
                            add_intersection(intersections, wire_index, x, y, steps_required)
            
        wire_index += 1

fewest_steps_number = math.inf
intersections_list = list(intersections.values())
for i in range(len(intersections_list)):
    steps = sum(intersections_list[i].values())
    if steps < fewest_steps_number:
        fewest_steps_number = steps

print("The fewest combined steps the wires must take to reach an intersection is " + str(fewest_steps_number))
