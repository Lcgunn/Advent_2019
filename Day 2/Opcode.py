

with open("Day_2_Input", 'r') as input:
    data = input.read()

puzzle_input = [int(i) for i in data.split(',')]    # Creates an array of ints based off of the list: data. Creates a new array element when it sees a ','



print(puzzle_input)