import pandas as pd
import subprocess
import os

excelFile = "People.xlsx"
templateFile = "Template.tex"
outputFolderName = "Output"
dictionaryOfFieldsToReplace = {
    "Name": "field1",
    "id": "field2",
}
keyUsedForFilename = "Name"

dataFrame = pd.read_excel(excelFile,header=0)

if not(os.path.exists(os.path.join(os.getcwd(), outputFolderName))):
    subprocess.run(["mkdir", outputFolderName]) 

for rowNumber, rowEntry in dataFrame.iterrows():
    with open(templateFile, "rt") as fin:
        with open("Template_copy.tex", "wt") as fout:
            for line in fin:
                myline = line
                for key, value in dictionaryOfFieldsToReplace.items(): 
                    myline = myline.replace("{{" + value + "}}", str(getattr(rowEntry,key)))
                fout.write(myline)
    print("Compiling document for " + getattr(rowEntry,keyUsedForFilename))
    subprocess.run(["pdflatex", "Template_copy.tex"], stdout=subprocess.DEVNULL) 
    subprocess.run(["mv", "Template_copy.pdf", os.path.join(outputFolderName, getattr(rowEntry,keyUsedForFilename) + ".pdf")]) 

subprocess.run(["rm", "Template_copy.log"]) 
subprocess.run(["rm", "Template_copy.aux"]) 
subprocess.run(["rm", "Template_copy.tex"])