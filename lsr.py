def lsr(x, y):
    """
    lsr finds the Least Squares Regression of a data set

    Input:
        Independent variable, x
        Dependent variable, y

    Output:
        Slope of regression line, m
        Y-intercept of regression line, b
        Coefficient of determination, R (R-squared)

    Syntax
        lsr(x,y)
    """
    import numpy as np
    import matplotlib.pyplot as plt
    xs = x**2  # x-squared
    xy = x*y  # xy
    sxy = np.sum(xy)  # Sum of xy
    sx = np.sum(x)  # Sum of x
    sy = np.sum(y)  # Sum of y
    sxs = np.sum(xs)  # Sum of x-squared
    N = len(x)  # Number of points
    m = (N*sxy - sx*sy)/(N*sxs - sx**2)  # Slope
    b = (sy - m*sx)/N  # y-intercept
    ybar = sum(y)/N  # Average y
    eq = m*x + b  # Applied regression line
    SStot = sum((y - ybar)**2)  # Total sum of squares
    SSres = sum((y - eq)**2)  # Sum of squares of residuals
    R = 1 - SSres/SStot  # Coefficient of determination, R-squared
    return m, b, R
