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


GIT_ROOT      =   os.path.dirname(  os.path.dirname( os.path.abspath(__file__)  ) )

GIT_BASE_DIR  = os.path.dirname(GIT_ROOT)

TEMPLATE_DIR  =   os.path.join(GIT_ROOT, 'templates','document-a4')

SOURCE_DIR  =   os.path.join(GIT_ROOT, 'source')
# Link to a nested repo with commons
LIBRARY_URL='git@:github.com/someone/commons.git'
