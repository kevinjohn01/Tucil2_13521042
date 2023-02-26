import random
import time
from lib.sorting import *
from lib.findClosestPair import *
from lib.bruteforce import *
from lib.visualization import *

#Program untuk Mencari 2 Titik dengan Jarak Terpendek dari Daftar Titik yang Dibangkitkan secara Acak

#Input dimensi dan generate titik random
R = int(input("Masukkan Dimensi: "))
N = int(input("Masukkan Banyak Titik: "))
while(N<2):
    print("Masukan tidak valid, silahkan coba lagi")
    N = int(input("Masukkan Banyak Titik: "))
PointList = [[(random.uniform(-1000000,1000000)) for j in range(R)] for i in range (N)]

#Sorting elemen titik berdasarkan absis
quickSort(PointList,0,N-1)

#Pencarian dengan Divide and Conquer
euc_count=0                                                         #counter
start = time.time()                                                 #inisialisasi waktu
d, pair,euc_count= FindClosestPair(PointList,N,R,euc_count)         #mencari pasangan titik terdekat
stop = time.time()                                                  #waktu berhenti  

print()
print("======================================================================================")
print("Pencarian dengan Divide and Conquer:")
print()
print("Pasangan titik terdekat: ")
printPoint(pair[0])                                                 #Menampilkan titik pertama
printPoint(pair[1])                                                 #Menampilkan titik kedua
print("Dengan jarak",d)                                             #Menampilkan jarak kedua titik
print()
print("Terdapat",euc_count, "kali perhitungan euclidean distance")  #Menampilkan berapa kali pemanggilan euclidean distance
print("Waktu eksekusi:", stop-start, "detik")                       #Menampilkan waktu eksekusi

print("Dijalankan di prosesor Intel64 Family 6 Model 78 Stepping 3 GenuineIntel")
print("======================================================================================")

#Pencarian dengan Brute Force
print("Tampilkan Solusi dengan Brute Force? (y/n)")
n=input()
if (n=='y'):
    print("======================================================================================")
    start = time.time()                                             #inisialisasi waktu
    print("Pencarian dengan Brute Force:")
    d2,pair2 = bruteforce(PointList,N,R)                            #Perhitungan dengan brute force
    stop = time.time()                                              #waktu berhenti
    print("Pasangan titik: ")
    printPoint(pair2[0])                                            #Menampilkan titik pertama
    printPoint(pair2[1])                                            #Menampilkan titik kedua
    print("Dengan jarak",d2)                                        #Menampilkan jarak
    print()
    print("Waktu eksekusi: ", stop-start, "detik")                  #Menampilkan waktu
    print("Dijalankan di prosesor Intel64 Family 6 Model 78 Stepping 3 GenuineIntel")
    print("======================================================================================")

if (R == 3):
    print("Tampilkan visualisasi data? (y/n)")
    n=input()
    if (n=='y'):
        show(PointList,pair)
        
print("Terima kasih sudah menggunakan program ini!")


