if __name__ == "__main__":
    total_code_length = 0
    total_memory_length = 0
    with open("2015/day8_input.txt", "r") as f:
        content = f.read().strip().split("\n")
        for line in content:
            current_line_memory_length = 0
            i = 1
            while i < len(line) - 1:
                if line[i] == '\\':
                    if line[i + 1] == 'x':
                        i += 3
                    else:
                        i += 1
                current_line_memory_length += 1
                i += 1
            total_code_length += len(line)
            total_memory_length += current_line_memory_length
    print(total_code_length - total_memory_length)