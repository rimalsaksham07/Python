input_string = "Python"
reversed_string = ""

for char in input_string:
    reversed_string =  char + reversed_string 

print(reversed_string)

# Initially, input_string is "Python" and reversed_string is "".
# First iteration: char is 'P', reversed_string becomes 'P'.
# Second iteration: char is 'y', reversed_string becomes 'yP'.
# Third iteration: char is 't', reversed_string becomes 'tyP'.
# Fourth iteration: char is 'h', reversed_string becomes 'htyP'.
# Fifth iteration: char is 'o', reversed_string becomes 'ohtyP'.
# Sixth iteration: char is 'n', reversed_string becomes 'nohtyP'.
