if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    a = set(a) #To remore duplicate values
    a = list(a)
    a.sort(reverse=True) #make descending order
    print(a[1])


