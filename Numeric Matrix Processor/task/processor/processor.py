def add_matrices():
    an, am = input().split()
    an = int(an)
    am = int(am)
    A = []
    B = []
    for i in range(0, an):
        A.append(input().split())
    bn, bm = input().split()
    bn = int(bn)
    bm = int(bm)
    for i in range(0, bn):
        B.append(input().split())
    if an == bn and am == bm:
        C = [[int(A[n][m]) + int(B[n][m]) for m in range(len(A[0]))] for n in range(len(A))]
        for i in range(0, len(C)):
            print(" ".join(map(str, C[i])))
    else:
        print("ERROR")
        

def multiply_matrix():
    an, am = input().split()
    A = []
    for i in range(0, int(an)):
        A.append(input().split())
    scalar = int(input())
    C = [[int(A[n][m]) * scalar for m in range(len(A[0]))] for n in range(len(A))]
    print(C)
    for i in range(0, len(C)):
        print(" ".join(map(str, C[i])))

