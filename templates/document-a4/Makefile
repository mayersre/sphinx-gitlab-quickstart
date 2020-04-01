# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -j auto -q
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = {{ values.project_fn }}
SOURCEDIR     = source
BUILDDIR      = build
HTDIR         = htdocs
HTFILES		  = $(BUILDDIR)/html/
SINGLEDIR     = $(BUILDDIR)/singlehtml
DEPLOYDIR     = /home/gitlab-runner/public/$(SPHINXPROJ)

export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

DATE := $(shell date)
USER := $(shell whoami)
TAG  := $(shell git tag)

GITVERSION := $(BFS_VERSION)
GITMESSAGE := $(BFS_MESSAGE)




all :
	echo "GITVERSION = $(GITVERSION)"
	echo "GITMESSAGE = $(GITMESSAGE)"
	echo "TAG = $(TAG)"
	make version pdf compresspdf copypdf singlehtml docx copydocx html copyhtml

ifeq "$(strip $(USER))"  "gitlab-runner"
deploy:
	rm -rf $(DEPLOYDIR)
	mkdir -p $(DEPLOYDIR)
	mv $(HTFILES)/* $(DEPLOYDIR)/
	echo "Deployed to local apache server"
else
deploy:
	echo "__$(USER)__ is not gitlab-runner, so no deployment"
endif

copypdf:
	cp build/latex/$(SPHINXPROJ).pdf source/$(SPHINXPROJ).pdf
	cp build/latex/$(SPHINXPROJ).pdf public/$(SPHINXPROJ).pdf

copydocx:
	cp build/singlehtml/index.docx source/$(SPHINXPROJ).docx
	cp build/singlehtml/index.docx public/$(SPHINXPROJ).docx

copyhtml:
	cp -r build/html/ public/

nopublic:
	rm -rf public/*

pdf:
	sphinx-build -M latexpdf  source build  -c source/pdf_conf

compresspdf:
	mv build/latex/$(SPHINXPROJ).pdf build/latex/$(SPHINXPROJ)-big.pdf
	ps2pdf build/latex/$(SPHINXPROJ)-big.pdf build/latex/$(SPHINXPROJ).pdf
	#rm build/latex/$(SPHINXPROJ)-big.pdf

version:
	echo $(USER)
	python makeversion.py
	
docx:
	cd build/singlehtml && pandoc -o index.docx index.html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

htdocs:
	rsync -rupE "$(HTFILES)" "$(HTDIR)"
	
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



	