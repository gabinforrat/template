# Template
Script to create quickly and easily, files needed for a project.

## Use
You'll need to install yaml to use this script.
```sh
pip3 install pyyaml
# or
pip3 install -r requirements.txt
```

To have access to this script everywhere on your Linux machine, add a line in your `~/.bashrc`
```bash
alias template="python3 [SCRIPT_PATH]/touch_template.py"
```

You'll have
```sh
template [FLAG] NAME
```
Create files and directories following a template in the current directory.

A NAME argument indicates which template will be created.

All available FLAG are as follow:
  --help : display this help and exit
  --list : list of all template available, with their name and description
  --gitignore : add a .gitignore file with files already ignored (if available)

## Config
To add or modify templates, add the template files in `template_dir`.
Then modify `config.yaml`, to add your template to the list:
```yaml
template:
  {template name}:
    directory: {name of the template's directory}
    description: {template's description}
    gitignore: {list of files/directory to ignore in git}
```
