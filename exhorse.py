def horse(x):
    count=1
    z=0
    a=0
    b=0
    for i in range(z,len(x)-2):
        z=z+1
        count=count+1
        if (x[i]=='hit') & (x[i+1]=='miss'):
            if x[i+2]=='hit':
                z=z+1
                if count%2==0:
                    if x[i+1]=='hit':
                        a=a+1
                    else:
                        b=b+1
                else:
                    if x[i+1]=='hit':
                        b=b+1
                    else:
                        a=a+1
                    count=count+1
        if (a==5)|(b==5):
            if a==5:
                print 'the game ends, b wins'
            if b==5:
                print 'the game ends, a wins'
            break
    m=list()
    n=list()
    count=0
    for i in 'Horse':
        count=count+1
        if count>a:
            break
        else:
            m.append(i)
    count=0
    for j in 'Horse':
        count=count+1
        if count>b:
            break
        else:
            n.append(j)
    m=str(m)
    n=str(n)
    print 'the first person gets',m,',the second person gets',n
    
        
                
                
            
            
                
            
                
            
        
        
        
