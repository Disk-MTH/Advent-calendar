import glob
import os
import shutil


def getAllresourcesPath():
    path1 = "..\\diskmth\\resources\\*.*"
    path2 = "..\\diskmth\\resources\\*\\*.*"
    path3 = "..\\diskmth\\resources\\*\\*\\*.*"
    filesPath = []
    for i in glob.glob(path1):
        filesPath.append(os.path.abspath(i))
    for i in glob.glob(path2):
        filesPath.append(os.path.abspath(i))
    for i in glob.glob(path3):
        filesPath.append(os.path.abspath(i))
    return filesPath

def getFullCommand():
    resourcesList = getAllresourcesPath()
    command = "pyinstaller --onefile --windowed --clean"

    if os.path.exists("..\\diskmth\\resources\\icons\\app_icon.ico"):
        command = command + " --icon \"" + os.path.abspath("..\\diskmth\\resources\\icons\\app_icon.ico").replace("\\", "/") + "\""

    for i in range(len(resourcesList)):
        command = command + " --add-data \"" + resourcesList[i].replace("\\", "/") + ";.\""

    command = command +  " --collect-data \"pygame\""
    command = command + " \"" + os.path.abspath("..\\diskmth\\Main.py") + "\""
    return command

if __name__ == '__main__':
    try:
        os.chdir("..\\env\\Scripts\\")
    except FileNotFoundError:
        pass
    os.system("activate")
    os.chdir("..\\..")
    try:
        os.mkdir("build")
    except FileExistsError:
        shutil.rmtree("build")
        os.mkdir("build")
    os.chdir("build")
    os.system(getFullCommand())
    os.system("pause")