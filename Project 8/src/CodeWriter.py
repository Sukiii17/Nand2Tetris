
class CodeWriter():
    """
    Translates VM commands into Hack assembly code.
    """
    def __init__(self, outputfile):
        """
        Opens the output file/stream and gets ready to write into it.
        """
        self.f = open(outputfile, "w") 
        self.boolean_count = 0
        self.call_count = 0
        # Bootstraping code
        self.f.write('//SP=256\n')
        self.f.write('@256\nD=A\n@SP\nM=D\n')
        self.writeCall('Sys.init', 0)
        
                   
    def setFileName(self, fileName):
        """
        Informs that the translation of a new VM file has started (called by the VMTranslator).
        """
        self.current_file = fileName.replace('.vm','').split('/')[-1]

                
    def writeArithmetic(self, command):
        """
        Writes the assembly code that is the translation of the given arithmetic command.
        Input: string, one of the following: add, sub, neg, eq, gt, lt, and, or, not
        """
        assembly_code = ''
        assembly_code += '//' + command + '\n'
        if command == 'add':
            assembly_code += self.common_arithmetic('M=D+M')
        elif command == 'sub':
            assembly_code += self.common_arithmetic('M=M-D')
        elif command == 'neg':
            assembly_code += '@SP\nA=M-1\nM=-M\n'
        elif command == 'eq':
            assembly_code += self.common_comparison('JEQ',str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'gt':
            assembly_code += self.common_comparison('JGT',str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'lt':
            assembly_code += self.common_comparison('JLT',str(self.boolean_count))
            self.boolean_count += 1
        elif command == 'and':
            assembly_code += self.common_logical('M=D&M')
        elif command == 'or':
            assembly_code += self.common_logical('M=D|M')
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
            assembly_code += self.common_push_local_argument_this_that('LCL', str(index))
        elif segment == 'argument':
            assembly_code += self.common_push_local_argument_this_that('ARG', str(index))
        elif segment == 'this':
            assembly_code += self.common_push_local_argument_this_that('THIS', str(index))
        elif segment == 'that':
            assembly_code += self.common_push_local_argument_this_that('THAT', str(index))
        elif segment == 'pointer':
            if index == 0:
                assembly_code += self.common_push_pointer('THIS')
            elif index == 1:
                assembly_code += self.common_push_pointer('THAT')
            else:
                raise ValueError('Invalid index for the pointer')
        elif segment == 'temp':
            assembly_code += self.common_push_temp_static_constant('M', str(index+5))
        elif segment == 'static':
            assembly_code += self.common_push_temp_static_constant('M', str(self.current_file)+str(index))
        elif segment == 'constant':
            assembly_code += self.common_push_temp_static_constant('A', str(index))
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
            assembly_code += self.common_pop_local_argument_this_that('LCL', str(index))
        elif segment == 'argument':
            assembly_code += self.common_pop_local_argument_this_that('ARG', str(index))
        elif segment == 'this':
            assembly_code += self.common_pop_local_argument_this_that('THIS', str(index))
        elif segment == 'that':
            assembly_code += self.common_pop_local_argument_this_that('THAT', str(index))
        elif segment == 'pointer':
            if index == 0:
                assembly_code += self.common_pop_pointer_temp_static('THIS')
            elif index == 1:
                assembly_code += self.common_pop_pointer_temp_static('THAT')
            else:
                raise ValueError('Invalid index for the pointer')
        elif segment == 'temp':
            assembly_code += self.common_pop_pointer_temp_static(str(index+5))
        elif segment == 'static':
            assembly_code += self.common_pop_pointer_temp_static(str(self.current_file)+str(index))
        else:
            raise ValueError('Invalid segment! Cannot write assembly code for this push command')
        self.f.write(assembly_code)    
    

    def writeLabel(self, label):
        """
        Writes assembly code that effects the label command.
        """
        assembly_code = ''
        assembly_code += '//' + 'label ' + label + ' \n'
        assembly_code += '({})\n'.format(str(self.current_file)+str(label))
        self.f.write(assembly_code)   
    
    
    def writeGoto(self, label):
        """
        Writes assembly code that effects the goto command.
        """
        assembly_code = ''
        assembly_code += '//' + 'goto ' + label + ' \n'
        assembly_code += '@{}\n0;JMP\n'.format(str(self.current_file)+str(label))
        self.f.write(assembly_code)
        
        
    def writeIf(self, label):
        """
        Writes assembly code that effects the if-goto command.
        """
        assembly_code = ''
        assembly_code += '//' + 'if-goto ' + label + ' \n'
        assembly_code += '@SP\nAM=M-1\nD=M\n@{}\nD;JNE\n'.format(str(self.current_file)+str(label))
        self.f.write(assembly_code)
        
        
    def writeFunction(self, functionName, nVars):
        """
        Writes assembly code that effects the function command.
        """
        assembly_code = ''
        assembly_code += '//' + 'function ' + functionName + ' ' + str(nVars) + ' \n'
        assembly_code += '({})\n'.format(functionName)
        for i in range(nVars):
            assembly_code += '@SP\nAM=M+1\nA=A-1\nM=0\n'
        self.f.write(assembly_code)
    
    
    def writeCall(self, functionName, nArgs):
        """
        Writes assembly code that effects the call command.
        """
        assembly_code = ''
        assembly_code += '//' + 'call ' + functionName + ' ' + str(nArgs) + ' \n'
        # push return address
        ret = functionName+str(self.call_count)
        assembly_code += self.common_call('A', ret)
        self.call_count += 1
        # push LCL ARG THIS THAT
        for i in ['LCL', 'ARG', 'THIS', 'THAT']:
            assembly_code += self.common_call('M', i)
        # ARG=SP-n-5
        assembly_code += '@SP\nD=M\n@{}\nD=D-A\n@ARG\nM=D\n'.format(str(nArgs+5))
        # LCL=SP
        assembly_code += '@SP\nD=M\n@LCL\nM=D\n'
        # goto f
        assembly_code += '@{}\n0;JMP\n'.format(functionName)
        # (return address)
        assembly_code += '({})\n'.format(ret)
        self.f.write(assembly_code)
    
    
    def writeReturn(self):
        """
        Writes assembly code that effects the return command.
        """
        assembly_code = ''
        assembly_code += '//return\n'
        # FRAME = LCL
        assembly_code += '@LCL\nD=M\n@FRAME\nM=D\n'
        # RET = *(FRAME-5)
        assembly_code += self.common_return(str(5), 'RET')
        # *ARG = pop()
        assembly_code += '@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n'
        # SP = ARG + 1
        assembly_code += '@ARG\nD=M\n@SP\nM=D+1\n'
        # THAT = *(FRAME-1)
        assembly_code += '@FRAME\nA=M-1\nD=M\n@THAT\nM=D\n'
        # THIS = *(FRAME-2)
        assembly_code += '@FRAME\nD=M-1\nA=D-1\nD=M\n@THIS\nM=D\n'
        # ARG = *(FRAME-3)
        assembly_code += self.common_return(str(3), 'ARG')
        # LCL = *(FRAME-4)
        assembly_code += self.common_return(str(4), 'LCL')
        # goto RET
        assembly_code += '@RET\nA=M\n0;JMP\n'
        self.f.write(assembly_code)
        
        
    def close(self):
        """
        Closes the output file.
        """
        self.f.close()


    def common_arithmetic(self, command_format):
        """
        Helper function for writing assembly code for 'add' and 'sub'.
        """
        return '@SP\nAM=M-1\nD=M\nA=A-1\n{}\n'.format(command_format)
    
    
    def common_comparison(self, command_format, index):
        """
        Helper function for writing assembly code for comparison commands: 'eq', 'gt', 'lt'.
        """
        return '@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=-1\n@continue{}\nD;{}\n@SP\nA=M-1\nM=0\n(continue{})\n'.format(index, command_format, index)
    
    
    def common_logical(self, command_format):
        """
        Helper function for writing assembly code for logical commands: 'and', 'or'.
        """
        return '@SP\nAM=M-1\nD=M\nA=A-1\n{}\n'.format(command_format)
 
    
    def common_push_local_argument_this_that(self, command_format, index):
        """
        Helper function for writing assembly code for push commands with memory segments mappings: 
        'local', 'argument', 'this', and 'that'.
        """
        return '@{}\nD=M\n@{}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'.format(command_format, index)
        
    
    def common_push_pointer(self, index):
        """
        Helper function for writing assembly code for push commands with memory segments mapping 'pointer'.
        """
        return '@{}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'.format(index)
    

    def common_push_temp_static_constant(self, command_format, index):
        """
        Helper function for writing assembly code for push commands with memory segments mappings:
        'temp', 'static', and 'constant'.
        """
        return '@{}\nD={}\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'.format(index, command_format)
    
    
    def common_pop_local_argument_this_that(self, command_format, index):
        """
        Helper function for writing assembly code for pop commands with memory segments mappings: 
        'local', 'argument', 'this', and 'that'.
        """
        return '@{}\nD=M\n@{}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n'.format(command_format, index)
    

    def common_pop_pointer_temp_static(self, index):
        """
        Helper function for writing assembly code for pop commands with memory segments mappings:
        'pointer', 'temp', and 'static'.
        """
        return '@SP\nAM=M-1\nD=M\n@{}\nM=D\n'.format(index)


    def common_call(self, command_format, index):
        """
        Helper function for writing assembly code for function calls.
        """
        return '@{}\nD={}\n@SP\nAM=M+1\nA=A-1\nM=D\n'.format(index, command_format)
    
    
    def common_return(self, index1, index2):
        """
        Helper function for writing assembly code for function returns.
        """
        return '@FRAME\nD=M\n@{}\nA=D-A\nD=M\n@{}\nM=D\n'.format(index1, index2)
    
    
    