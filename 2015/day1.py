if __name__ == "__main__":
    cnt = 0
    fst_pos = 0
    with open("2015/day1_input.txt", "r") as f:
        line = f.readline()
        line = list(line)
        for i in range(len(line)):
            if line[i] == "(":
                cnt += 1
            elif line[i] == ")":
                cnt -= 1
            if cnt < 0 and fst_pos == 0:
                fst_pos = i + 1
    print(cnt)
    print(fst_pos)