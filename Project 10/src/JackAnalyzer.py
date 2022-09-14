import sys
import os
import CompilationEngine

filePath = sys.argv[-1]
filePath = os.path.normpath(filePath)
if filePath[-3:] == '.jack': # if filename is a single .jack file
    inputFile = filePath
    outputFile = filePath[:-4] + 'xml'
    compilation = CompilationEngine.CompilationEngine(inputFile,outputFile)
    compilation.compileClass()
    compilation.close()
else: # if filename is a path to directory
    for files in os.listdir(filePath):
        if files.endswith('.jack'):
            inputFile = os.path.join(filePath, files)
            outputFile = inputFile[:-4] + 'xml'
            compilation = CompilationEngine.CompilationEngine(inputFile,outputFile)
            compilation.compileClass()
            compilation.close()
                    