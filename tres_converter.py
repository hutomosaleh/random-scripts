import os

# For remaking .tres file with different png path
# Great for reusing texture tres files, for game cosmetics

folder_path = 'Testing stuff'
file_list = os.listdir(folder_path)
sprite_sheet_path = "res://Assets/Player/Hair/Boy/1/boy_hair_1.png"
text_replacement = f'[ext_resource path="{sprite_sheet_path}" type="Texture" id=1]\n'

for file in file_list:
    if file.split(".")[-1] == "tres":
        new_file_name = file[1:]
        with open(f"{directory}/{new_file_name}", "w") as new_file:
            with open(f"{directory}/{file}", 'r') as original_file:
                for index, line in enumerate(original_file.readlines()):
                    if index == 2:
                        new_file.write(text_replacement)
                    else:
                        new_file.write(line)
