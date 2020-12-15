def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


def add_matrices():
    A = []
    B = []
    an, am = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix: ")
    for i in range(0, an):
        A.append(input().split())
    bn, bm = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix: ")
    for i in range(0, bn):
        B.append(input().split())
    if an == bn and am == bm:
        return [[float(A[n][m]) + float(B[n][m]) for m in range(len(A[0]))] for n in range(len(A))]
    else:
        return []
        

def multiply_matrix_by_constant():
    A = []
    an, am = input("Enter size of matrix: ").split()
    print("Enter matrix:")
    for i in range(0, int(an)):
        A.append(input().split())
    scalar = float(input("Enter constant: "))
    return [[float(A[n][m]) * scalar for m in range(len(A[0]))] for n in range(len(A))]


def multiply_matrices():
    A = []
    B = []
    an, am = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix: ")
    for i in range(0, an):
        A.append(input().split())
    bn, bm = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix: ")
    for i in range(0, bn):
        B.append(input().split())
    if am == bn:
        C = [[0 for _i in range (bm)] for _j in range(an)]
        for n in range(an):
            for m in range(bm):
                acc = 0
                for x in range(am):
                    acc += float(A[n][x]) * float(B[x][m])
                C[n][m] = acc
        return C
    else:
        return []


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    t = int(input())
    print("Your choice: {}".format(t))
    an, am = map(int, input("Enter matrix size: ").split())
    a = []
    print("Enter matrix: ")
    for i in range(0, an):
        a.append(list(map(float, input().split())))
    if t == 1:
        return [[a[m][n] for m in range(len(a[0]))] for n in range(len(a))]
    elif t == 2:
        return [[a[am - 1 - m][an - 1 - n] for m in range(len(a[0]))] for n in range(len(a))]
    elif t == 3:
        return [[a[n][am - 1 - m] for m in range(len(a[0]))] for n in range(len(a))]
    else:
        return [[a[an - 1 - n][m] for m in range(len(a[0]))] for n in range(len(a))]


def main():
    print_menu()
    choice = int(input("Your choice: "))
    while choice != 0:
        if choice == 1:
            C = add_matrices()
        elif choice == 2:
            C = multiply_matrix_by_constant()
        elif choice == 3:
            C = multiply_matrices()
        elif choice == 4:
            C = transpose_matrix()
        if C:
            print("The result is:")
            for i in range(0, len(C)):
                print(" ".join(map(str, C[i])))
        else:
            print("The operation cannot be performed.")
        print_menu()
        choice = int(input("Your choice: "))



main()
