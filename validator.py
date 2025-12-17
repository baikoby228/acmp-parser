def check_test(FORMAT_FILE_NAME: str, test: list):
    format = []
    with open(FORMAT_FILE_NAME, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                format.append(parts)

    pos = 0
    mp = {}
    for row in format:
        type = row[0]

        if type == 'int':
            name = row[1]
            if pos == len(test):
                #print('bad')
                return False
            if not isinstance(test[pos], int):
                #print('not int')
                return False
            mp[name] = test[pos]
            pos += 1

        if type == 'ints':
            size = row[1]
            if 'a' <= size[0] <= 'z':
                size = mp[size]
            else:
                size = int(size)
            name = row[2]
            mp[name] = []
            for i in range(size):
                if pos == len(test):
                    #print('bad')
                    return False
                if not isinstance(test[pos], int):
                    #print('not int')
                    return False
                mp[name].append(test[pos])
                pos += 1

    #print('mp =', mp)
    return pos == len(test)
