# Task 2 - Detecting file names, file-input method appearances or fail compiliations.

import os

target_folder = r"C:\Users\Admin\Documents\Hashed Folders"
file_name_list = ['bai1.cpp', 'bai2.cpp', 'bai3.cpp', '309A.cpp']

def file_name_check():
    error_list = {}
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): continue
        participant_name = root.rsplit("\\", 1)[1]
        for file in files:
            if file not in file_name_list:
                try:
                    error_list[participant_name].append(file)
                except:
                    error_list[participant_name] = []
                    error_list[participant_name].append(file)

    print(f"There are {len(error_list)} participants with incorrectly named files found.")
    for participant_name in error_list:
        print(f"{participant_name}:", end = " ")
        for file in error_list[participant_name]:
            print(f"{file}", end = ", ")
        print()

def file_opening_check(): 
    error_list = {}
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): continue

        participant_name = root.rsplit("\\", 1)[1]

        for file in files:
            file_name = file.rsplit(".", 1)[0]
            with open(f"{root}\{file}", encoding = "utf-8") as f:
                content = f.read()
                if f"{file_name}.inp" not in content:
                    try:
                        error_list[participant_name].append(file)
                    except:
                        error_list[participant_name] = []
                        error_list[participant_name].append(file)

    print(f"There are {len(error_list)} participants with files not having file-input method found.")
    for participant_name in error_list:
        print(f"{participant_name}:", end = " ")
        for file in error_list[participant_name]:
            print(f"{file}", end = ", ")
        print()

def compilation_check():
    error_list = {}
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): 
            continue

        participant_name = root.rsplit("\\", 1)[1]

        for file in files:
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

            try: 
                os.remove(f"{file_name}.exe")
            except: continue

    print(f"There are {len(error_list)} participants with failed compilations found.")
    for participant_name in error_list:
        print(f"{participant_name}:", end = " ")
        for file in error_list[participant_name]:
            print(f"{file}", end = ", ")
        print()

file_name_check()
print()
file_opening_check()
print()
compilation_check()