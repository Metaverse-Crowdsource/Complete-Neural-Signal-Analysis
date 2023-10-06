import os
import shutil
import glob


def create_and_move_files():
    # List all the files with '_requirements.txt' suffix
    requirement_files = glob.glob('*_requirements.txt')

    # Extract prefix names
    prefixes = [filename.split('_requirements.txt')[0] for 
                filename in requirement_files]

    for prefix in prefixes:
        # Create folder with prefix name
        if not os.path.exists(prefix):
            os.mkdir(prefix)

        # Move respective files to the respective folder
        shutil.move(f'{prefix}_requirements.txt', prefix)
        if os.path.exists(f'{prefix}.ipynb'):
            shutil.move(f'{prefix}.ipynb', prefix)


def rename_files_in_folders():
    folders = [dir for dir in os.listdir() if os.path.isdir(dir)]

    for folder in folders:
        os.chdir(folder)
        for file in os.listdir():
            if file.endswith('_requirements.txt'):
                os.rename(file, 'requirements.txt')
        os.chdir('..')


if __name__ == '__main__':
    create_and_move_files()
    rename_files_in_folders()
