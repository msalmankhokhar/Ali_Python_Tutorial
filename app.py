import os
folder_path = 'C:\\Users\Salman Khokhar\\Desktop\\Pics'
list_of_files = os.listdir(folder_path)

for filename in list_of_files:
    index = list_of_files.index(filename)

    extension = os.path.splitext(filename)[1]

    source_path = folder_path + f"\\{filename}"

    destination_path = folder_path + f"\\Image {index + 1}{extension}"

    os.rename(source_path, destination_path)

    print(f"Successfully renamed file number {index+1}")

