import numpy as np


def lecture_graph(path):
    with open(path, "r") as f:
        m = 0
        n = 0
        cols = []
        fv = []
        # print(fv)
        # print(cols)
        for lineNum, line in enumerate(f):

            if(lineNum == 0):
                n = int(line)
                print(1/n)
                # print(n)
                fv = np.zeros((1,n),dtype="int64")
                for k in range(0,n):
                    cols.append([])
                # print(cols)

            elif(lineNum == 1):
                m = int(line)

            elif(line[0] != "\n"):
                l = line.split()
                # print(l)
                i = int(l[0])
                # print(i)
                d = int(l[1])
                if(d == 0):
                    fv[0,i-1] = 1
                elif(d > 0 and len(l) >= 4):
                    lastJ = -1
                    somme = 0
                    for index in range(2,len(l),2):
                        if(l[index] != "\n"):
                            j = int(l[index])
                            # print(j)
                            Mij = float(l[index+1])
                            somme = somme + Mij
                            # print(j, Mij,sep=" ")
                            cols[j-1].append(np.array([i-1,Mij],dtype="float64"))
                            lastJ = j
                    # print(somme)
                    # print(cols[lastJ-1][-1][-1])
                    # if(somme != 1.0 and lastJ != -1):
                        # cols[lastJ-1][-1][-1] += (1-somme)
        # for elems in cols:
        #     print(elems)
        return (n, m, cols, fv)

def iter_pi(n, e, cols, f, a=0.85):
    pi = np.zeros((1,n),dtype="float64")
    w = pi.dot(f.transpose())
    # print(pi)
    newPi = np.full((1,n), 1/n ,dtype="float64")
    # e = 10**-5
    while np.linalg.norm((newPi - pi), ord=1) > e:



        for j in range(0,n):
            pi[0,j] = newPi[0,j]
       
        w = pi.dot(f.transpose())
        for j in range(0,n):
            s = 0
            for elem in cols[j]:
                s += pi[0,int(elem[0])]*elem[1]
            newPi[0,j] = s*a + ((1-a)/n) + (w*a/n)
        print(np.linalg.norm((newPi - pi), ord=1))

    print(newPi)
    print(np.sum(newPi))
    return newPi

n, m, cols, fv = lecture_graph("wikipedia-20051105V2.txt")

pi = iter_pi(n, 10**-9,cols,fv,0.85)

# print(np.unique(pi))





    # cols[0].append((1,0.5))
    # print(cols)