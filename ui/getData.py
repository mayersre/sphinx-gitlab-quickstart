'''
Created on 15.04.2019

This Function creates a data structure from which InputPanel creates 
the biggest part of the GUI.

You need four Dictionaries

The first two need exactly the same keys:

verbose_names    Names of your Variables
values           The values assigned to the Variables and used as default

order            Not used, fill with one empty List []
callback_vars    Auto filled by inputPanel, leave empty

You may add or remove Variables, then they will appear/diappear in the GUI
See commented out variables. Unless you write code to process new variables 
nothing will happen to them.

@author: mayers
'''
#
import os
#
import datetime
#
from tkinter import StringVar
#
from etc.settings import GIT_BASE_DIR, TEMPLATE_DIR

def getData():
    '''
    '''
    stringdata = {
        'verbose_names':{
            'path'          :  'The directory name for the new project',
            'sep'           :  'if True, separate source and build dirs',
            'dot'           :  'replacement for dot in _templates etc.',
            'project'       :  'project name',
            'one_line_desc' :  'One line description of Project',
            'project_fn'    :  'Slugged project name for filenames',
            'author'        :  'author names',
            'version'       :  'version of project',
            'release'       :  'release of project',
            'copyright'     :  'Copyright by',
            'language'      :  'document language',
            'suffix'        :  'source file suffix',
            'master'        :  'master document name',
            #'epub'          :  'use epub',
            'now'           :  'Todays date',
            'draft'         :  'Draft Watermark on pages',
            'allgemein'     :  'Path to include files and logos',
            #'autodoc'       :  'enable autodoc extension',
            #'doctest'       :  'enable doctest extension',
            #'intersphinx'   :  'enable intersphinx extension',
            #'todo'          :  'enable todo extension',
            #'coverage'      :  'enable coverage extension',
            #'imgmath'       :  'enable imgmath for pdf, disable mathjax)',
            #'mathjax'       :  'enable mathjax extension',
            #'ifconfig'      :  'enable ifconfig extension',
            #'viewcode'      :  'enable viewcode extension',
            #'githubpages'   :  'enable githubpages extension',

            'BASE_DIR'      :  'Documents base directory',
            
            #'makefile'      :  'Create Makefile',
            #'batchfile'     :  'Create batch command file',
    
            'TEMPLATE_DIR'  :  'Where to find the Document templates (OPTIONAL)',
    
            },
        'values':{
            'path'          :  os.path.join(GIT_BASE_DIR,'my-first-project'),
            'sep'           :  True,
            'dot'           :  '_',
            'project'       :  'My first project',
            'one_line_desc' :  'My first project, Document',
            'project_fn'    :  'my-first-project',
            'author'        :  'Me Myself',
            'version'       :  '0.1',
            'release'       :  datetime.datetime.now().strftime('%B %G'),
            'copyright'     :  datetime.datetime.now().strftime('(C) Me Myself %G'),
            'language'      :  'en',
            'suffix'        :  '.rst',
            'master'        :  'index',
            #'epub'          :  False,
            'now'           :  datetime.datetime.now().strftime('%d. %b %G'),
            'draft'         :  False,
            'allgemein'     :  '.',
            #'autodoc'       :  True,
            #'doctest'       :  False,
            #'intersphinx'   :  True,
            #'todo'          :  False,
            #'coverage'      :  False,
            #'imgmath'       :  False,
            #'mathjax'       :  True,
            #'ifconfig'      :  True,
            #'viewcode'      :  False,
            #'githubpages'   :  False,

            'BASE_DIR'      :  GIT_BASE_DIR,
            
            #'makefile'      :  True,
            #'batchfile'     :  False,
            
            'TEMPLATE_DIR'  :  TEMPLATE_DIR,
            },
        'order':[],
        'callback_vars':{},
        }
    #
    for key in stringdata['verbose_names'] :
        stringdata['callback_vars'][key]=StringVar()
        stringdata['order'].append(key)
        stringdata['callback_vars'][key].set(stringdata['values'][key])
    #
    
    return stringdata
