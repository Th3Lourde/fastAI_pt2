import matrixMultiplication as lib


x = [
    [1,2,3],
    [3,2,1],
    [1,2,3],
    ]

y = [
    [4,5,6],
    [6,5,4],
    [4,6,5],
    ]

# print(lib.matrixMult(x,y))

def test_matrixMult(tests):
    for i in range(len(tests)):
        assert lib.matrixMult(tests[i][0], tests[i][1]) == tests[i][2] , "got {}*{} = {}\nwant {}*{} = {}".format(tests[i][0], tests[i][1], lib.matrixMult(tests[i][0], tests[i][1]), tests[i][0], tests[i][1], tests[i][2])

if __name__ == '__main__':
    '''
    This tests the function matrixMult(x,y)
    in the file called matrixMultiplication.py

    Have a lists of tests. Each element is 3 matrices
    x,y,x*y
    '''
    tests = [
        [
            [[1],[2],[3]],
            [[2,1]],
            [[2,1],[4,2],[6,3]]
        ],
        [
            [ [1,2,3], [3,2,1], [1,2,3], ],
            [ [4,5,6], [6,5,4], [4,6,5], ],
            [[28, 33, 29], [28, 31, 31], [28, 33, 29]],
        ]
    ]

    errs = test_matrixMult(tests)

    if not errs:
        print("[tests] {}/{} complete :)".format(len(tests),len(tests)))
