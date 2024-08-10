import os
import sys
import yaml
import shutil


terminal_path = os.path.abspath(os.getcwd())
script_path = os.path.dirname(os.path.abspath(__file__))
with open(f"{script_path}/config.yaml") as file:
    config = yaml.safe_load(file)



def help():
    print("""Usage: template [FLAG] NAME
Create files and directories following a template in the current directory.

A NAME argument indicates which template will be created.

All available FLAG are as follow:
    --help : display this help and exit
    --list : list of all template available, with their name and description
    --gitignore : add a .gitignore file with files already ignored (if available)
    """
    )

def template_list():
    print("List of every template available:")
    for temp in config['template']:
        print('  %(name)-15s : %(description)s' % {'name':temp,'description':config['template'][temp]['description']})

def is_template_valid(template):
    for t in config['template']:
        if t == template:
            return True
    return False

def main():
    if(len(sys.argv)>3):
        raise Exception("Too many argument passed. To see the syntax of the command, use --help")

    is_gitignore = False
    try:
        if(sys.argv[1][:2]=="--"):
            flag = sys.argv[1]
            if(flag=="--help"):
                help()
                return 1
            elif(flag=="--list"):
                template_list()
                return 2
            elif(flag=="--gitignore"):
                is_gitignore = True
                template_option = sys.argv[2]
        else:
            flag = ""
            template_option = sys.argv[1]
    except Exception as e:
        raise Exception("This command requires options. Check with --list to see available template. To see the syntax of the command, use --help")

    if not is_template_valid(template_option):
        raise Exception("This template doesn't exist. Check with --list to see available template")

    template_dir = f"{script_path}{config['src_dir']}"
    template_config = config['template'][template_option]
    template_folder = f"{template_dir}/{template_config['directory']}"

    # https://docs.python.org/3/library/shutil.html
    shutil.copytree(template_folder,terminal_path,dirs_exist_ok=True)

    created_files = []
    original_files = list(os.walk(template_folder))
    count_folder = 0
    for each in original_files:
        if count_folder == 0:
            for sub_dir in each[1]:
                created_files.append(f"{terminal_path}/{sub_dir}")
            for sub_file in each[2]:
                created_files.append(f"{terminal_path}/{sub_file}")
        else:
            for sub_dir in each[1]:
                created_files.append(f"{terminal_path}/{original_files[0][1][count_folder-1]}/{sub_dir}")
            for sub_file in each[2]:
                created_files.append(f"{terminal_path}/{original_files[0][1][count_folder-1]}/{sub_file}")
        count_folder += 1

    for f in created_files:
        os.utime(f)

    if not is_gitignore:
        return 0

    if "gitignore" not in template_config.keys():
        return 0

    try:
        f = open(f"{terminal_path}/.gitignore",'x')
        for ignored_file in template_config['gitignore']:
            f.write(f"{ignored_file}\n")
        f.close()
    except Exception as e:
        raise e
    return 0


if __name__ == "__main__":
    main()
