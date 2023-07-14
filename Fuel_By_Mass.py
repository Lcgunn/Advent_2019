# Opens file of inputs and creates a list of ints
    #s.strip() gets rid of white spaces

with open("Day_1_Input", 'r') as input:
    puzzle_input = [int(s.strip()) for s in input] 

def launch_fuel(puzzle_input: int):
    fuel: int = 0
    for mass in puzzle_input:
        fuel += (mass // 3) - 2
    print(fuel)
    
launch_fuel(puzzle_input)