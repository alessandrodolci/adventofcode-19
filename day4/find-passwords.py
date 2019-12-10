import re
import os

base_pattern = r"^(?=\d{6}$)0*1*2*3*4*5*6*7*8*9*$"
repeat_pattern = r".*(\d)\1{1}.*"
exactly_two_repetition_pattern = r"(?:^|(.)(?!\1))(\d)\2(?!\2)"

base_regex = re.compile(base_pattern)
repeat_regex = re.compile(repeat_pattern)
exactly_two_repetition_regex = re.compile(exactly_two_repetition_pattern)

bounds = []
with open(os.path.join("input", "input-1.txt"), "r") as input_file:
    line = input_file.readline()
    bounds = line.split("-")

passwords = []
for number in range(int(bounds[0]), int(bounds[1])):
    string = str(number)
    if base_regex.search(string) and repeat_regex.search(string) and exactly_two_repetition_regex.search(string):
        passwords.append(string)

print(str(len(passwords)) + " passwords found.")
