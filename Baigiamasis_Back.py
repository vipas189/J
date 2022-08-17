def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def tkinter_geometry_center(tkinter, x, y):
    ws = tkinter.winfo_screenwidth()
    hs = tkinter.winfo_screenheight()
    x2 = (ws / 2) - (x / 2)
    y2 = (hs / 2) - (y / 2)
    tkinter.geometry('%dx%d+%d+%d' % (x, y, x2, y2))
