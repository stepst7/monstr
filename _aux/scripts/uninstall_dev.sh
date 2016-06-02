#!/bin/bash

# Deactivate current virtualenv
deactivate

git clean -xdn
git clean -xn

#WARNING! To remove ignored files instead of -n use -f. This will remove all uncommitded and unstashed files.
