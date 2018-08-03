from math import ceil, sqrt

def squared(value):
    return ceil(sqrt(value))


def cm2inch(*tupl):
    """Convert centimeters to inches.
    Args:
        tupl: value or pair of values to convert
    """
    inch = 2.54000508001
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        if len(tupl)==1:
            return tupl[0]/inch
        else:
            return tuple(i/inch for i in tupl)


def make_margins(width, height, margins=None, left=0, right=0, top=0, bottom=0 ):
    """Create Matplotlib margins.
    Args:
        width, height: figure size
        margins: equal margins all around
        left, right, top, bottom: set individual margins
    """
    if margins: 
        left = margins
        right = margins
        top = margins
        bottom = margins

    return {"LM":left/width, "RM": 1-right/width, "BM": bottom/height, "TM": 1-top/height }

def format_with_unit(val, precision=1, suffix="%"):
    d = '{:.{prec}f}{suffix}'.format(val, prec=precision, suffix="%")
    return d


def format_signed_unicode(val, precision=2):
    d = '{:{sign}.{prec}f}'.format(val, sign='+', prec=precision)
    if abs(val) == 0.0: d = d.replace('+', '')
    d = d.replace('-', '−') # unicode minus
    return d