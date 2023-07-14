# Opens file of inputs and creates a list of ints
    #s.strip() gets rid of white spaces

with open("Day_1_Input", 'r') as input:
    puzzle_input = [int(s.strip()) for s in input] 

def launch_fuel(puzzle_input: int):
    fuel: int = 0
    for mass in puzzle_input:
        fuel += (mass // 3) - 2  # // -> Divides and rounds down
        fuel_remain = fuel
        while fuel_remain > 0:
            fuel_remain = (fuel_remain // 3) - 2
            fuel += fuel_remain
    print(fuel) # Prints total fuel needed for launch
    
launch_fuel(puzzle_input)