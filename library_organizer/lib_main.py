import os
import glob

__input__path = r'E:\Education' #your local path to root folder for education and science
__input__included_extensions = '.djvu, .fb2, .pdf'

def main():
    print("Hello, mr. Sniper\n")
    searching_extension = '.ini'
    get_files_with_extension(__input__path, searching_extension)
    print()
    get_files_from_folder(__input__path)

def get_files_from_folder(directory):
    "Returns files in the dir"
    arr = []
    incl_extensions = get_incl_extensions(__input__included_extensions)

    for file in glob.glob(f"{directory}/*.*"):
        file_fullname, file_extension = os.path.splitext(file)
        for incl_extension in incl_extensions:
            if(file_extension == incl_extension):
                print(file)
                arr.append(file)

def get_incl_extensions(incl_extensions):
    result = incl_extensions.split(", ")
    return result

def get_files_with_extension(directory, ext):
    "Returns files in the dir with an extension"
    arr = []
    exit = True
    incl_extensions = get_incl_extensions(__input__included_extensions)
    for x in incl_extensions:
        if (x == ext):
            exit = False
    if(exit):
        return
    for name in glob.glob(f"{directory}/*{ext}"):
        print(name)
        arr.append(name)
