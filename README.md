# variable_declaration_check

Installation:

```shell
pip install pylint
pip install variable-declaration-check
```

Usage:

```shell
pylint --load-plugins=variable_declaration_checker my_python_script.py
```

To disable other checks of pylint:

```shell
pylint --load-plugins=variable_declaration_checker --disable=all --enable=un-declared-variable --enable=re-declared-variable my_python_script.py
```
