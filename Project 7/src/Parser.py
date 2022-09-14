import re

class Parser():
    """
    Handles the parsing of a single .vm file, and encapsulates access to the input code.
    It reads VM commands, parses them, and provides convenient access to their components.
    In addition, it removes all white space and comments.
    """
    def __init__(self, inputfile):
        """
        Opens the input file/stream, removes white space and comments, and get ready to
        parse it.
        """
        self.f = open(inputfile, 'r')
        self.rawfile = self.f.readlines()
        self.cleanfile = []
        for line in self.rawfile:
            command = line.strip()
            command = command.partition("//")[0].replace(' ', '')
            if command != '':
                self.cleanfile.append(command)
        self.cleanfile.reverse()
        self.current_command = None
        
        
    def hasMoreCommands(self):
        """
        Returns boolean value whether there are more commands in the input
        Return: boolean
        """
        return self.cleanfile != []
    
    
    def advance(self):
        """
        Reads the next commands in the input and makes it the current command.
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        if self.hasMoreCommands():
            self.current_command = self.cleanfile.pop()
            
            
    def commandType(self):
        """
        Returns the type of the current Virtual Machine command. 
        C_ARITHMETIC is returned for all the arithmetic commands.
        Command type is one of the followings: C_ARITHMETIC, C_PUSH,
        C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL.
        """
        arithmetic_command = ['add','sub','neg','eq','gt','lt','and','or','not']
        if self.current_command in arithmetic_command:
            return 'C_ARITHMETIC'
        elif 'push' in self.current_command:
            return 'C_PUSH'
        elif 'pop' in self.current_command:
            return 'C_POP'
        elif 'label' in self.current_command:
            return 'C_LABEL'
        elif 'goto' in self.current_command:
            return 'C_GOTO'
        elif 'if-goto' in self.current_command:
            return 'C_IF'
        elif 'function' in self.current_command:
            return 'C_FUNCTION'
        elif 'return' in self.current_command:
            return 'C_RETURN'
        elif 'call' in self.current_command:
            return 'C_CALL'
        else:
            raise ValueError('This is an invalid command type')
        
        
    def arg1(self):
        """
        Returns the first argument of the current command. 
        In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
        Should not be called if the current command is C_RETURN.
        Return: string
        """
        if self.commandType() == 'C_ARITHMETIC':
            return self.current_command
        elif self.commandType() == 'C_PUSH':
            arg = self.current_command.split('push')[1]
            end_ind = re.search(r'\d', arg).start()
            return arg[:end_ind]
        elif self.commandType() == 'C_POP':
            arg = self.current_command.split('pop')[1]
            end_ind = re.search(r'\d', arg).start()
            return arg[:end_ind]
        elif self.commandType() == 'C_LABEL':
            return self.current_command.split('label')[1]
        elif self.commandType() == 'C_GOTO':
            return self.current_command.split('goto')[1]
        elif self.commandType() == 'C_IF':
            return self.current_command.split('if-goto')[1]
        elif self.commandType() == 'C_FUNCTION':
            arg = self.current_command.split('function')[1]
            end_ind = re.search(r'\d', arg).start()
            return arg[:end_ind]
        elif self.commandType() == 'C_CALL':
            arg = self.current_command.split('call')[1]
            end_ind = re.search(r'\d', arg).start()
            return arg[:end_ind]
        elif self.commandType() == 'C_RETURN':
            pass
        else:
            raise ValueError('This is an invalid first argument of the command')
        
        
    def arg2(self):
        """
        Returns the second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION,
        or C_CALL.
        Return: integer
        """
        if self.commandType() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            start_ind = re.search(r'\d', self.current_command).start()
            return int(self.current_command[start_ind:])


