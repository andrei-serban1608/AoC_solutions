import numpy as np

signal_map = {}

def parse_operation(op):
    op_tokens = op.strip().split(" ")
    signal = op_tokens[-1]
    # if condition only for task 2
    if signal == 'b':
        signal_map[signal] = np.uint16(16076)
    elif op_tokens[1] == "->":
        if op_tokens[0].isdigit() or op_tokens[0] in signal_map.keys():
            input = 0
            if op_tokens[0].isdigit():
                input = np.uint16(op_tokens[0])
            else:
                input = signal_map[op_tokens[0]]
            if isinstance(input, np.uint16):
                signal_map[signal] = input
    elif op_tokens[0] == "NOT":
        if op_tokens[1].isdigit() or op_tokens[1] in signal_map.keys():
            input = 0
            if op_tokens[1].isdigit():
                input = np.uint16(op_tokens[1])
            else:
                input = signal_map[op_tokens[1]]
            if isinstance(input, np.uint16):   
                signal_map[signal] = ~input
    elif op_tokens[1] == "AND":
        if (op_tokens[0].isdigit() or op_tokens[0] in signal_map.keys()) and (op_tokens[2].isdigit() or op_tokens[2] in signal_map.keys()):
            input1 = 0
            input2 = 0
            if op_tokens[0].isdigit():
                input1 = np.uint16(op_tokens[0])
            else:
                input1 = signal_map[op_tokens[0]]
            if op_tokens[2].isdigit():
                input2 = np.uint16(op_tokens[2])
            else:
                input2 = signal_map[op_tokens[2]]
            if isinstance(input1, np.uint16) and isinstance(input2, np.uint16):
                signal_map[signal] = input1 & input2
    elif op_tokens[1] == "OR":
        if (op_tokens[0].isdigit() or op_tokens[0] in signal_map.keys()) and (op_tokens[2].isdigit() or op_tokens[2] in signal_map.keys()):
            input1 = 0
            input2 = 0
            if op_tokens[0].isdigit():
                input1 = np.uint16(op_tokens[0])
            else:
                input1 = signal_map[op_tokens[0]]
            if op_tokens[2].isdigit():
                input2 = np.uint16(op_tokens[2])
            else:
                input2 = signal_map[op_tokens[2]]
            if isinstance(input1, np.uint16) and isinstance(input2, np.uint16):
                signal_map[signal] = input1 | input2
    elif op_tokens[1] == "LSHIFT":
        if (op_tokens[0].isdigit() or op_tokens[0] in signal_map.keys()) and (op_tokens[2].isdigit() or op_tokens[2] in signal_map.keys()):
            input = 0
            num_bits = 0
            if op_tokens[0].isdigit():
                input = np.uint16(op_tokens[0])
            else:
                input = signal_map[op_tokens[0]]
            if op_tokens[2].isdigit():
                num_bits = np.uint16(op_tokens[2])
            else:
                num_bits = signal_map[op_tokens[2]]
            if isinstance(input, np.uint16) and isinstance(num_bits, np.uint16):
                signal_map[signal] = input << num_bits
    elif op_tokens[1] == "RSHIFT":
        if (op_tokens[0].isdigit() or op_tokens[0] in signal_map.keys()) and (op_tokens[2].isdigit() or op_tokens[2] in signal_map.keys()):
            input = 0
            num_bits = 0
            if op_tokens[0].isdigit():
                input = np.uint16(op_tokens[0])
            else:
                input = signal_map[op_tokens[0]]
            if op_tokens[2].isdigit():
                num_bits = np.uint16(op_tokens[2])
            else:
                num_bits = signal_map[op_tokens[2]]
            if isinstance(input, np.uint16) and isinstance(num_bits, np.uint16):
                signal_map[signal] = input >> num_bits
    else:
        raise Exception("Invalid operation!")

if __name__ == "__main__":
    while 'a' not in signal_map.keys():
        with open("day7_input.txt", "r") as f:
            op = f.readline()
            while op != "":
                parse_operation(op)
                op = f.readline()
    print(signal_map['a'])
