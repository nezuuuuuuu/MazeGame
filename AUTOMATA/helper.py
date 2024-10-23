
array=[
      [  1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
    [  1,      2,      3,      4,      1,      5,      1,      6,      7,      8,      9,     10,     11,      1,     12,     13,      1,     14,     15,      1],
    [  1,     16,      1,     17,      1,     18,      1,     19,      1,      1,      1,      1,     20,      1,     21,      1,     22,     23,     24,      1],
    [  1,     25,      1,     26,     27,     28,     29,     30,      1,     31,     32,      1,     33,      1,     34,     35,     36,      1,     37,      1],
    [  1,     38,      1,      1,      1,      1,      1,     39,      1,     40,      1,      1,     41,      1,      1,      1,     42,      1,     43,      1],
    [  1,     44,     45,     46,     47,     48,     49,     50,      1,     51,     52,     53,     54,     55,     56,     57,     58,     59,     60,      1],
    [  1,     61,      1,      1,      1,      1,      1,      1,     62,      1,      1,     63,      1,      1,      1,      1,     64,      1,     65,      1],
    [  1,     66,      1,     67,      1,      1,      1,     68,     69,     70,      1,     71,      1,      1,      1,      1,     72,      1,      1,      1],
    [  1,     73,      1,     74,     75,     76,     77,     78,      1,     79,     80,     81,      1,      1,      1,      1,      1,     82,      1,      1],
    [  1,     83,      1,     84,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,     85,     86,     87,     88,      1,      1],
    [  1,     89,     90,     91,     92,     93,     94,     95,      1,      1,     96,     97,     98,     99,      1,      1,      1,    100,      1,      1],
    [  1,    101,      1,    102,      1,      1,    103,      1,      1,      1,    104,      1,      1,    105,      1,      1,      1,    106,      1,      1],
    [107,    108,      1,    109,      1,    110,    111,    112,    113,    114,    115,    116,    117,    118,      1,    119,      1,    120,      1,      1],
    [  1,    121,      1,    122,      1,      1,    123,      1,      1,    124,      1,    125,      1,    126,    127,    128,    129,    130,      1,      1],
    [  1,    131,    132,      1,      1,      1,    133,      1,      1,      1,      1,    134,      1,      1,      1,      1,      1,    135,      1,      1],

    [  1,    136,    137,      1,      1,      1,    138,      1,      1,      1,      1,    139,      1,      1,      1,      1,      1,    140,      1,      1],
    [  1,    141,    142,    143,    144,    145,    146,    147,      1,    148,    149,    150,    151,      1,    152,    153,    154,    155,    156,      1],
    [  1,    157,      1,    158,      1,    159,    160,    161,      1,    162,      1,      1,    163,      1,    164,    165,    166,    167,      1,      1],
    [  1,    168,      1,    169,      1,      1,    170,    171,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1,      1],
]


def transition_table_maker():
    for row in range(len(array)):
        for col in range(len(array[row])):
            if(array[row][col]!=1):
                # w
                print('[',end='')

                try:
                    if(array[row-1][col]==1):
                        print(f'{array[row][col]}', end=", ")
                    else:
                        print(f'{array[row-1][col]}', end=", ")
                except IndexError:
                 print(f'{array[row][col]}', end=", ")
                # a
                try:
                    if(array[row][col-1]==1):
                        print(f'{array[row][col]}', end=", ")
                    else:
                        print(f'{array[row][col-1]}', end=", ")
                except IndexError:
                 print(f'{array[row][col]}', end=", ")


                # s
                try:
                    if(array[row+1][col]==1):
                        print(f'{array[row][col]}', end=", ")
                    else:
                        print(f'{array[row+1][col]}', end=", ")
                except IndexError:
                 print(f'{array[row][col]}', end=", ")
                # d
                try:
                    if(array[row][col+1]==1):
                        print(f'{array[row][col]}', end="")
                    else:
                        print(f'{array[row][col+1]}', end="")
                except IndexError:
                    print(f'{array[row][col]}', end="")
                print('],')
            
mydict = {i: f'q{i-2}' for i in range(2, 172)}

# print(mydict)

def state_transition():
    for row in range(len(array)):
            for col in range(len(array[row])):
                if(array[row][col]!=1):
                    # w
                    try:
                        if(array[row-1][col]==1):
                            print(f'(\'{mydict[array[row][col]]}\',\'w\'):\'{mydict[array[row][col]]}\' ', end=", \n")
                        else:
                            print(f'(\'{mydict[array[row][col]]}\',\'w\'):\'{mydict[array[row-1][col]]}\' ', end=", \n")
                        
                    except IndexError:
                        print(f'(\'{mydict[array[row][col]]}\',\'w\'):\'{mydict[array[row][col]]}\' ', end=", \n")

                    # a


                    try:
                        if(array[row][col-1]==1):
                            print(f'(\'{mydict[array[row][col]]}\',\'a\'):\'{mydict[array[row][col]]}\' ', end=", \n")
                        else:
                            print(f'(\'{mydict[array[row][col]]}\',\'a\'):\'{mydict[array[row][col-1]]}\' ', end=", \n")
                        
                    except :
                      print(f'(\'{mydict[array[row][col]]}\',\'a\'):\'{mydict[array[row][col]]}\' ', end=", \n")


                    #   s
                    try:
                        if(array[row+1][col]==1):
                            print(f'(\'{mydict[array[row][col]]}\',\'s\'):\'{mydict[array[row][col]]}\' ', end=", \n")
                        else:
                            print(f'(\'{mydict[array[row][col]]}\',\'s\'):\'{mydict[array[row+1][col]]}\' ', end=", \n")
                        
                    except :
                     print(f'(\'{mydict[array[row][col]]}\',\'s\'):\'{mydict[array[row][col]]}\' ', end=", \n")

                    #   d
                    try:
                        if(array[row][col+1]==1):
                            print(f'(\'{mydict[array[row][col]]}\',\'d\'):\'{mydict[array[row][col]]}\' ', end=", \n")
                        else:
                            print(f'(\'{mydict[array[row][col]]}\',\'d\'):\'{mydict[array[row][col+1]]}\' ', end=", \n")
                        
                    except :
                        print(f'(\'{mydict[array[row][col]]}\',\'d\'):\'{mydict[array[row][col]]}\' ', end=", \n")
        
        
                

def print_states():
    for i in range(2, 172):  
        print(f'\'{mydict[i]}\'',end=', ')
# transition_table_maker()
state_transition()