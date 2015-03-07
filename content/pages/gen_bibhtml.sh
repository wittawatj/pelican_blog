#!/bin/bash

bibtex2html -d -r --nodoc --style abbrvnat \
    --no-keys --no-abstract \
    --named-field pdf "pdf" \
    --note note  \
    --dl --unicode wjpubs.bib
    #--dl --unicode --header "head" --footer "foot" wjpubs.bib

