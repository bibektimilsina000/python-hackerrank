if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x = [p for p in range(x+1)]
    y = [q for q in range(y+1)]
    z = [r for r in range(z+1)]

final = [[i, j, k] for i in x for j in y for k in z]
req = [l for l in final if sum(l) != n]
print(req)
