from sorting import *
            
def FindClosestPair(arrayOfPoint, pointCount,dimension,euc_count):
    pair = []
    if(pointCount == 2):
        d = euclidean_distance(arrayOfPoint[0],arrayOfPoint[1],dimension)
        #print(d)
        euc_count +=1
        pair.append(arrayOfPoint[0])
        pair.append(arrayOfPoint[1])

    elif(pointCount == 3): #Penanganan untuk banyak titik tidak 2^k
        d1 = euclidean_distance(arrayOfPoint[0],arrayOfPoint[1],dimension)
        d2 = euclidean_distance(arrayOfPoint[0],arrayOfPoint[2],dimension)
        d3 = euclidean_distance(arrayOfPoint[1],arrayOfPoint[2],dimension)
        euc_count += 3
        if (d1<=d2 and d1<=d3) :
            d = d1
            pair.append(arrayOfPoint[0])
            pair.append(arrayOfPoint[1])
        elif (d2<=d1 and d2<=d3) :
            d = d2
            pair.append(arrayOfPoint[0])
            pair.append(arrayOfPoint[2])
        else:
            d = d3
            pair.append(arrayOfPoint[1])
            pair.append(arrayOfPoint[2])

    else:
        k = pointCount//2
        arrayOfPoint1,arrayOfPoint2 = splitList(arrayOfPoint,pointCount)
        d1,pair1,euc_count = FindClosestPair(arrayOfPoint1,k,dimension,euc_count)
        d2,pair2,euc_count = FindClosestPair(arrayOfPoint2,pointCount-k,dimension,euc_count)
        if(d1<d2):
            d = d1
            pair = pair1
        else:
            d=d2
            pair = pair2
        
        for point1 in arrayOfPoint1:
            for point2 in arrayOfPoint2:
                if (dimension==1):
                    if(abs(point1[0]-point2[0])<d):
                        pair3 = []
                        d3 = euclidean_distance(point1,point2,dimension)
                        euc_count += 1
                        if(d3<d):
                            d = d3
                            pair3.append(point1)
                            pair3.append(point2)
                            pair = pair3
                elif (dimension==2):
                    if(abs(point1[0]-point2[0])<d and abs(point1[1]-point2[1]) < d):
                        pair3 = []
                        d3 = euclidean_distance(point1,point2,dimension)
                        euc_count += 1
                        if(d3<d):
                            d = d3
                            pair3.append(point1)
                            pair3.append(point2)
                            pair = pair3
                else:
                    if(abs(point1[0]-point2[0])<d and abs(point1[1]-point2[1]) < d and abs(point1[2]-point2[2])<d):
                        pair3 = []
                        d3 = euclidean_distance(point1,point2,dimension)
                        euc_count += 1
                        if(d3<d):
                            d = d3
                            pair3.append(point1)
                            pair3.append(point2)
                            pair = pair3
    return d,pair,euc_count

def euclidean_distance(point1,point2,dimension):
    sum = 0
    for i in range (dimension):
        sum += point1[i]**2 + point2[i]**2
    return sum**(0.5)

def splitList(array,b):
    k = b//2
    array1 = []
    array2 = []
    for i in range(k):
        array1.append(array[i])
    for i in range(k,b):
        array2.append(array[i])
    return array1,array2

def printPoint(point):
    print("(",end="")
    for i in range(len(point)-1):
        print(point[i],end="")
        print(",",end="")
    print(point[len(point)-1],end="")
    print(")")
    return