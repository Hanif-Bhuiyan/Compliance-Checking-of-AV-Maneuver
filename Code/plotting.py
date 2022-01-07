
import pandas as pd
import matplotlib.pyplot as plt


def result_plotting(av, tv):

    fig, ax = plt.subplots()

    data = pd.read_excel('output.xlsx')

    pos_av_x = av+" positionx"
    pos_av_y = av+" positiony"

    pos_tv_x = tv+" positionx"
    pos_tv_y = tv+" positiony"

    timestamp = data['Time']
    v_1_pos_x = data[pos_av_x]
    v_1_pos_y = data[pos_av_y]
    #v_1_pos_x = data['vehicle-1 positionx']
    #v_1_pos_y = data['vehicle-1 positiony']

    coordinate_1 = []

    for i in range(len(v_1_pos_x)):
        coordinate_1.append([v_1_pos_x[i],v_1_pos_y[i]])


    x_1 = [c[0] for c in coordinate_1]
    y_1 = [c[1] for c in coordinate_1]

    ax.plot(x_1,y_1, label='AV (Automated Vehicle)')


    for i, txt in enumerate(timestamp):

        #if(i % 5 == 0):
            #print(txt)
            #ax.annotate(f'{txt}s', (x_1[i], y_1[i]))
            ax.annotate('|', (x_1[i], y_1[i]))

    v_2_pos_x = data[pos_tv_x]
    v_2_pos_y = data[pos_tv_y]

    #v_2_pos_x = data['vehicle-2 positionx']
    #v_2_pos_y = data['vehicle-2 positiony']

    coordinate_2 = []

    for i in range(len(v_2_pos_x)):
        coordinate_2.append([v_2_pos_x[i],v_2_pos_y[i]])


    x_2 = [c[0] for c in coordinate_2]
    y_2 = [c[1] for c in coordinate_2]

    ax.plot(x_2,y_2, label = 'TV (Target Vehicle)')
    #ax.plot(label = '| = timestamp 0.05s')


    for i, txt in enumerate(timestamp):
        #if(i % 5 == 0):
            #print(txt)
            #ax.annotate(f'{txt}s', (x_2[i], y_2[i]))
            ax.annotate('|',(x_2[i], y_2[i]))

    result = data['Result']
    #ax.plot(result)


    for i, txt in enumerate(result):
        #if(i % 5 == 0):
            #print(txt)
            #ax.annotate(f'{txt}s', (x_2[i], y_2[i]))
            ax.annotate(" "+txt,(x_1[i], y_1[i]))

    #ax.set_xlim(450, 700)
    #ax.set_ylim(1300, 1600)

    #ax.set_ylim([0,1600])

    #plt.xlabel('X Coordinate')
    #plt.xlabel('Y Coordinate')
    plt.xlabel('AV and TV trajectory')
    plt.ylabel('P and F indicates legal and illegal action respectively in every 0.05s (|)')
    plt.title('| = timestamp (0.05s)')
    plt.legend()

    plt.show()

