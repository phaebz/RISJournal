# pdfsplitter.py
# 2014 by horst.jens@spielend-programmieren.at
# license: gpl
# about: i have many tex files and want epubs, one for each article
# using pandoc

import os
import os.path
import subprocess 
myfiles = []
#files = os.walk()
for root, dirs, files in os.walk("."):
    for filename in files:
        if "a4_hochformat.tex" in filename:
            myfiles.append(filename)
            
    break
print(myfiles)
print("working")
for filename in myfiles:
    pos = filename.find("_a4_hochformat")
    vorname = filename[:pos]
    print("making epub of "+vorname)
    subprocess.call(["pandoc",filename, "-o", vorname+".epub"])


    
