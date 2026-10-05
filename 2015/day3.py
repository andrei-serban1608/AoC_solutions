if __name__ == "__main__":
    position_santa = (0, 0)
    position_robo_santa = (0, 0)
    total_coordinates = [position_santa]
    with open("2015/day3_input.txt", "r") as f:
        coordinates = f.readline()
        while coordinates != "":
            coordinates = list(coordinates.strip())
            santa_turn = True
            for c in coordinates:
                if santa_turn:
                    if c == '^':
                        position_santa = (position_santa[0], position_santa[1] + 1)
                    elif c == 'v':
                        position_santa = (position_santa[0], position_santa[1] - 1)
                    elif c == '>':
                        position_santa = (position_santa[0] + 1, position_santa[1])
                    elif c == '<':
                        position_santa = (position_santa[0] - 1, position_santa[1])
                    else:
                        print("ERROR: Invalid coordinate!")
                    total_coordinates.append(position_santa)
                else:
                    if c == '^':
                        position_robo_santa = (position_robo_santa[0], position_robo_santa[1] + 1)
                    elif c == 'v':
                        position_robo_santa = (position_robo_santa[0], position_robo_santa[1] - 1)
                    elif c == '>':
                        position_robo_santa = (position_robo_santa[0] + 1, position_robo_santa[1])
                    elif c == '<':
                        position_robo_santa = (position_robo_santa[0] - 1, position_robo_santa[1])
                    else:
                        print("ERROR: Invalid coordinate!")
                    total_coordinates.append(position_robo_santa)
                santa_turn = not santa_turn
            coordinates = f.readline()
    no_of_houses = len(set(total_coordinates))
    print(no_of_houses)