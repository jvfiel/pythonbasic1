from Tkinter import *

def fill(lstbox,listdic):
    #print listdic
    for dic in listdic:
        # for key in dic:
        #print dic['item'], dic['price']
        lstbox.insert(END, '{0}: {1}'.format(dic['item'], dic['price']))