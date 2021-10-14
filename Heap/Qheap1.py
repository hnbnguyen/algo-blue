t = int(input())
def solve(t):
    arr = []
    for i in range(t):
        c = input()
        if len(c) == 1:
            print(min(arr))
        else:
            c = list(map(int, c.split()))
            if c[0] == 1:
                arr.append(c[1])
            else:
                arr.remove(c[1])

solve(t)