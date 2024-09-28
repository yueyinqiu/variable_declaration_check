$ErrorActionPreference="Stop"

Write-Host "It's going to use:"
pip -V

Write-Host "Enter Anything To Confirm: " -NoNewline
[Console]::ReadLine()

New-Item -Force -Path "./src/dist" -ItemType Directory
New-Item -Force -Path "./src/variable_declaration_checker.egg-info" -ItemType Directory
Remove-Item "./src/dist" -Recurse
Remove-Item "./src/variable_declaration_checker.egg-info" -Recurse

python -m build "./src"

pip uninstall variable_declaration_checker -y
pip install ((Get-Item -Path "./src/dist/*.whl")[0])
