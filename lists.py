if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'insert':
            position = int(cmd[1])
            value = int(cmd[2])
            arr.insert(position, value)
        
        if cmd[0] == 'remove':
            r_value = int(cmd[1])
            arr.remove(r_value)
            
        if cmd[0] == 'append':
            apnd_value = int(cmd[1])
            arr.append(apnd_value)
        
        if cmd[0] == 'sort':
            arr.sort()
        
        if cmd[0] == 'pop':
            arr.pop()
        
        if cmd[0] == 'reverse':
            arr.reverse()
        
        if cmd[0] == 'print':
            print(arr)
        
            
            
            
    