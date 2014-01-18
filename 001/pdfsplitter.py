# pdfsplitter.py
# 2014 by horst.jens@spielend-programmieren.at
# license: gpl
# about: i have a large master.tex (LaTeX) file for the RIS Journal
# ( http://spielend-programmieren.at/de:ris:001:start )
# and want to create seperate pdfs out of it, one pdf for each article

import os.path

start = "start splitting here\n"
ende = "end{document}" 
sep = "%-----------------------------------------------------------\n"


## load masterfile

file = open("ris001_a4_hochformat.tex")
original = []
for line in file:
    original.append(line)
file.close()
#print(original)

articles = {}
tmplist = []
kopflist = []
interesting = False
for line in original:
    if start in line:
        interesting = True
    if not interesting:
        kopflist.append(line)
        continue
    tmplist.append(line)
    if ende in line:
        print("Ende gefunden")
        break
    if line == sep:
        foundname = False
        for tline in tmplist:
            if "\input{" in tline:
                print("habe namen gefunden!")
                print(tline)
                articlename = tline[tline.find("{")+1:tline.find("/")]
                print("Artikel name:")
                print(">"+articlename+"<")
                articles[articlename] = tmplist
                break
        tmplist = []

#print(articles.keys())
                
# es steht alles in articles drin
# files erzeugen
for a in articles.keys():
    foundinput = False
    file = open("{}_a4_hochformat.tex".format(a), "w")
    for line in kopflist:
        file.write(line)
    print(articles[a])
    for line in articles[a]:
        if "\\newpage" in line and not foundinput:
            continue # Seitenvorschub vor Artikel ist unnötig bei Eizelartikeln
            
        if "\input{" in line:
            foundinput = True
            texfile = open(os.path.join(a,a+".tex"))
            for tline in texfile:
                file.write(tline)
            texfile.close()
            continue # die input line selbst nicht übernehmen
        file.write(line)
    file.write("\\"+ende)
    file.close()


file = open("makepdf.sh","w")        
for a in articles.keys():
    file.write("pdflatex {}.tex\n".format("{}_a4_hochformat".format(a)))
file.close()
                
        
        



