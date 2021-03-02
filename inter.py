def inter(x, X, Y):
    """
    Inter performs linear interpolation between two (2) (x,y) coordinate pairs.

    Input:
       Vector containing independent coordinates, X
       Vector containing dependent coordinates, Y
       Independent location between X(0) and X(1), x

    Output:
        Location of y(x) between coordinate pair (X,Y)

    Syntax:
        inter(x, X, Y)
    """
    m = (Y[1] - Y[0])/(X[1] - X[0])  # Slope
    y = Y[0] + (x - X[0])*m  # Solve for unknown 'y'
    return y
