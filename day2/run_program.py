import sys

OP_SUM = 1
OP_MUL = 2
OP_TERM = 99

OUTPUT_FIRST_CHAR = 19690720

def execute_operation(op, first_term, second_term):
    if op == OP_SUM:
        return first_term + second_term
    elif op == OP_MUL:
        return first_term * second_term

def run_program(line):
    codes = line[:]

    i = 0
    current_op = int(codes[i])
    while current_op != OP_TERM:
        first_term_index = int(codes[i+1])
        second_term_index = int(codes[i+2])
        result_index = int(codes[i+3])

        codes[result_index] = execute_operation(current_op, int(codes[first_term_index]), int(codes[second_term_index]))
        
        i += 4
        current_op = int(codes[i])
    
    return codes

with open("input/input-1.txt", "r") as input_file:
    for line in input_file:
        processed_line = line.split(",")
        processed_line[1] = 12
        processed_line[2] = 2
        
        result_line = run_program(processed_line)

        print("First run completed, result codes string: ")
        print(result_line)
        
        for noun in range(0, 100):
            for verb in range(0, 100):
                processed_line[1] = noun
                processed_line[2] = verb

                result_line = run_program(processed_line)

                if result_line[0] == OUTPUT_FIRST_CHAR:
                    print("Noun: " + str(noun) + ", verb: " + str(verb) + ", run completed, result code strings: ")
                    print(result_line)
                    print("Expected result is: " + str((100 * noun) + verb))

                    sys.exit(0)
        