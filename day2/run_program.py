OP_SUM = 1
OP_MUL = 2
OP_TERM = 99

def execute_operation(op, first_term, second_term):
    if op == OP_SUM:
        return first_term + second_term
    elif op == OP_MUL:
        return first_term * second_term

with open("input/input-1.txt", "r") as input_file:
    for line in input_file:
        codes = line.split(",")
        codes[1] = 12
        codes[2] = 2

        i = 0
        current_op = int(codes[i])
        while current_op != OP_TERM:
            first_term_index = int(codes[i+1])
            second_term_index = int(codes[i+2])
            result_index = int(codes[i+3])

            codes[result_index] = execute_operation(current_op, int(codes[first_term_index]), int(codes[second_term_index]))
            
            i += 4
            current_op = int(codes[i])

        print("Execution completed, result codes string: ")
        print(codes)
