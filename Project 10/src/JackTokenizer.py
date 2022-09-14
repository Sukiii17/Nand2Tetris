
import re

class JackTokenizer():
    """
    This module ignores all comments and white space in the input stream 
    and enables accessing the input one token at a time.
    Also, it parses and provides the type of each token, as defined by the Jack grammer.
    """
    def __init__(self,inputfile):
        """
        Opens the input .jack file / stream and tokenizes it into a list.
        """    
        self.f = open(inputfile, 'r')
        self.cleanfile = self.f.read()
        self.cleanfile = re.sub(r'//.*\n', r' ', self.cleanfile) # get rid of comments //....
        # get rid of comments /*...*/ and /**...*/
        self.cleanfile = re.sub(r'/\*.*?\*/', r' ', self.cleanfile, flags=re.S)
        self.cleanfile = self.cleanfile.replace('\n',' ') # get rid of \n
        self.cleanfile = self.cleanfile.replace('\t',' ') # get rid of \t
        # add white space before and after below listed symbols
        self.cleanfile = re.sub(r'(?<=[{}()[\].,;+\-*/&|<>=\~])', r' ', self.cleanfile)
        self.cleanfile = re.sub(r'(?=[{}()[\].,;+\-*/&|<>=\~])', r' ', self.cleanfile)
        # strip out leading and ending white spaces
        self.cleanfile = self.cleanfile.strip()
        # split according to white spaces unless in the double quote
        self.cleanfile = re.findall(r'[^"\s]\S*|".+?"', self.cleanfile)
        self.cleanfile.reverse()
        self.currentToken = None
        self.escape_seq = {'<':'&lt;', '>':'&gt;', '"':'&quot;', '&':'&amp;'}
        self.keywordList = ['class','constructor','function','method','field','static',\
                        'var','int','char','boolean','void','true','false','null',\
                        'this','let','do','if','else','while','return']
        self.symbolList = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']
 
    def hasMoreTokens(self):
        """
        Are there more tokens in the input?
        Returns: boolean
        """
        return self.cleanfile != []
    
    def advance(self):
        """
        Gets the next token from the input, and makes it the current token.
        This method should only be called only if hasMoreTokens is true.
        Initially there is no current token.
        """    
        if self.hasMoreTokens():
            self.currentToken = self.cleanfile.pop()
                
    def tokenType(self):
        """
        Returns the type of the current token, as a cosntant.
        Returns: keyword, symbol, identifier, integerConstant, stringConstant
        """
        if self.currentToken in self.keywordList:
            return 'keyword'
        elif self.currentToken in self.symbolList:
            return 'symbol'
        elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', self.currentToken):
            return 'identifier'
        elif self.currentToken.isdigit():
            return 'integerConstant'
        else:
            return 'stringConstant'
    
    def keyWord(self):
        """
        Returns the keyword which is the current token, as a cosntant.
        This method should be called only if tokenType is keyword.
        Returns: class, method, function, constructor, int, boolean, char, void, var,
        static, field, let, do, if, else, while, return, true, false, null, this
        """
        if self.tokenType() == 'keyword':
            return self.currentToken
    
    def symbol(self):
        """
        Returns the character which is the current token. 
        Should be called only if tokenType is symbol.
        Returns: char
        """
        if self.tokenType() == 'symbol':
            if self.currentToken in self.escape_seq.keys():
                return self.escape_seq[self.currentToken]
            else:
                return self.currentToken
    
    def identifier(self):
        """
        Returns the string which is the current token.
        Should be called only if tokenType is identifier.
        Returns: string
        """
        if self.tokenType() == 'identifier':
            return self.currentToken

    def intVal(self):
        """
        Returns the integer value of the current token.
        Should be called only if tokenType is integerConstant.
        Returns: int
        """
        if self.tokenType() == 'integerConstant':
            return self.currentToken

    def stringVal(self):
        """
        Returns the string value of the current token, without the opening and closing double quotes.
        Should be called only if tokenType is stringConstant.
        Returns: string
        """
        if self.tokenType() == 'stringConstant':
            return self.currentToken[1:-1]
        
#    def getCurrentToken(self):
#        return self.currentToken
    
        