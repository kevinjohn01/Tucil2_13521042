#Mengurutkan List berdasarkan nilai x nya
def Partition(m,i,j):
    pivot = m[j]
    p = i-1
    for q in range (i,j):
        if (m[q] <= pivot):
            p += 1
            temp = m[q]
            m[q] = m[p]
            m[p] = temp
    temp = m[p+1]
    m[p+1] = m[j]
    m[j] = temp
    return p+1
#    while (p>=q) :
#        while(m[p][0] < pivot) :
#            p +=1
#        
#        while(m[q][0] > pivot):
#            q -= 1
#        
#        if (p<q):
#            #swap m[p] dan m[q]
#            temp = m[p]
#            m[p] = m[q]
#            m[q] = temp
#
#    return q
#        
#        
def quickSort(m,i,j):
    if(i<j):
        k = Partition(m,i,j)
        quickSort(m,i,k-1)
        quickSort(m,k,j)
    return
