@echo off
echo Installing required modules...
python -m pip install -r install.txt
cd plugins
npm install yargs
cd ..
if %errorlevel%==0 (
    echo Installation successful!
) else (
    echo Installation failed! Please check the error messages above.
)
pause
python run.py