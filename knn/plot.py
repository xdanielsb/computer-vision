import matplotlib.pyplot as plt

forms = ['^', 'o', 's', 'p', '*', '+', 'x', '|', 'd', 'h']
colors = ['b','g','','c','r','m','y','k']

def plot(data):
    
    for i in range(0, len(data)):

        x = data[i][:,0]
        y = data[i][:,1]
        print x
        siz= 80
        plt.scatter(x, y, siz, colors[i], forms[i])
    plt.show()
