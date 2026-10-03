lights = [[0 for _ in range(1000)] for _ in range(1000)]

def parse_instruction(ins):
    ins_tokens = ins.strip().split(" ")
    if ins_tokens[0] == "toggle":
        start_str = ins_tokens[1]
        action = ins_tokens[0]
    elif ins_tokens[0] == "turn":
        start_str = ins_tokens[2]
        action = ins_tokens[0] + " " + ins_tokens[1]
    else:
        raise Exception("Invalid instruction!")
    end_str = ins_tokens[-1]
    start = [int(n) for n in start_str.split(",")]
    end = [int(n) for n in end_str.split(",")]
    if len(start) != 2 or len(end) != 2:
        raise Exception("Invalid coordinates in instruction!")
    return action, start, end

def turn_on(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            lights[i][j] += 1

def turn_off(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            lights[i][j] = max(0, lights[i][j] - 1)

def toggle(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            lights[i][j] += 2

if __name__ == "__main__":
    with open("day6_input.txt", "r") as f:
        instruction = f.readline()
        while instruction != "":
            action, start, end = parse_instruction(instruction)
            if action == "turn on":
                turn_on(start, end)
            elif action == "turn off":
                turn_off(start,end)
            else:
                toggle(start, end)
            instruction = f.readline()

    total_lights = 0
    for i in range(1000):
        for j in range(1000):
            total_lights += lights[i][j]

    print(total_lights)