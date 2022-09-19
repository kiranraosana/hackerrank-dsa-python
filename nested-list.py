if __name__ == '__main__':
    c = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        c[name] = score
        
    r = set(c.values())
    d = []
    for i in c:
        if c[i] == sorted(list(r))[1]:
            d.append(i)
    for i in sorted(d):
        print(i)