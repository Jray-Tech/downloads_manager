import os
import shutil
from _datetime import datetime
print(os.getcwd())
main_dir = 'C:/Users/Ayomide/Downloads'
copy_dir = 'C:/Users/Ayomide/Desktop/CleanDownloads'
os.chdir(main_dir)
print(os.getcwd())
base_files = ['Movies', 'Music', 'Others', 'Text', 'Zip', 'Pictures', 'Files']
# check if the copy dir exist if it doesnt make it!
if not os.path.exists(copy_dir):
    print('doesnt exist')
    os.makedirs(copy_dir)
else:
    print('file path already exists do not worry man!!')

# a full list of the files type and what they mean!
linked_list = {
    'movie': ['.mp4'],
    'code': ['.html', '.py', '.js', '.css', '.whl'],
    'zip': ['.zip', '.gz'],
    'images': ['.jpg', '.png'],
    'executable': ['.exe', '.msi'],
    'music': ['.mp3']
}
# returned_code = shutil.move('first_folder', 'C:/Users/Ayomide/Desktop/Play/move_here')
# print(returned_code)
# for parsing th time the files were created... try to read the code
months = ['Jan', 'Feb', 'Mar', 'Apr', 'may', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
# checking the full list in the main path...
#

for directory in os.listdir():
    # checking if it is a file or if it is a directory... for here it checks for dir first
    time_created = os.stat(directory).st_ctime
    file_size = os.stat(directory).st_size
    time_created = datetime.fromtimestamp(time_created)
    # splitting function to get the values of year month and day.
    time_created_string = str(time_created)
    split_time_created_string = time_created_string.split('-')
    year = split_time_created_string[0]
    month = split_time_created_string[1]
    month = int(month) - 1
    actual_month = months[month]
    if os.path.isdir(directory):
        # check if the directory where the file should be moved exists on filesystem
        # use join to join them for checking ...
        # if it exist move th =e file if not create, then move!
        file_should_be_stored = os.path.join(copy_dir, 'Files', year, actual_month, directory)
        # i leaned i need to have a dir that doesnt exist...
        # to copy a file i created a dir that doesnt exist and if the dir exist that means i hv copied there already!
        # condition runs only if the directory does not exist!
        if not os.path.exists(file_should_be_stored):
            # exists already
            print(directory)
            try:
                returned_code = shutil.copytree(directory, file_should_be_stored)
                print(returned_code)
            except PermissionError:
                print('IT Didint work gave a permission error')
    else: # for conditional u can just check if isFILE IN CASE OF ERRORS
        (_dir_, ext) = os.path.splitext(directory)
        # checks if the file given is part of the expected files in my linked_list
        if ext in linked_list['movie']:
            # move code here ....copy. lol
            # also create the file to be copied to and check for existence first!
            movie_file_ = os.path.join(copy_dir, 'Movies', year, actual_month, directory)
            move_movie_file_here = os.path.join(copy_dir, 'Movies', year, actual_month)
            # check if file exists ? create if it doesnt .... move file
            if not os.path.exists(movie_file_):
                print('exists')
                # store file only if file doesnt already exist....]
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_movie_file_here)
                    shutil.copy2(directory, move_movie_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_movie_file_here)
        elif ext in linked_list['executable']:
            exe_file_ = os.path.join(copy_dir, 'Executables', year, actual_month, directory)
            move_exe_file_here = os.path.join(copy_dir, 'Executables', year, actual_month)
            if not os.path.exists(exe_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_exe_file_here)
                    shutil.copy2(directory, move_exe_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_exe_file_here)
        elif ext in linked_list['code']:
            code_file_ = os.path.join(copy_dir, 'Code', year, actual_month, directory)
            move_code_file_here = os.path.join(copy_dir, 'Code', year, actual_month)
            if not os.path.exists(code_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_code_file_here)
                    shutil.copy2(directory, move_code_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_code_file_here)
        elif ext in linked_list['zip']:
            zip_file_ = os.path.join(copy_dir, 'Compressed', year, actual_month, directory)
            move_zip_file_here = os.path.join(copy_dir, 'Compressed', year, actual_month)
            if not os.path.exists(zip_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_zip_file_here)
                    shutil.copy2(directory, move_zip_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_zip_file_here)
        elif ext in linked_list['images']:
            images_file_ = os.path.join(copy_dir, 'Pictures', year, actual_month, directory)
            move_images_file_here = os.path.join(copy_dir, 'Pictures', year, actual_month)
            if not os.path.exists(images_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_images_file_here)
                    shutil.copy2(directory, move_images_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_images_file_here)
        elif ext in linked_list['music']:
            music_file_ = os.path.join(copy_dir, 'Music', year, actual_month, directory)
            move_music_file_here = os.path.join(copy_dir, 'Music', year, actual_month)
            if not os.path.exists(music_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_music_file_here)
                    shutil.copy2(directory, move_music_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_music_file_here)
        else:
            others_file_ = os.path.join(copy_dir, 'Others', year, actual_month, directory)
            move_others_file_here = os.path.join(copy_dir, 'Others', year, actual_month)
            if not os.path.exists(others_file_):
                print('exists')
                try: # try to make the directory... except it already exists.. then in both cases just add the file
                    os.makedirs(move_others_file_here)
                    shutil.copy2(directory, move_others_file_here)
                except OSError:
                    print('directory already exists .....')
                    shutil.copy2(directory, move_others_file_here)

# check for file.... done
# check for diredctory ... .done
# if directory, do the moving..... follow steps below! ....use a copy code to copy your code!...done
# if file... check the type of file.....done
# check the date modified... done
# create a dictionary or some variables... done
# check if a directory already exists based on the naing convention it should have... done
# if it exists... then move the file inside it.... done
# else
# use this to create a directory they should be on... done
# move the files in... done
# finally, do something similar for the directories on the machine... done
# finally make classes... done



# PROPOSED NAMING CONVENTION
# Directory of Photos, Videos, Music, Text, Other, Zip files
# Sub directories of year taken or modified or whatever
# Sub directrory of the month it ws taken in or something ... .have fun ... with code
# always have it copy all files first to another location or just use the copty key
# files that do not mathc should always have an otherws place