#!/usr/bin/env python3

from input import input, test_input

def move_waypoint(waypoint, waypoint_adj):
    return (waypoint[0] + waypoint_adj[0], waypoint[1] + waypoint_adj[1])

def rotate_waypoint(waypoint, clockwise_degree):
    if (clockwise_degree % 90) != 0:
        raise Exception(f"Invalid rotation degree: {clockwise_degree}")

    quaters = clockwise_degree / 90
    quaters = int(quaters % 4)
    for _ in range(quaters):
        waypoint = (-waypoint[1], waypoint[0])

    return waypoint

def move_forward(waypoint, dist, multiplyer):
    return (dist[0] + waypoint[0] * multiplyer, dist[1] + waypoint[1] * multiplyer) 

def solution(input):
    waypoint = (1, 10) # (north, east)
    dist = (0, 0)
    print("Initial condition")
    print(f"waypoint: {waypoint}")
    print(f"dist: {dist}")
    print("------------------------------")
    for instruction in input:
        action = instruction[0]
        magnitude = int(instruction[1:])
        if (action == "N"):
           waypoint = move_waypoint(waypoint, (magnitude, 0)) 
        elif (action == "E"):
           waypoint = move_waypoint(waypoint, (0, magnitude)) 
        elif (action == "S"):
           waypoint = move_waypoint(waypoint, (-magnitude, 0)) 
        elif (action == "W"):
           waypoint = move_waypoint(waypoint, (0, -magnitude)) 
        elif (action == "L"):
            waypoint = rotate_waypoint(waypoint, -magnitude) # clockwise is positive
        elif (action == "R"):
            waypoint = rotate_waypoint(waypoint, magnitude)
        elif (action == "F"):
            dist = move_forward(waypoint, dist,  magnitude)
        else:
            raise Exception(f"Invalid action {action} in instruction")

        print(instruction)
        print(f"waypoint: {waypoint}")
        print(f"dist: {dist}")
        print("------------------------------")

    return abs(dist[0]) + abs(dist[1])

if __name__ == "__main__":
    assert(solution(test_input) == 286)
    print(solution(input))
