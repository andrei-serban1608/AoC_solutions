if __name__ == "__main__":
    total_code_length = 0
    total_embedded_length = 0
    with open("2015/day8_input.txt", "r") as f:
        content = f.read().strip().split("\n")
        for line in content:
            current_line_embedded_length = 2
            for c in line:
                if c == '\"' or c == '\\':
                    current_line_embedded_length += 2
                else:
                    current_line_embedded_length += 1
            total_code_length += len(line)
            total_embedded_length += current_line_embedded_length
    print(total_embedded_length - total_code_length)