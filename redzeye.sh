#!/bin/bash
echo "Installing required modules..."
python -m pip install -r install.txt
cd plugins
npm install yargs
cd ..
if [ $? -eq 0 ]; then
    echo "Installation successful!"
else
    echo "Installation failed! Please check the error messages above."
fi
read -p "Press any key to continue... " -n1 -s
echo
python run.py
