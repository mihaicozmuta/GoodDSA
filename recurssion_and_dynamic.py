# recursion problems which will be afterwards improved with dynamic programming approaches

# Problem 1: given N stairs with the posibility to climb 1, 2 or 3 at a time, return the number of possible ways


def get_ways(stairs) -> int:
    if stairs == 0 or stairs == 1:
        return 1
    if stairs == 2:
        return 2
    return get_ways(stairs - 3) + get_ways(stairs - 2) + get_ways(stairs - 1)


# draw the recursion tree and you will see the problem with the above approach. Let's apply memoization


def get_ways_better(stairs) -> int:
    prevs = [0] * (stairs + 1)
    prevs[0] = 1
    prevs[1] = 1
    prevs[2] = 2

    for i in range(3, stairs + 1):
        prevs[i] = prevs[i - 3] + prevs[i - 2] + prevs[i - 1]

    return prevs[stairs]


# a robot is in a maze, at the top left corner. she can move only right or down. if the value is None, then we cannot
# step there. return the robot's way to the right bottom corner





if __name__ == '__main__':
    stairs = 4
    print("There are {} ways of climbing {} stairs".format(get_ways_better(stairs), stairs))
