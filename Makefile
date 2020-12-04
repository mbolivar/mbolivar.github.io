SPHINXOPTS    ?= -jauto
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help html deploy

# $(O) allows easily extending $(SPHINXOPTS).

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

deploy:
	python3 deploy.py
