def trapz(x, y):
    # Trapezoidal method of discrete integration
    import numpy as np
    t = np.zeros([len(x), 1])
    for i in range(1, len(x)):
        dx = x[i] - x[i-1]
        t[i] = (y[i-1] + y[i])*dx/2
    area = sum(t)
    return area

