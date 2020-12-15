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
        C = [[float(A[n][m]) + float(B[n][m]) for m in range(len(A[0]))] for n in range(len(A))]
        print("The result is:")
        for i in range(0, len(C)):
            print(" ".join(map(str, C[i])))
    else:
        print("The operation cannot be performed.")
        

def multiply_matrix_by_constant():
    A = []
    an, am = input("Enter size of matrix: ").split()
    print("Enter matrix:")
    for i in range(0, int(an)):
        A.append(input().split())
    scalar = float(input("Enter constant: "))
    C = [[float(A[n][m]) * scalar for m in range(len(A[0]))] for n in range(len(A))]
    print("The result is:")
    for i in range(0, len(C)):
        print(" ".join(map(str, C[i])))


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
        print("The result is:")
        for i in range(0, len(C)):
            print(" ".join(map(str, C[i])))
    else:
        print("The operation cannot be performed")


def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


def main():
    print_menu()
    choice = int(input("Your choice: "))
    while choice != 0:
        if choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_matrix_by_constant()
        elif choice == 3:
            multiply_matrices()
        print_menu()
        choice = int(input("Your choice: "))



main()
