# import packages
import sys
import Parser
import CodeWriter

# read input and output
inputFile = sys.argv[-1]
outputFile = inputFile[:-2] + 'asm'

class VMTranslator():
    '''
    Construct a Parser to parse the VM input file and a CodeWriter to generate code into the output file.
    '''
    def __init__(self, inputFile, outputFile):
        self.parser = Parser.Parser(inputFile)
        self.code_writer = CodeWriter.CodeWriter(outputFile)
    def translate(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.commandType() == 'C_ARITHMETIC':
                self.code_writer.writeArithmetic(self.parser.arg1())
            elif self.parser.commandType() == 'C_PUSH':
                self.code_writer.writePush(self.parser.arg1(), self.parser.arg2())
            elif self.parser.commandType() == 'C_POP':
                self.code_writer.writePop(self.parser.arg1(), self.parser.arg2())
        self.code_writer.close()

if __name__ == '__main__':
    inputFile = sys.argv[-1]
    outputFile = inputFile[:-2] + 'asm'
    vm_translator = VMTranslator(inputFile, outputFile)
    vm_translator.translate()
    
#VMTranslator('StackTest.vm', 'StackTest.asm').translate()