# Task 2 - Detecting file names, file-input method appearances or fail compiliations.

import os
import logging
import fnmatch 
from datetime import datetime

start_time = datetime.now()
target_folder = r"C:\Users\Admin\Documents\Hashed Folders"
file_name_list = ['bai1.cpp', 'bai2.cpp', 'bai3.cpp', '309A.cpp']

# File logging
logging.basicConfig(
    filename = 'log.txt', 
    filemode = 'w',
    format = '[%(asctime)s] %(message)s', 
    datefmt ='%d/%b/%y %H:%M:%S'
)

# Total file count
total_file_cnt = len([file for root, dir, files in os.walk(target_folder) for file in files if fnmatch.fnmatch(file, '*.cpp')])

def file_name_check():
    error_list = {}
    cur_cnt = 1
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): continue

        participant_name = root.rsplit("\\", 1)[1]
        for file in files:
            print(f"Process 1/3 - Checking file name... ({cur_cnt}/{total_file_cnt})", end = '')
            if file not in file_name_list:
                try:
                    error_list[participant_name].append(file)
                except:
                    error_list[participant_name] = []
                    error_list[participant_name].append(file)
            cur_cnt += 1
            print("\r", end = "") #preventing new line

    print()
    logging.warning(f"There are {len(error_list)} participants with incorrectly named files found.")

    for participant_name in error_list:
        error_msg = f"- {participant_name}: "

        for file in error_list[participant_name]:
            error_msg += f"{file}, "

        error_msg = error_msg[:-2] #Removing the last ,
        logging.warning(error_msg)
def file_opening_check(): 
    error_list = {}
    cur_cnt = 1
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): continue

        participant_name = root.rsplit("\\", 1)[1]

        for file in files:
            print(f"Process 2/3 - Checking file input method... ({cur_cnt}/{total_file_cnt})", end = '')

            file_name = file.rsplit(".", 1)[0]
            with open(f"{root}\{file}", encoding = "utf-8") as f:
                content = f.read()
                if f"{file_name}.inp" not in content:
                    try:
                        error_list[participant_name].append(file)
                    except:
                        error_list[participant_name] = []
                        error_list[participant_name].append(file)
   
            cur_cnt += 1
            print("\r", end = "") #preventing new line

    print()
    logging.warning(f"There are {len(error_list)} participants with files not having file-input method found.")
    for participant_name in error_list:
        error_msg = f"- {participant_name}: "

        for file in error_list[participant_name]:
            error_msg += f"{file}, "

        error_msg = error_msg[:-2] #Removing the last ,
        logging.warning(error_msg)

def compilation_check():
    error_list = {}
    cur_cnt = 1
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): 
            continue

        participant_name = root.rsplit("\\", 1)[1]

        for file in files:
            print(f"Process 3/3 - Compiling files... ({cur_cnt}/{total_file_cnt})", end = '')

            file_name = file.rsplit(".", 1)[0]
            file_dir = f"{root}\{file}"
            os.system(f"g++ -std=c++14 \"{file_dir}\" -o {file_name} 2>tmp.txt")

            with open("tmp.txt", "r") as f:
                if f.read() != "":
                    try:
                        error_list[participant_name].append(file)
                    except:
                        error_list[participant_name] = []
                        error_list[participant_name].append(file)
            
            cur_cnt += 1
            print("\r", end = "") #preventing new line

            try: 
                os.remove(f"{file_name}.exe")
            except: continue


    print()
    logging.warning(f"There are {len(error_list)} participants with failed compilations found.")
    for participant_name in error_list:
        error_msg = f"- {participant_name}: "

        for file in error_list[participant_name]:
            error_msg += f"{file}, "

        error_msg = error_msg[:-2] #Removing the last ,
        logging.warning(error_msg)

file_name_check()
logging.warning("")
file_opening_check()
logging.warning("")
compilation_check()

end_time = datetime.now()
print(f"All processes finished with execution time of {end_time - start_time}")