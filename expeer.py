#beer problem
for num in range(2,21,1):
    nn=num/2
    nt=[nn]
    nb=nn
    nl=nn
    while nb>=3 or nl>=5:
        nb1=nb/3
        nl1=nl/5
        nn=nb1+nl1
        modub=nb-nb1*3
        modul=nl-nl1*5
        nb=nb1+modub+nl1
        nl=nb1+modul+nl1
        nt.append(nn)
    nsum=sum(nt)
    print num,nsum
