import os

os.chdir("C:\\Users\\Dell\\Desktop\\Python-Video")

for file in os.listdir():
    f_name, f_ext = os.path.splitext(file)
    f_title, f_code = f_name.split("[")

    f_title, f_code = f_title.strip(), f_code.strip()

    new_name = f"{f_title}{f_ext}"

    os.rename(file, new_name)