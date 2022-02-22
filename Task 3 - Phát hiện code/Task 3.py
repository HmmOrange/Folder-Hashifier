# Task 3 - Detecting code snippet

import os
import logging
from datetime import datetime

start_time = datetime.now()
target_folder = r"C:\Users\Admin\Documents\Hashed Folders"
target_code = {
    "A": "#define int long long",
    "B": "lmao"
}

# File logging
logging.basicConfig(
    filename = 'log.txt', 
    filemode = 'w',
    format = '[%(asctime)s] %(message)s', 
    datefmt ='%d/%b/%y %H:%M:%S'
)

logging.warning("Possible results:")
for participant in target_code:
    msg = f"{participant}: "
    code_snippet = target_code[participant]
    for root, dir, files in os.walk(target_folder):
        # root == target_folder
        if target_folder.endswith(root): continue

        participant_file_name = root.rsplit("\\", 1)[1]

        for file in files:
            #file_name = file.rsplit(".", 1)[0]
            with open(f"{root}\{file}", encoding = "utf-8") as f:
                content = f.read()
                if code_snippet in content:
                    msg += f"{participant_file_name}, "
                    break 
        
    if msg[-2:] == ", ": msg = msg[:-2]
    logging.warning(msg)

print("✓ Results logged in log.txt")

end_time = datetime.now()
print(f"All processes finished with execution time of {end_time - start_time}")