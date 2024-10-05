Write-Host "Installing required modules..."
python -m pip install -r install.txt
cd plugins
npm install yargs
cd ..
if ($LASTEXITCODE -eq 0) {
    Write-Host "Installation successful!"
} else {
    Write-Host "Installation failed! Please check the error messages above."
}
Read-Host -Prompt "Press Enter to continue..."
python run.py