import random
import time
import matplotlib.pyplot as plt
from sorting import *
from findClosestPair import *
from bruteforce import *

#Program untuk Mencari 2 Titik dengan Jarak Terpendek dari Daftar Titik yang Dibangkitkan secara Acak

#Input dimensi dan generate titik random
R = int(input("Masukkan Dimensi: "))
N = int(input("Masukkan Jumlah Titik: "))
PointList = [[(random.uniform(-1000000,1000000)) for j in range(R)] for i in range (N)]

#Sorting elemen titik berdasarkan absis
quickSort(PointList,0,N-1)

#Pencarian dengan Divide and Conquer
euc_count=0                                                         #counter
start = time.time()                                                 #inisialisasi waktu
d, pair,euc_count= FindClosestPair(PointList,N,R,euc_count)         #mencari pasangan titik terdekat
stop = time.time()                                                  #waktu berhenti                  
print("Pencarian dengan Divide and Conquer:")
print("Pasangan titik: ")
printPoint(pair[0])                                                 #Menampilkan titik pertama
printPoint(pair[1])                                                 #Menampilkan titik kedua
print("Dengan jarak",d)                                             #Menampilkan jarak kedua titik
print("Terdapat",euc_count, "kali perhitungan euclidean distance")  #Menampilkan berapa kali pemanggilan euclidean distance
print("Execution time:", stop-start)                                #Menampilkan waktu eksekusi

print()
print("======================================================================================")
print()

#Pencarian dengan Brute Force
print("Tampilkan Solusi dengan Brute Force? (y/n)")
n=input()
if (n=='y'):
    start = time.time()                                             #inisialisasi waktu
    print("Perhitungan dengan Brute Force")
    d2,pair2 = bruteforce(PointList,N,R)                            #Perhitungan dengan brute force
    stop = time.time()                                              #waktu berhenti
    print("Pasangan titik: ")
    printPoint(pair2[0])                                            #Menampilkan titik pertama
    printPoint(pair2[1])                                            #Menampilkan titik kedua
    print("Dengan jarak:",d2)                                       #Menampilkan jarak
    print("Execution time: ", stop-start)                           #Menampilkan waktu

if (R == 3):
    print("Tampilkan visualisasi data? (y/n)")
    n=input()
    if (n=='y'):
        x =[]
        y =[]
        z =[]
        xa = []
        ya = []
        za = []
        for point in PointList:
            if(point == pair[0] or point == pair[1]):
                xa.append(point[0])                                     #Assign nilai x untuk pasangan titik terdekat
                ya.append(point[1])                                     #Assign nilai y untuk pasangan titik terdekat
                za.append(point[2])                                     #Assign nilai z untuk pasangan titik terdekat
            else:
                x.append(point[0])                                      #Assign nilai x untuk titik yang lain
                y.append(point[1])                                      #Assign nilai x untuk titik yang lain
                z.append(point[2])                                      #Assign nilai x untuk titik yang lain
        fig = plt.figure(figsize = (20,20))
        ax = plt.axes(projection = "3d")
        ax.scatter3D(x,y,z,color="green")                               #Menampilkan titik lain dengan warna hijau
        ax.scatter3D(xa,ya,za,color = "red")                            #Menampilkan pasangan titik terdekat dengan warna merah
        plt.show()
print("Terima kasih sudah menggunakan program ini!")


