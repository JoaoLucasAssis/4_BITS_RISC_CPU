def write_instructions(output_file_name, output):
    try:
        count = 0

        with open(output_file_name, 'w') as file:
            file.write("v2.0 raw\n")

            for instruction in output:
                file.write(instruction + " ")
                count += 1
            
                if count == 8:
                    count = 0
                    file.write("\n")

        print("Arquivo 'output.txt' criado.")
    except ValueError:
        raise ValueError()

def translate_instruction(opcode, operand, address):
    translated_instruction = ""

    if opcode == "move":
        translated_instruction = '0' if address == '0' else '1'
    elif opcode == "add":
        translated_instruction = '2' if address == '0' else '3'
    elif opcode == "sub":
        translated_instruction = '4' if address == '0' else '5'
    elif opcode == "or":
        translated_instruction = '6' if address == '0' else '7'
    elif opcode == "not":
        translated_instruction = '8' if address == '0' else '9'
    elif opcode == "shift":
        translated_instruction = 'a' if address == '0' else 'b'
    elif opcode == "jump":
        translated_instruction = 'c' if address == '0' else 'd'
    elif opcode == "goto":
        translated_instruction = 'e'
    elif opcode == "str":
        translated_instruction = 'f'

    return translated_instruction + operand

def validate_instruction(instruction):
    opcode, operand, address = instruction.split()
    operand = operand.replace(",", "") # Retira a vírgula do operando

    opcode_options = ['move', 'add', 'sub', 'or', 'not', 'shift', 'jump', 'goto', 'str']
    operand_options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    address_options = ['0', '1']

    if opcode not in opcode_options:
        raise ValueError(f"Invalid opcode: {opcode}")
    if operand not in operand_options:
        raise ValueError(f"Invalid operand: {operand}")
    if address not in address_options:
        raise ValueError(f"Invalid address: {address}")
    
    return opcode, operand, address

def read_instructions(input_file_name):
    try:
        with open(input_file_name, 'r') as file:
            instructions = [line.strip() for line in file.readlines()]

        if not instructions:
            print("Error: File is empty.")
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")

    return instructions

def main():
    input_file_name = "input.txt"
    output_file_name = "output.txt"
    output = []

    instructions = read_instructions(input_file_name)

    for instruction in instructions:
        opcode, operand, address = validate_instruction(instruction)

        translated_instruction = translate_instruction(opcode, operand, address)

        output.append(translated_instruction)
    
    write_instructions(output_file_name, output)

if __name__ == "__main__":
    main()