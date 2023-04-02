import array
import os
import subprocess

def run_command_in_subdirectories_one_level(command):
    print(f'command : {command}')
    if command.startswith('rm'):
        print(f'Invalid command (rm): {command}')
        quit()

    working_dir = os.getcwd()
    print(f'cwd : {working_dir}')
    dirs = list()
    for file in os.listdir(working_dir):
        if (os.path.isdir(os.path.join(working_dir, file))):
            dirs.append(file)

    dirs.sort()
    for subdir in dirs:
        print(f'\n===================================================')
        print(f'{subdir} : {command}\n')
        os.chdir(subdir)
        try:
            subprocess.run(command, shell=True, check=True)
        except Exception:
            print(f'Error')
        os.chdir('..')

command = input("Enter the shell command to run: ")
run_command_in_subdirectories_one_level(command)

