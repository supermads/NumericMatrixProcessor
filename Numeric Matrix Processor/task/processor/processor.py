def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("0. Exit")


def get_one_matrix():
    a = []
    an, am = map(int, input("Enter size of matrix: ").split())
    print("Enter matrix:")
    for i in range(0, int(an)):
        a.append(list(map(float, input().split())))
    return a, an, am


def get_two_matrices():
    a = []
    b = []
    an, am = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix: ")
    for i in range(0, an):
        a.append(list(map(float, input().split())))
    bn, bm = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix: ")
    for i in range(0, bn):
        b.append(list(map(float, input().split())))
    return a, an, am, b, bn, bm


def add_matrices(a, an, am, b, bn, bm):
    if an == bn and am == bm:
        return [[float(a[n][m]) + float(b[n][m]) for m in range(len(a[0]))] for n in range(len(a))]
    else:
        return []


def multiply_matrix_by_constant(a):
    scalar = float(input("Enter constant: "))
    return [[a[n][m] * scalar for m in range(len(a[0]))] for n in range(len(a))]


def multiply_matrices(a, an, am, b, bn, bm):
    if am == bn:
        c = [[0 for _i in range(bm)] for _j in range(an)]
        for n in range(an):
            for m in range(bm):
                acc = 0
                for x in range(am):
                    acc += float(a[n][x]) * float(b[x][m])
                c[n][m] = acc
        return c
    else:
        return []


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    t = int(input())
    print("Your choice: {}".format(t))
    a, an, am = get_one_matrix()
    if t == 1:
        return [[a[m][n] for m in range(len(a[0]))] for n in range(len(a))]
    elif t == 2:
        return [[a[am - 1 - m][an - 1 - n] for m in range(len(a[0]))] for n in range(len(a))]
    elif t == 3:
        return [[a[n][am - 1 - m] for m in range(len(a[0]))] for n in range(len(a))]
    else:
        return [[a[an - 1 - n][m] for m in range(len(a[0]))] for n in range(len(a))]


def find_determinant(a, an, am):
    d = 0
    if an == 1:
        d = a[0][0]
    elif an == 2:
        d = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
    else:
        for i in range(am):
            cofactor = a[0][i] * pow(-1, i)
            d += cofactor * find_determinant([[a[n][m] for n in range(1, an)] for m in range(am) if m != i], an - 1, am - 1)
    return d


def main():
    print_menu()
    choice = int(input("Your choice: "))
    while choice != 0:
        if choice == 1:
            c = add_matrices(*get_two_matrices())
        elif choice == 2:
            c = multiply_matrix_by_constant(get_one_matrix()[0])
        elif choice == 3:
            c = multiply_matrices(*get_two_matrices())
        elif choice == 4:
            c = transpose_matrix()
        if choice == 5:
            print("The result is:")
            print(find_determinant(*get_one_matrix()))
        elif c:
            print("The result is:")
            for i in range(0, len(c)):
                print(" ".join(map(str, c[i])))
        else:
            print("The operation cannot be performed.")
        print_menu()
        choice = int(input("Your choice: "))



main()
