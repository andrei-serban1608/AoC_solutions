from hashlib import md5

def list_hex(s):
    return list(hex(s))

def append_key(k, num):
    return k + str(num)

if __name__ == "__main__":
    not_found = True
    with open("2015/day4_input.txt", "r") as f:
        key = f.read().strip()
    num = 1
    while not_found:
        str_to_hash = append_key(key, num)
        hash_res = md5(str_to_hash.encode()).hexdigest()
        # for part one replace the if statement with
        # if hash_res[0:5] == "00000":
        if hash_res[0:6] == "000000":
            not_found = False
        else:
            num += 1
    print(num)
