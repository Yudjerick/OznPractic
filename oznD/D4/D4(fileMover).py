import os
import shutil
import subprocess
import time

def moveFiles():
    src = os.getcwd()
    sp = os.listdir(".")

    if not os.path.isdir("OznPractic"):
         os.mkdir("OznPractic")
    os.chdir("OznPractic")
    if not os.path.isdir("blockA"):
        os.mkdir("blockA")
    if not os.path.isdir("blockB"):
        os.mkdir("blockB")

    for i in sp:
        if i[0] == 'A':
            shutil.move(src+"/"+i, src+"/OznPractic/blockA")
        if i[0] == 'B':
            shutil.move(src+"/"+i, src+"/OznPractic/blockB")

    sp = os.listdir(".")
    for i in sp:
        findFunc(i)

def findFunc(file):
    if os.path.isdir(file):
        print('folder "' + file + '":')
        os.chdir(file)
        for j in os.listdir("."):
            findFunc(j)
        os.chdir("..")
        return
    if os.path.splitext(file)[1]!='.py':
        return
    print('>>> script "' + file + '"')
    f = open(file, "rt")
    lines = f.readlines()
    for i in lines:
        if len(i.split()) > 0 and i.split()[0] == "def":
            print('>>> >>> function "' + i[4:-2] + '"')

    startTime = time.time()
    output = subprocess.run(["python",file], capture_output = True, text = True)
    finishTime = time.time()
    print('>>> >>> output "' + output.stdout + '"')
    print('>>> >>> time "' + str(finishTime - startTime) + '"')
    f.close()

moveFiles()