import array
import os
import subprocess

def run_command_in_subdirectories_one_level(command):
    print(f'cwd : {os.getcwd()}')
    print(f'command : {command}')
    root = os.getcwd()
    dirs = list()
    for file in os.listdir(root):
        if (os.path.isdir(os.path.join(root, file))):
            dirs.append(file)

    dirs.sort()
    for subdir in dirs:
        print(f'\n========================================')
        print(f'{subdir} : {command}')
        os.chdir(subdir)
        try:
            subprocess.run(command, shell=True, check=True)
        except Exception:
            print(f'Error')
        os.chdir('..')

command = input("Enter the shell command to run: ")
run_command_in_subdirectories_one_level(command)

