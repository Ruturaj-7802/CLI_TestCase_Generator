import random
def tree():
    vl, vh = map(int, input("Range of vertices : ").split())
    while True:
        v1 = random.randint(vl, vh)
        if v1 != 1:
            break
    pruferCode = []
    for i in range(v1-2):
        element = random.randint(1, v1)
        pruferCode.append(element)
    
    edges = []
    freqCount = {}
    print(v1)
    print(pruferCode)    

    for i in range(1, v1+1):
        freqCount[i] = 0
    for i in pruferCode:
        freqCount[i] = freqCount[i] + 1
    print(freqCount)
    
    for i in pruferCode:
        edge1 = i
        for j in range(1, v1+1):
            if freqCount[j] == 0:
                edge2 = j
                break        
        edges.append([edge1, edge2])
        freqCount[edge1]-=1
        freqCount[edge2]-=1

    cnt =0
    for i in range(1, v1+1):
        if(freqCount[i] == 0):
            if(cnt == 0):
                edge1 = i
                cnt+=1
            elif(cnt == 1):
                edge2 = i
                break
    edges.append([edge1, edge2])

    
    print(edges)
        

tree()


    


