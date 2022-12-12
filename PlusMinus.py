def plusMinus(arr):
    zero = pos = neg = 0
    length = len(arr)
    for x in arr:
        if x == 0:
            zero += 1
        
        

        if x > 0:
            pos +=1
        
        


        if x < 0:
            neg +=1
        
    print(f'{(pos/length):.6f}')
    print(f'{(neg/length):.6f}')
    print(f'{(zero/length):.6f}')