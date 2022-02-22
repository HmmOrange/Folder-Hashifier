# Task 1 - Hashifying folder names w/ logs

import os
import shutil
import random
import xlsxwriter #pip install xlsxwriter
from datetime import datetime

start_time = datetime.now()
source_folder = r"C:\Users\Admin\Documents\Participants Code"
destination_folder = r"C:\Users\Admin\Documents\Hashed Folders"

# Duplicating folders
def duplicating():
    print(f"Duplicating folders...")
    try:
        # dirs_exist_ok verifies correct source folder
        shutil.copytree(source_folder, destination_folder, dirs_exist_ok = True)
        # Logging
        print(f"✓ Files & folders copied from {source_folder} to {destination_folder}.")
    except FileNotFoundError:
        print("❌ Error: Source directory provided is incorrect. Please check again.")
        exit(0)

# Hashing folders
def hashing():
    hashed_names_list = []
    folders_dir_list = [] 

    # Creating worksheet for logging
    log_wb = xlsxwriter.Workbook("HashLog.xlsx") 
    log_ws = log_wb.add_worksheet("Sheet 1")

    # Beautifying cells :^)
    cell_format_1 = log_wb.add_format({
        'bold': True,
        'font_color': 'red',
        'align': "center"
    })
    cell_format_2 = log_wb.add_format({
        'align': "center"
    })

    # Writing sheets
    log_ws.write(0, 0, "STT", cell_format_1)
    log_ws.write(0, 1, "SBD", cell_format_1)
    log_ws.write(0, 2, "Phách", cell_format_1)

    row, col = 1, 0

    for subdir in os.listdir(destination_folder):
        f = os.path.join(destination_folder, subdir)
        if os.path.isdir(f):
            folders_dir_list.append(f)
            log_ws.write(row, col, row, cell_format_2)
            log_ws.write(row, col + 1, subdir, cell_format_2)
            row += 1

    
    print(f"Hashing files...")

    # Generating hashed folders' names
    for i in range(1, len(folders_dir_list) + 1):
        hashed_names_list.append("P{0:03d}".format(i))

    random.shuffle(hashed_names_list)

    # Renaming folders
    try:
        row, col = 1, 2
        cur_count = 0
        for dir in folders_dir_list:
            new_name = hashed_names_list[cur_count]
            os.rename(dir, f"{destination_folder}\{new_name}")
            log_ws.write(row, col, new_name, cell_format_2)
            row += 1
            cur_count += 1
        print("✓ Folders hashed successfully.")

        log_wb.close()
        print("✓ Hash log XLSX created successfully.")
    except FileExistsError:
        print("❌ A folder in the destination directory is preventing the hashing procedure. Make sure it's empty before trying again.")
        exit(0)

duplicating()
hashing()


end_time = datetime.now()
print(f"All processes finished with execution time of {end_time - start_time}")
