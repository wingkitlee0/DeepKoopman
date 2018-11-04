import numpy as np 
import scipy.integrate




def PendulumFn(x1range, x2range, numICs, tSpan, seed, max_potential):
    np.random.seed(seed)

    lenT = tSpan.shape[0]

    X = np.zeros((numICs*lenT, 2))

    def potential(x,y):
        return 0.5*y**2 - np.cos(x)

    def func(x, t):
        dxdt = np.zeros((2,))
        dxdt[0] = x[1]
        dxdt[1] = -np.sin(x[0])
        return dxdt

    count = 0
    while (count < numICs):
        x1 = (x1range[1]-x1range[0])*np.random.random() + x1range[0]
        x2 = (x2range[1]-x2range[0])*np.random.random() + x2range[0]
        ic = [x1, x2]

        pot = potential(x1, x2)
        if pot <= max_potential:
            print("x1, x2, pot = ", x1, x2, pot)

            # x(t)
            xx = scipy.integrate.odeint(func, y0=ic, t=tSpan)

            X[count*lenT:count*lenT+lenT, :] = xx 
            count += 1
    
    print(count)
    return X

if __name__=='__main__':
    tSpan = np.linspace(0.0, 1.0, 10)
    seed = 1234
    max_potential = -0.9
    X = PendulumFn([-0.5, 0.5], [-0.5, 0.5], 100, tSpan, seed, max_potential)

    np.savetxt("test.dat", X)

