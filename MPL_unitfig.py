''' 
Unit figure plot experiment v 0.1
'''
#%%
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import copy



def label(xy, text):
    y = xy[1] + 1.5  # shift y-value for label so that it's below the artist
    plt.text(xy[0], y, text, ha="left", family='sans-serif', size=9)


# # TODO split symbols from values into separate functions for grid (numpy grid? and for drawing)
# maybe returning each block as a collection instead of one?

def symbols_from_values(*inputvalues, art=None, xy=(0, 0), xyspacing=(1.1, 1.1), size=1, unit=10.0, squared=False, gridw=5, blockspacing=1, valuetext=False):
    # from a value or list of values, create a number of horisontally spaced blocks. 
    # spacing between blocks in grid units 
    
    items = []
    blocks = 0

    for val in inputvalues:
        x_start = xy[0] + blocks * (xyspacing[0]*gridw+(1*blockspacing))
        y_start = xy[1]
        if valuetext:
                label((x_start,y_start), str(val))

        unitvalue = float(val)/unit
        x1 = x_start
        y1 = y_start
        for i in range(int(round(unitvalue,0))):
            if art !=None:
                a = copy.copy(art)
            else:
                a = mpatches.Rectangle(xy=([0, 0]), width=size, height=size)
            if i!=0 and i%gridw == 0:
                x1 = x_start
                y1 -= xyspacing[1]

            a.set_xy([x1, y1])        
            x1 += xyspacing[0]
            items.append(a)
        blocks +=1



    return items


