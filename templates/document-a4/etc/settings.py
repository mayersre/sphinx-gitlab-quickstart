'''
General settings for the Sphinx-Gitlab-Quickstart (SGQ) project

(c) Reiner Mayers, 2020
MIT License

The Variables are used in the User interfaces. They should reflect your standard setup

GIT_ROOT in this place the new Project will be created

LIB_DIR  place things here that all projects need

LOGO_DIR here the build will look for the Logos on the Documents

COMMON_DIR maybe mount a common git repository here, currently not used

You need to set in the Environment or in the Gitlab preferences :

SGQ_VERSION
SGQ_MESSAGE

'''
import os, sys
import git

# I usually clone this repo and run the gui from here, so git root is below ...
GIT_ROOT    =   os.path.dirname(  os.path.dirname( os.path.abspath(__file__)  ) )

LIB_DIR     =   os.path.join(GIT_ROOT, 'library')

LOGO_DIR    =   os.path.join(LIB_DIR, 'logos')

COMMON_DIR  =   os.path.join(LIB_DIR, 'common')

SOURCE_DIR  =   os.path.join(GIT_ROOT, 'source')
#
# Create Version and Revision
#
repo = git.Repo(GIT_ROOT)
#
try :
    GIT_VERSION=repo.tags[-1].name
    GIT_MESSAGE=repo.git.tag(n=True).split('\n')[-1]
except IndexError :
    GIT_VERSION = os.environ.get('SGQ_VERSION', 'Initial Version not defined yet')
    GIT_MESSAGE = os.environ.get('SGQ_MESSAGE', 'Initial Message not defined yet')
#
GIT_REVISION=repo.commit().hexsha
