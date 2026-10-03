if __name__ == "__main__":
    total_paper = 0
    total_ribbon = 0
    with open("day2_input.txt", "r") as f:
        line = f.readline()
        while line != "":
            l = int(line[0:line.find("x")])
            line = line[line.find("x") + 1:]
            w = int(line[0:line.find("x")])
            line = line[line.find("x") + 1:]
            h = int(line.strip())
            volume = l * w * h
            peri1 = 2 * (l + w)
            peri2 = 2 * (w + h)
            peri3 = 2 * (h + l)
            ribbon = min(peri1, peri2, peri3) + volume
            total_ribbon += ribbon
            side1 = l * w
            side2 = w * h
            side3 = h * l
            paper = 2 * (side1 + side2 + side3) + min(side1, side2, side3)
            total_paper += paper
            line = f.readline()
    print(total_paper)
    print(total_ribbon)
