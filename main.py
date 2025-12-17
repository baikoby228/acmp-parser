from parser import get_tests
from validator import check_test

BAD_TESTS = [620]

L = 620
R = 1000
FORMAT_FILE_NAME = 'format.txt'

if __name__ == '__main__':
    for i in range(L, R + 1):
        if i in BAD_TESTS:
            continue

        print('start check task', i)
        tests = get_tests(i)
        #print(tests)

        flag = True
        for test in tests:
            if not check_test(FORMAT_FILE_NAME, test):
                flag = False
                break
        if flag:
            print('find test:', i)
