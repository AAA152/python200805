while True:
    print('-----------------')
    print('1. 加法')   
    print('2. 減法')
    print('3. 乘法')
    print('4. 除法')
    print('5. 離開')
    Sel =int(input('請輸入選項:'))
    if Sel == 1:
        n1 =int(input('請輸入數字一:'))   
        n2 =int(input('請輸入數字二:'))
        print(n1,'+',n2, '=', n1+n2)
    if Sel == 2:
        n3 =int(input('請輸入數字一:'))   
        n4 =int(input('請輸入數字二:'))
        print(n3, '-',n4, '=', n3-n4)
    if Sel == 3:
        n5 =int(input('請輸入數字一:'))   
        n6 =int(input('請輸入數字二:'))
        print(n5, 'x',n6, '=', n5*n6)
    if Sel == 4:
        n7 =int(input('請輸入數字一:'))   
        n8 =int(input('請輸入數字二:'))
        print(n7, '/',n8, '=', n7/n8)
    else:
        break
        
       