from findClosestPair import euclidean_distance

def bruteforce(arrayOfPoint, pointCount,dimension):
    count =0
    pair = []
    d = 99999999999999999999
    for i in range(pointCount):
        for j in range(i+1,pointCount):
            pairnow= []
            dnow = euclidean_distance(arrayOfPoint[i],arrayOfPoint[j],dimension)
            count+=1
            #print(dnow)
            pairnow.append(arrayOfPoint[i])
            pairnow.append(arrayOfPoint[j])
            if(dnow<d):
                d = dnow
                pair  = pairnow
    print("Terdapat",count,"kali perhitungan euclidean distance")
    return d,pair
