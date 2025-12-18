import time

from dotenv import load_dotenv
import os

from parser import get_tests
from validator import check_test

BAD_TESTS = [620]

load_dotenv()
L = int(os.getenv('L'))
R = int(os.getenv('R'))
FORMAT_FILE_NAME = os.getenv('FORMAT_FILE_NAME')

if __name__ == '__main__':
    res = []

    start = time.perf_counter()
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
            res.append(i)
    end = time.perf_counter()

    print('result:')
    for x in res:
        print(x)

    print(f"Время: {end - start:.6f} сек")