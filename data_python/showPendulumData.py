import numpy as np 
import matplotlib.pyplot as plt 

if __name__=='__main__':
    filename = "Pendulum_train1_x.csv"

    data = np.loadtxt(filename, delimiter=',')
    x1 = data[:,0]
    x2 = data[:,1]
    
    x1 = x1.reshape( int(x1.shape[0]/51), 51)
    x2 = x2.reshape( int(x2.shape[0]/51), 51)

    for j in range(100):
        plt.plot(x1[j,:],x2[j,:])

plt.show()
