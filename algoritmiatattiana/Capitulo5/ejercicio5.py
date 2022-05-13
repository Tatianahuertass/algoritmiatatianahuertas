lp=[]
i=0
while i < 20:
    p=int(input("por favor digite el tañano de lista, que desea capturar : "))
    while p < 0:
        print ("por favor digite numero postivos")
        break
    lp.append(p)
    i+=1
    posi = list(filter(lambda j: j>=0, lp))
    print(posi)

