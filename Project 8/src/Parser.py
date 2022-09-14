
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
            command = command.partition("//")[0].strip()
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
        elif self.current_command.partition(' ')[0] == 'push':
            return 'C_PUSH'
        elif self.current_command.partition(' ')[0] == 'pop':
            return 'C_POP'
        elif self.current_command.partition(' ')[0] == 'label':
            return 'C_LABEL'
        elif self.current_command.partition(' ')[0] == 'if-goto':
            return 'C_IF'
        elif self.current_command.partition(' ')[0] == 'goto':
            return 'C_GOTO'
        elif self.current_command.partition(' ')[0] == 'function':
            return 'C_FUNCTION'
        elif self.current_command.partition(' ')[0] == 'return':
            return 'C_RETURN'
        elif self.current_command.partition(' ')[0] == 'call':
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
        elif self.commandType() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            arg = self.current_command.partition(' ')[2]
            return arg.partition(' ')[0]
        elif self.commandType() in ['C_LABEL', 'C_GOTO', 'C_IF']:
            return self.current_command.partition(' ')[2]
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
            arg = self.current_command.partition(' ')[2]
            return int(arg.partition(' ')[2])


