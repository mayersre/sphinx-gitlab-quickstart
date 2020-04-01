'''
Created on 12.04.2019

Latest version of InputFrame, derived from my Coolprop GUI

@author: mayers
'''
from tkinter import *
import tkinter.ttk as ttk



class InputFrame(LabelFrame):
    '''
    This input frame creates Entries and selects for Variables
    contained in a Dictionary structure
    
    datadict needs at least the three dicts and the list below
    for each one key must be an entry in every dict
    the list order is used for processing
    You can pass a list order with only one field e.g. to init
    and only this field will be processed
     
    datadict={
                'verbose_names':{},
                'values':{},
                'callback_vars':{},
                'order':[],
                }
    
    if a dict units is added to the datadict, the units will be displayed behind the entry widgets
    
    '''
    def __init__(self, parent,cnf={}, title=None,datadict=None,order=None,frameborder=5, InputWidth=60,**kwargs):
        #
        LabelFrame.__init__(self, parent)
        #
        self.InputWidth=InputWidth
        if datadict :
            self.datadict=datadict
        else:
            self.datadict={
                'verbose_names':{},
                'values':{},
                'callback_vars':{},
                'order':[],
                }
        #
        if order :
            self.order=order
        else:
            self.order=self.datadict['order']
        #
        if title :
            self.IFrame = LabelFrame(parent, relief=GROOVE, text=title,bd=frameborder,font=("Arial", 10, "bold"))
        else:
            self.IFrame = LabelFrame(parent, relief=GROOVE,bd=frameborder,font=("Arial", 10, "bold"))
        #
        self.IFrame.grid(row=1,column=1,padx=8,pady=5,sticky=W)
        #
        self.InputPanel(self.IFrame)

    def InputPanel(self, PanelFrame, font=("Arial", 10, "bold")):
        '''
        '''
        #
        order_number=1
        for Dkey in self.order :
            if self.datadict['verbose_names'][Dkey] :
                #
                self.datadict['callback_vars'][Dkey].trace("w", lambda name, index, mode,
                                                         var=self.datadict['callback_vars'][Dkey],
                                                         value=self.datadict['values'][Dkey],
                                                         key=Dkey: self.InputPanelUpdate(var, key, value)
                                                         )
                Label(PanelFrame, text=self.datadict['verbose_names'][Dkey], font=font).grid(column=1, row=order_number, padx=8, pady=5, sticky=W)
                if type(self.datadict['values'][Dkey])==type(True):
                    Checkbutton(PanelFrame, width=self.InputWidth, variable=self.datadict['callback_vars'][Dkey], font=font).grid(column=2, row=order_number, padx=8, pady=5, sticky=W)
                else:
                    Entry(PanelFrame, width=self.InputWidth, textvariable=self.datadict['callback_vars'][Dkey], font=font).grid(column=2, row=order_number, padx=8, pady=5, sticky=W)
                try:
                    Label(PanelFrame, text=self.datadict['units'][Dkey],font=font).grid(column=3, row=order_number,padx=8,pady=5,sticky=W)
                except KeyError :
                    Label(PanelFrame, text='       ',font=font).grid(column=3, row=order_number,padx=8,pady=5,sticky=W)
            else :
                Label(PanelFrame, text=' ', font=font).grid(column=1, row=order_number, padx=8, pady=5, sticky=W)
            #
            order_number+=1

    def InputPanelUpdate(self, tkVar, key, value):
        print(tkVar, key, tkVar.get(),'#')
        #
        if type(self.datadict['values'][key])==type(True):
            # For booleans we misuse a string
            self.datadict['values'][key] = True if tkVar.get()=='1' else False
        elif type(self.datadict['values'][key])==type(1):
            # int
            self.datadict['values'][key] = int(tkVar.getint())
        elif type(self.datadict['values'][key])==type(1.1):
            # float
            self.datadict['values'][key] = float(tkVar.getdouble())
        else:
            # all the rest
            self.datadict['values'][key] = tkVar.get()



