import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def strip(input):
    output = ""
    for c in input:
        if c in "0123456789 /":
            output += c
        if ord(c) == 13:
            output += "#"

    return output

def break_down(input):
    temp = input.split("#")

    #print(temp)

    labels = []
    values = []

    for el in temp:
        print(el)
        if len(el) > 2:
            pairs = el.split()
            labels.append(pairs[0])
            values.append(int(pairs[1]))

    print(f"labels: {labels}")
    print(f"values: {values}")


    xpos = np.arange(len(labels))
    plt.xticks(xpos,labels)
    fig, ax = plt.subplots()
    plt.bar(xpos, values)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    temp = base64.b64encode(buf.getbuffer()).decode("ascii")
    output = f"<img  class='center' width='600px' height='auto' src='data:image/png;base64,{temp}'/>"

    #plt.show()

    return output



'''

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    #plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values, width, label='Total')
   

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Euros')
    ax.set_title('Total Wallet Value chart')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)

    fig.tight_layout()


'''

    