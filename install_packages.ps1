$ErrorActionPreference="Stop"

Write-Host "It's going to use:"
pip -V

Write-Host "Enter Anything To Confirm: " -NoNewline
[Console]::ReadLine()

pip install --upgrade setuptools build twine
pip install --upgrade pylint