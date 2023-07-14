# Opens file of inputs and creates a list of ints
    #s.strip() gets rid of white spaces

with open("Day_1_Input", 'r') as input:
    puzzle_input = [int(s.strip()) for s in input] 

def launch_fuel(puzzle_input: int):
    fuel: int = 0
    for mass in puzzle_input:
        fuel += fuel_calc(mass) - mass
    print(fuel) # Prints total fuel needed

def fuel_calc(mass: int):
    new_mass = (mass // 3) - 2
    if new_mass < 0:
        return mass # Return mass once new_mass is 0 or below
    else:
        return fuel_calc(new_mass) + mass # Returns added mass until there is no mass left

launch_fuel(puzzle_input)