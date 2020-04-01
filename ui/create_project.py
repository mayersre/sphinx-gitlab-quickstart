'''
Created on 15.04.2019

@author: mayers
'''
#
import os, shutil,sys
#
lib_path = os.path.dirname(  os.path.dirname( os.path.abspath(__file__)  ) )
sys.path.append(lib_path)

print (lib_path)

from etc.settings import GIT_ROOT, SOURCE_DIR, GIT_BASE_DIR, TEMPLATE_DIR, LIBRARY_URL

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk
#
from tkinter.simpledialog import Dialog
#
import git
#
from ui.inputpanels import InputFrame
from ui.getData import getData
#
from django.template.defaultfilters import slugify
#
from jinja2 import Template
#
import datetime
#
from six import text_type
from docutils.utils import column_width
#
class SpInputFrame(InputFrame):
    '''
    Add local functions to InputPanelUpdate
    '''
    def InputPanelUpdate(self, tkVar, key, value):
        #print(tkVar, key, tkVar.get(),'#')
        #
        if type(self.datadict['values'][key])==type(True):
            self.datadict['values'][key] = True if tkVar.get()=='1' else False
        else:
            self.datadict['values'][key] = tkVar.get()
            if key=='project':
                self.datadict['values']['project_fn']=slugify(self.datadict['values'][key])
                self.datadict['callback_vars']['project_fn'].set(self.datadict['values']['project_fn'])

