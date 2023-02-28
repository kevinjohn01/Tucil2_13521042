import matplotlib.pyplot as plt
def show(PointList,pair,dimension):
    if (dimension ==1):
        x =[]
        y=[]
        xa = []
        ya = []
        for point in PointList:
            if(point == pair[0] or point == pair[1]):
                xa.append(point[0])                                     #Assign nilai x untuk pasangan titik terdekat
                ya.append(1)                                     #Assign nilai y untuk pasangan titik terdekat
            else:
                x.append(point[0])                                      #Assign nilai x untuk titik yang lain
                y.append(1)                                      #Assign nilai x untuk titik yang lain
        plt.scatter(x,y)
        plt.scatter(xa,ya)
        plt.show()
    elif (dimension==2):
        x =[]
        y=[]
        xa = []
        ya = []
        for point in PointList:
            if(point == pair[0] or point == pair[1]):
                xa.append(point[0])                                     #Assign nilai x untuk pasangan titik terdekat
                ya.append(point[1])                                     #Assign nilai y untuk pasangan titik terdekat
            else:
                x.append(point[0])                                      #Assign nilai x untuk titik yang lain
                y.append(point[1])                                      #Assign nilai x untuk titik yang lain
        plt.scatter(x,y)
        plt.scatter(xa,ya)
        plt.show()
    elif(dimension==3):
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
        fig = plt.figure(figsize = (50,50))
        ax = plt.axes(projection = "3d")
        ax.scatter3D(x,y,z,color="black")                               #Menampilkan titik lain dengan warna hijau
        ax.scatter3D(xa,ya,za,color = "red")                            #Menampilkan pasangan titik terdekat dengan warna merah
        plt.show()