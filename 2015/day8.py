def parse_string(s):
    tokens = list(s)
    print(tokens)

if __name__ == "__main__":
    with open("test.txt", "r") as f:
        line = f.read().split("\n")
        print(list(line))