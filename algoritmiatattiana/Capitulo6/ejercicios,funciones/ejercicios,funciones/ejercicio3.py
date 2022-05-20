#elabore un programa que
#si una lista esta vacia
#la debe llenar con la serie Fibonacci hasta
50.

def fibonacci(num):
    a= [0,1]
    if num==1:
        print('0')
    elif num==2:
        print('[0,','1]')
    else:
        while(len(a)<num):
            a.append(0)
        if(num==0 or num==1):
            return 1
        else:
            a[0]=0
            a[1]=1
            for i in range(2,num):
                a[i]=a[i-1]+a[i-2]
            print(a)

fibonacci(50)