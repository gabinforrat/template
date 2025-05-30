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

## Help
```
Usage: template [OPTION]... TEMPLATE
Create files and directories following a TEMPLATE in the current directory.

Options:
  -h, --help            show this help message and exit
  -p OUTPUT_PATH, --path=OUTPUT_PATH
                        path to create the template at
  -l, --list            list of all template available, with their name and
                        description
  -g, --gitignore       add a .gitignore file with files already ignored (if
                        available)
```



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

# Version
1.2.1