class gui_startpanel(Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent, title=None, data=None):
        '''
        Constructor
        '''
        self.parent=parent
        self.data=data
        #
        self.Row1Frame = LabelFrame(parent, relief=GROOVE, text=' 1.) Enter project name',bd=5,font=("Arial", 10, "bold"))
        self.Row1Frame.grid(row=1,column=1,padx=8,pady=5,sticky=W+E, columnspan=3)
        #
        self.Row2Frame = LabelFrame(parent, relief=GROOVE, text=' 2.) Choose base directory and template directory' ,bd=5,font=("Arial", 10, "bold"))
        self.Row2Frame.grid(row=2,column=1,padx=8,pady=5,sticky=W+E, columnspan=3 )
        #
        self.Row3Frame = LabelFrame(parent, relief=GROOVE, text=' 3.) Enter main parameters',bd=5,font=("Arial", 10, "bold"))
        self.Row3Frame.grid(row=3,column=1,padx=8,pady=5,sticky=W)
        #
        self.Row4Frame = LabelFrame(parent, relief=GROOVE, text=' 4.) Run quickstart',bd=5,font=("Arial", 10, "bold"))
        self.Row4Frame.grid(row=4,column=1,padx=8,pady=5,sticky=W)
        #
        self.Row1IFrame=SpInputFrame(self.Row1Frame, title='Project Name',datadict=self.data,order=['project'])
        #
        self.b2=Button(self.Row2Frame,text="Choose location for project directory")
        self.b2.grid(row=1,column=1,padx=8,pady=5,stick=W+E, columnspan=3)     
        self.b2.bind("<ButtonRelease-1>", self.Button_2_Click)
        #
        self.b2a=Button(self.Row2Frame,text="Choose location of template files")
        self.b2a.grid(row=2,column=1,padx=8,pady=5,stick=W+E, columnspan=3)     
        self.b2a.bind("<ButtonRelease-1>", self.Button_2a_Click)
        #
        self.Row3IFrame=SpInputFrame(self.Row3Frame, title='Main configuration',datadict=self.data)
        #
        self.b4=Button(self.Row4Frame,text="Run this configuration and build the project from templates")
        self.b4.grid(row=1,column=1,padx=8,pady=5,stick=W+E, columnspan=3)     
        self.b4.bind("<ButtonRelease-1>", self.runQuickstart)
        #

    def Button_2_Click(self,event): 
        '''
        '''
        START_DIR = os.path.dirname(os.path.abspath(__file__) )
        #
        BASE_DIR = filedialog.askdirectory(parent=self.parent, initialdir=GIT_BASE_DIR ,title="Choose base directory")
        self.data['values']['BASE_DIR']=GIT_BASE_DIR
        self.data['callback_vars']['BASE_DIR'].set(self.data['values']['BASE_DIR'])
        #
        self.data['values']['path']=os.path.join(BASE_DIR,self.data['values']['project_fn'])
        self.data['callback_vars']['path'].set(self.data['values']['path'])
        #
    def Button_2a_Click(self,event): 
        '''
        '''
        START_DIR = os.path.dirname(os.path.abspath(__file__) )
        #
        LOCAL_TEMPLATE_DIR = filedialog.askdirectory(parent=self.parent, initialdir=TEMPLATE_DIR ,title="Choose Templatedirectory")
        #
        self.data['values']['TEMPLATE_DIR']=LOCAL_TEMPLATE_DIR
        self.data['callback_vars']['TEMPLATE_DIR'].set(self.data['values']['TEMPLATE_DIR'])
        #
        
    def runQuickstart(self,event):
        '''
        run template build with gathered information
        '''
        #
        self.data['values']['project_underline'] = column_width(self.data['values']['project']) * '='
        #
        if self.data['values']['path']=='.' :
            print('path is not configured')
        else :
            if not os.path.exists(self.data['values']['path']):
                os.makedirs(self.data['values']['path'])
            #
            root_src_dir = self.data['values']['TEMPLATE_DIR']
            root_dst_dir = self.data['values']['path']
            #
            for src_dir, dirs, files in os.walk(self.data['values']['TEMPLATE_DIR']):
                #print(src_dir, dirs, files)
                dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                    if dst_dir.split('/')[-1]=='source':
                        pass
                        # create link from library
                        #dst_link=os.path.join(dst_dir,'library')
                        #src_link=os.path.join(self.data['values']['BASE_DIR'],'library')
                        #print('creating link from {} to {} '.format(src_link,dst_link))
                        #os.symlink(src_link, dst_link)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    indexfile=True
                    if os.path.exists(dst_file):
                        if file_ == 'index.rst':
                            indexfile=False
                        else:
                            print('Deleting : ', dst_file)
                            os.remove(dst_file)
                    if file_ in ['.gitignore',]:
                        if os.path.exists(dst_file):
                            pass
                        else:
                            shutil.copy(src_file, dst_dir)
                    else :
                        if file_ == 'index.rst' and not indexfile:
                            pass
                        else:
                            if file_.endswith('.py') or file_.endswith('.rst') or file_.endswith('.sh') or file_=='Makefile':
                                print('Templating : ', dst_file)
                                with open(src_file) as file_:
                                    template = Template(file_.read())
                                output=template.render(self.data)
                                #
                                with open(dst_file,'w') as file__:
                                    file__.writelines(output)
                            else :
                                print('Copying : ', dst_file)
                                shutil.copy(src_file, dst_dir)
                            #
        print('Init of git repo')
        #
        repo = git.Repo.init(self.data['values']['path'])
        repo.git.add(A=True)
        repo.git.commit('-m','Initial creation by startpanel')
        print('Finished runQuickstart',self.data['values']['path'])
        runonce='''
#!/bin/bash
#
# Run this once if you have a repository for common before you push the directory
# 
cd {}
git submodule add  {} library/common

git submodule init
git submodule update

#
echo "if you need a fresh copy do a   git pull   in the library/common directory"
#
'''.format(self.data['values']['path'],LIBRARY_URL)
        #
        dst_file=os.path.join(self.data['values']['path'], 'run_me_once.sh')
        if os.path.exists(dst_file):
            os.remove(dst_file)
        with open(dst_file,'w') as file__:
            file__.writelines(runonce)

class GUI_Dialog:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        dummyvar = gui_startpanel(master,data=getData())



def gui_main():
    root = Tk() 
    app = GUI_Dialog(root)
    root.mainloop()

def tui_main():
    from ui.tui_curses import TUI_Dialog
    TUI_Dialog()
    print('using urwid/curses')

def X_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0

if __name__ == '__main__':
    if X_is_running():
        gui_main()
    else:
        tui_main()
