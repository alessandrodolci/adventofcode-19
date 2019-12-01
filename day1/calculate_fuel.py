sum = 0

def get_module_fuel(mass):
    return (mass // 3) - 2

with open("input/input-1.txt", "r") as input_file:
    for line in input_file:
        mass = int(line)
        fuel_needed = get_module_fuel(mass)
        sum += fuel_needed
        
        additional_fuel = get_module_fuel(fuel_needed)
        while (additional_fuel >= 0):
            sum += additional_fuel
            additional_fuel = get_module_fuel(additional_fuel)

print(sum)
