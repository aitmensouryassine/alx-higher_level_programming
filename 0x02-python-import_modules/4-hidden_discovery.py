#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list = dir(hidden_4)
    list_len = len(list)

    for i in range(0, list_len):
        if list[i][0:2] != "__":
            print(list[i])
