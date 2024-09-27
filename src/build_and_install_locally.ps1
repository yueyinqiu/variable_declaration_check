$ErrorActionPreference="Stop"

Write-Host "It's going to use:"
pip -V
Write-Host "At:"
Write-Host (Get-Location)

Write-Host "Enter Anything To Confirm: " -NoNewline
[Console]::ReadLine()

pip install --upgrade setuptools build twine

New-Item -Force -Path "./dist" -ItemType Directory
New-Item -Force -Path "./variable_declaration_checker.egg-info" -ItemType Directory

python -m build

pip uninstall variable_declaration_checker -y
pip install ((Get-Item -Path ./dist/*.whl)[0])