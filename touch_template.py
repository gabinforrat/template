import os
import sys
import yaml
import shutil
import optparse
from pathlib import Path

TERMINAL_PATH = os.path.abspath(os.getcwd())
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
with open(f"{SCRIPT_PATH}/config.yaml") as file:
    config = yaml.safe_load(file)

def template_list():
    print("List of every template available:")
    for temp in config['template']:
        print('  %(name)-15s : %(description)s' %
            {'name':temp,'description':config['template'][temp]['description']})

def is_template_valid(template):
    for t in config['template']:
        if t == template:
            return True
    return False

def main():
    usage = """%prog [OPTION]... TEMPLATE
Create files and directories following a TEMPLATE in the current directory.
"""
    parser = optparse.OptionParser(usage)

    parser.add_option("-p","--path", action="store", type="string",
        dest="output_path", default="", help="path to create the template at")
    parser.add_option("-l","--list", action="store_true",
        dest="is_show_list", default=False,
        help="list of all template available, with their name and description")
    parser.add_option("-g","--gitignore", action="store_true",
        dest="is_gitignore", default=False,
        help="add a .gitignore file with files already ignored (if available)")

    (options, args) = parser.parse_args()

    if options.is_show_list:
        template_list()
        return 1

    if len(args) <  1:
        raise Exception("This command requires options. Check with --list to see"
            + "available template. To see the syntax of the command, use --help")
    elif len(args) > 1:
        print("Error: Too many arguments")
    elif not is_template_valid(args[0]):
        raise Exception("This template doesn't exist. Check with --list to see"
            +"available template")


    path_to_output = os.path.abspath(Path(options.output_path))
    print(f"path_to_output: {path_to_output}")
    template_config = config['template'][args[0]]
    template_folder = f"{SCRIPT_PATH}{config['src_dir']}/{template_config['directory']}"

    shutil.copytree(template_folder,path_to_output,dirs_exist_ok=True)

    created_files = []
    original_files = list(os.walk(template_folder))

    absolute_path = original_files[0][0]
    for each in original_files:
        relative_path = each[0].replace(absolute_path,"")
        for sub_dir in each[1]:
            created_files.append(f"{path_to_output}{relative_path}/{sub_dir}")
        for sub_file in each[2]:
            created_files.append(f"{path_to_output}{relative_path}/{sub_file}")

    for file in created_files:
        os.utime(file)

    if not options.is_gitignore:
        return 0

    if "gitignore" not in template_config.keys():
        return 0

    try:
        file = open(f"{path_to_output}/.gitignore",'x')
        for ignored_file in template_config['gitignore']:
            file.write(f"{ignored_file}\n")
        file.close()
    except Exception as e:
        raise e
    return 0


if __name__ == "__main__":
    main()
