from parser import get_tests
from validator import check_test

L = 1
R = 6
FORMAT_FILE_NAME = 'test.txt'
if __name__ == '__main__':
    for i in range(L, R + 1):
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
