# Task 3 - Detecting code snippet

import os

target_folder = r"C:\Users\Admin\Documents\Hashed Folders"
target_code = {
    "A": "#define int long long",
    "B": "lmao"
}
print("Possible results:")
for participant in target_code:
    print(f"{participant}: ", end = "")
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
                    print(participant_file_name, end = ", ")
                    break 

    print()

