import subprocess
import os

def run_command_in_subdirectories_one_level(command):
    print(f'command:{command}')
    print(f'cwd:{os.getcwd()}')
    for path, dirs, files in os.walk('.'):
        print(f'path {path}')
        print(f'dirs {dirs}')
        for d in dirs:
            print(f'')
            print(f'{d}')
            print(f'Running {command} in {d}')
            os.chdir(d)
            try:
                subprocess.run(command, shell=True, check=True)
            except Exception:
                print(f'Error')
            os.chdir('..')

command = input("Enter the shell command to run: ")
run_command_in_subdirectories_one_level(command)

