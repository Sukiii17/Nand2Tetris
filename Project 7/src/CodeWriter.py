
class CodeWriter():
    """
    Translates VM commands into Hack assembly code.
    """
    def __init__(self, outputfile):
        """
        Opens the output file/stream and gets ready to write into it.
        """
        self.f = open(outputfile, "w") 
        self.current_file = outputfile.replace('.asm','').split('/')[-1]
        self.boolean_count = 0
               
        
    def writeArithmetic(self, command):
        """
        Writes the assembly code that is the translation of the given arithmetic command.
        Input: string, one of the following: add, sub, neg, eq, gt, lt, and, or, not
        """
        assembly_code = ''
        assembly_code += '//' + command + '\n'
        if command == 'add':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n'
        elif command == 'sub':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n'
        elif command == 'neg':
            assembly_code += '@SP\nA=M-1\nM=-M\n'
        elif command == 'eq':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@continue{}\n'.format(str(self.boolean_count))     
            assembly_code += 'D;JEQ\n@SP\nA=M-1\nM=0\n(continue{})\n'.format(str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'gt':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@continue{}\n'.format(str(self.boolean_count))     
            assembly_code += 'D;JGT\n@SP\nA=M-1\nM=0\n(continue{})\n'.format(str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'lt':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@continue{}\n'.format(str(self.boolean_count))     
            assembly_code += 'D;JLT\n@SP\nA=M-1\nM=0\n(continue{})\n'.format(str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'and':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n'
        elif command == 'or':
            assembly_code += '@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n'
        elif command == 'not':
            assembly_code += '@SP\nA=M-1\nM=!M\n'
        else:
            raise ValueError('Cannot write assembly code for this arithmetic command')
        self.f.write(assembly_code)
               
        
    def writePush(self, segment, index):
        """
        Writes the assembly code that is the translation of the given push command.
        Inputs:
        - segment can be one of the following: local, argument, this, that, pointer,
          temp, static, constant
        - index: integer
        """
        assembly_code = ''
        assembly_code += '//' + 'push ' + segment + ' ' + str(index) + '\n'
        if segment == 'local':
            assembly_code += '@LCL\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'argument':
            assembly_code += '@ARG\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'this':
            assembly_code += '@THIS\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'that':
            assembly_code += '@THAT\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'A=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'pointer':
            if index == 0:
                assembly_code += '@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
            elif index == 1:
                assembly_code += '@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
            else:
                raise ValueError('Invalid index for the pointer')
        elif segment == 'temp':
            assembly_code += '@'+str(index+5)+'\n'
            assembly_code += 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'static':
            assembly_code += '@'+str(self.current_file)+str(index)+'\n'
            assembly_code += 'D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        elif segment == 'constant':
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        else:
            raise ValueError('Invalid segment! Cannot write assembly code for this push command')
        self.f.write(assembly_code)


    def writePop(self, segment, index):
        """
        Writes the assembly code that is the translation of the given pop command.
        Inputs:
        - segment can be one of the following: local, argument, this, that, pointer,
          temp, static
        - index: integer
        """
        assembly_code = ''
        assembly_code += '//' + 'pop ' + segment + ' ' + str(index) + '\n'
        if segment == 'local':
            assembly_code += '@LCL\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n'
        elif segment == 'argument':
            assembly_code += '@ARG\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n'
        elif segment == 'this':
            assembly_code += '@THIS\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n'
        elif segment == 'that':
            assembly_code += '@THAT\nD=M\n'
            assembly_code += '@'+str(index)+'\n'
            assembly_code += 'D=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n'
        elif segment == 'pointer':
            if index == 0:
                assembly_code += '@SP\nAM=M-1\nD=M\n@THIS\nM=D\n'
            elif index == 1:
                assembly_code += '@SP\nAM=M-1\nD=M\n@THAT\nM=D\n'
            else:
                raise ValueError('Invalid index for the pointer')
        elif segment == 'temp':
            assembly_code += '@SP\nAM=M-1\nD=M\n'
            assembly_code += '@'+str(index+5)+'\n'
            assembly_code += 'M=D\n'
        elif segment == 'static':
            assembly_code += '@SP\nAM=M-1\nD=M\n'
            assembly_code += '@'+str(self.current_file)+str(index)+'\n'
            assembly_code += 'M=D\n'
        else:
            raise ValueError('Invalid segment! Cannot write assembly code for this push command')
        self.f.write(assembly_code)    
    
    
    def close(self):
        """
        Closes the output file.
        """
        self.f.close()

