if __name__ == "__main__":
    """ from math import cos
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

    DIM = 50

    X = [-DIM+i for i in range(2*DIM)]
    Y = [-DIM+i for i in range(2*DIM)]
    Z = [[1 for i in range(2*DIM)] for j in range(2*DIM)]
    for i in range(2*DIM):
        for j in range(2*DIM):
            Z[i][j] += cos(X[i] ** 2 + Y[j] ** 2)

    X, Y = np.meshgrid (X,Y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, np.array(Z), cmap='viridis', edgecolor='none')
    ax.set_title('Surface plot')
    plt.show()

    print (X)
    print (Y)
    print (np.array(Z)) """