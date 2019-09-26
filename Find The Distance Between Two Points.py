def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_left = mpg*fuel_left
    if distance_to_pump <= distance_left:
        return True
    else:
        return False