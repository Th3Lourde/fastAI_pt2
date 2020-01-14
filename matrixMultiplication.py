

'''
Ok so we are implementing matrix multiplication with python
Shouldn't be too hard :)

1) Check to make sure that the dimensions 'add up'
2) Create output matrix
3) Iterate, return answer
'''

# Assuming x,y will be List[List[int]]
def maxtrixMult(x,y):
    # 1) order matters, so this is x*y
    # num of columns in x must equal
    # num of rows in y, or we can't
    # carry out the operation.

    if (type(x) != list or type(x[0]) != list) or (type(y) != list or type(y[0]) != list):
        print("[Error] inputs are not both matrices")
        return None

    elif len(x[0]) != len(y):
        print("[Error] dimensions of inputs do not meet computational requirements")
        return None


    column = [0]*len(y[0])

    ans = [] # initialize empty output matrix
    for i in range(len(x)):
        ans.append(column)


    tmp = []

    a = []
    for j in range(len(x[0])):
        for i in range(len(x)):
            a.append(x[i][j])

    b = []
    for h in range(len(y)):
        for k in range(len(y[0])):
            b.append(y[h][k])


    # print("a: {}".format(a))
    # print("b: {}".format(b))

    for i in range(len(a)):
        a[i] *= b[i]

    # print("a: {}".format(a))

    for i in range(len(x[0])): # number of rows in ans
        start = i*len(y[0])
        end = i*len(y[0]) + len(y[0]) + 1
        tmp.append(a[start:end])

    print(tmp)





if __name__ == '__main__':
    x = [
        [1],
        [2],
        [3]
        ]

    y = [[1,2,3]]

    # print(len(x[0]))
    # print(len(y))


    '''
    Try # 2
    x: {{1,2,3},{3,2,1},{1,2,3}}
    y: {{4,5,6},{6,5,4},{4,6,5}}
    '''

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

    maxtrixMult(x,y)
