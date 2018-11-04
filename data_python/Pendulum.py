import numpy as np 
from PendulumFn import PendulumFn

if __name__=='__main__':
    numICs = 5000
    filenamePrefix = 'Pendulum';

    x1range = [-3.1,3.1]
    x2range = [-2, 2]
    tSpan = np.linspace(0.0, 1.0, 51)

    max_potential = .99

    seed = 1
    X_test = PendulumFn(x1range, x2range, round(.1*numICs), tSpan, seed, max_potential)
    filename_test = filenamePrefix + '_test_x.csv'
    np.savetxt(filename_test, X_test, fmt='%.14f', delimiter=',', )

    seed = 2
    X_val = PendulumFn(x1range, x2range, round(.2*numICs), tSpan, seed, max_potential);
    filename_val = filenamePrefix + '_val_x.csv'
    np.savetxt(filename_val, X_val, fmt='%.14f', delimiter=',', )


    for j in range(1,7):
        seed = 2+j
        X_train = PendulumFn(x1range, x2range, round(.7*numICs), tSpan, seed, max_potential);
        filename_train = filenamePrefix + '_train%d_x.csv' % j
        np.savetxt(filename_train, X_train, fmt='%.14f', delimiter=',', )

        print(X_train.shape)
        