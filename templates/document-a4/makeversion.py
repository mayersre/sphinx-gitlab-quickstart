'''
Created on 16.04.2019

@author: mayers
'''
import os, sys
import git
import datetime

BUILD_TIME=datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
sys.path.append(lib_path)

from etc.settings import SOURCE_DIR, GIT_REVISION, GIT_VERSION, GIT_MESSAGE



outfile='''

.. Versions-Informationsdatei, wird beim erstellen angelegt
   
   Bitte nicht bearbeiten


Skript Version und Abbildungen
------------------------------

Dieses Skript wird von einem Versionskontrollsystem verwaltet.
Alle Änderungen werden mit Historie gespeichert und sind mit
den folgenden Informationen reproduzierbar:


GIT Version : {}

GIT Version Message   : {}

GIT Revision (hexsha) : {} 

Erstellungsdatum : {}

'''.format(GIT_VERSION,GIT_MESSAGE,GIT_REVISION,BUILD_TIME)

outfile_en='''

.. Version Information file, created when running a script build
   
   Do not manually edit, changes will be lost


Script Version-Information
---------------------------

This script is managed with a sourcecode version control system (git).

All changes are saved with a history and can be reproduced with the
following versioning information :


GIT Version           : {}

GIT Version Message   : {}

GIT Revision (hexsha) : {} 

Build date and time   : {}

'''.format(GIT_VERSION,GIT_MESSAGE,GIT_REVISION,BUILD_TIME)

dst_file=os.path.join(SOURCE_DIR, 'version.rst')

if os.path.exists(dst_file):
    os.remove(dst_file)

{% if values.language ==  'en' %}
with open(dst_file,'w') as file__:
    file__.writelines(outfile_en)
{% else %}
with open(dst_file,'w') as file__:
    file__.writelines(outfile)
{% endif %}
#
#print('\n\n\n',outfile,'\n\n\n')

