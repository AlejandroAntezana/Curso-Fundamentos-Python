import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    #plt.show()
    plt.savefig('grafico.png')

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    #plt.show()
    plt.savefig('graficoPie.png')

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 100]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)