# import packages
import sys
import Parser
import CodeWriter
import os


class VMTranslator():
    """
    Construct a Parser to parse the VM input file and a CodeWriter to generate code into the output file.
    """
    def __init__(self, inputFiles, outputFile):
        """
        Intakes a list of .vm files and outputs to one single .asm file.
        """
        self.code_writer = CodeWriter.CodeWriter(outputFile)
        self.inputFiles = inputFiles
        
    def translate(self):
        """
        Parses, translates, and writes every .vm file in the intake files list to the output file.
        """
        for file in self.inputFiles:
            self.parser = Parser.Parser(file)
            self.code_writer.setFileName(file)
            while self.parser.hasMoreCommands():
                self.parser.advance()
                if self.parser.commandType() == 'C_ARITHMETIC':
                    self.code_writer.writeArithmetic(self.parser.arg1())
                elif self.parser.commandType() == 'C_PUSH':
                    self.code_writer.writePush(self.parser.arg1(), self.parser.arg2())
                elif self.parser.commandType() == 'C_POP':
                    self.code_writer.writePop(self.parser.arg1(), self.parser.arg2())
                elif self.parser.commandType() == 'C_LABEL':
                    self.code_writer.writeLabel(self.parser.arg1())
                elif self.parser.commandType() == 'C_GOTO':
                    self.code_writer.writeGoto(self.parser.arg1())
                elif self.parser.commandType() == 'C_IF':
                    self.code_writer.writeIf(self.parser.arg1())
                elif self.parser.commandType() == 'C_FUNCTION':
                    self.code_writer.writeFunction(self.parser.arg1(), self.parser.arg2())
                elif self.parser.commandType() == 'C_CALL':
                    self.code_writer.writeCall(self.parser.arg1(), self.parser.arg2())
                elif self.parser.commandType() == 'C_RETURN':
                    self.code_writer.writeReturn()
        self.code_writer.close()
            


if __name__ == '__main__':
    
    filePath = sys.argv[-1]
    filePath = os.path.normpath(filePath)
    if filePath[-3:] == '.vm': # if filename is a single .vm file
        inputFiles = [filePath]
        fileDirname = os.path.dirname(filePath)
        basename = os.path.basename(fileDirname)
        outputFile = fileDirname + '/' + basename + '.asm'
    else: # if filename is a path to directory
        basename = os.path.basename(filePath)
        inputFiles = []
        for files in os.listdir(filePath):
            if files.endswith('.vm'):
                inputFiles.append(os.path.join(filePath, files))        
        # inputFiles = glob.glob(filePath+'/*.vm')
        outputFile = filePath + '/' + basename + '.asm'
    vm_translator = VMTranslator(inputFiles, outputFile)
    vm_translator.translate()
    

