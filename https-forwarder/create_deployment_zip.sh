#!/bin/bash

# Add the python dependencies
cd python_requirements/
zip -r9 ../zip_upload.zip *

# Add project files
cd ..
zip -g zip_upload.zip *.py
