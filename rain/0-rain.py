#!/usr/bin/python3
def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    total_water = 0

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            total_water += max(0, left_max - walls[left])
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            total_water += max(0, right_max - walls[right])

    return total_water

