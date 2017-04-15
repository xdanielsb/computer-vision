import matplotlib.pyplot as plt

forms = ['^', 'o', 's', 'p', '*', '+', 'x', '|', 'd', 'h']
colors = ['b','g','','c','r','m','y','k']

def plot(data, n=1, neighbors=None):
    plt.figure(n)
    for i in range(0, len(data)):

        x = data[i][:,0]
        y = data[i][:,1]
        
        siz= 80
        plt.scatter(x, y, siz, colors[i], forms[i])

    if (neighbors != None):
        plt.plot(x, y)
    plt.show()
