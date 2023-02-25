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
     
def quickSort(m,i,j):
    if(i<j):
        k = Partition(m,i,j)
        quickSort(m,i,k-1)
        quickSort(m,k,j)
    return
