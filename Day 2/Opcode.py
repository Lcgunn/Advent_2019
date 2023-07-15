

with open("Day_2_Input", 'r') as input:
    data = input.read()

puzzle_input = [int(i) for i in data.split(',')]    # Creates an array of ints based off of the list: data. Creates a new array element when it sees a ','

current_op: int = 0
index: int = 0

while current_op != 99:     # If opcode == 99 then stop
    current_op = puzzle_input[index]
    # If op code is 1, add the numbers located at the position value of the next two ints and put it in the address of the third next int
    if current_op == 1:
        puzzle_input[puzzle_input[index + 3]] = puzzle_input[puzzle_input[index + 1]] + puzzle_input[puzzle_input[index + 2]]
    else:
        # If op code is 2, multiple the numbers located at the position value of the next two ints and put it in the address of the third next int
        if current_op == 2:
            puzzle_input[puzzle_input[index + 3]] = puzzle_input[puzzle_input[index + 1]] * puzzle_input[puzzle_input[index + 2]]
    
    # Increment index by 4 to get the next opcode
    index += 4
            
print(puzzle_input)
