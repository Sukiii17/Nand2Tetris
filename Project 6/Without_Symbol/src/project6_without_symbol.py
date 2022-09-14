# import packages
import sys


# tables for handling C-Instructions (dest, comp, jump)
COMP_MNEMONIC_TO_BINARY = {
        '0':'0101010',
        '1':'0111111',
        '-1':'0111010',
        'D':'0001100',
        'A':'0110000',
        '!D':'0001101',
        '!A':'0110001',
        '-D':'0001111',
        '-A':'0110011',
        'D+1':'0011111',
        'A+1':'0110111',
        'D-1':'0001110',
        'A-1':'0110010',
        'D+A':'0000010',
        'D-A':'0010011',
        'A-D':'0000111',
        'D&A':'0000000',
        'D|A':'0010101',
        'M':'1110000',
        '!M':'1110001',
        '-M':'1110011',
        'M+1':'1110111',
        'M-1':'1110010',
        'D+M':'1000010',
        'D-M':'1010011',
        'M-D':'1000111',
        'D&M':'1000000',
        'D|M':'1010101'
        }

DEST_MNEMONIC_TO_BINARY = {
        'null':'000',
        'M':'001',
        'D':'010',
        'MD':'011',
        'A':'100',
        'AM':'101',
        'AD':'110',
        'AMD':'111'
        }

JUMP_MNEMONIC_TO_BINARY = {
        'null':'000',
        'JGT':'001',
        'JEQ':'010',
        'JGE':'011',
        'JLT':'100',
        'JNE':'101',
        'JLE':'110',
        'JMP':'111'
        }


# input files and output files
inputFile = sys.argv[-1]
outputFile = inputFile[:-3] + 'hack'


# clean the original .asm file (remove white space, remove comments)
with open(inputFile, 'r+') as f:
    cleaned_file = []
    for line in f:
        line = line.replace(' ', '')  # remove spaces
        # remove everything in the line after //
        partition = line.partition("//")
        if partition[1] == '//':
            line = partition[0]
        line = line.replace('\n', '')  # remove spaces
        # remove blank lines
        if line.strip() != '':
            cleaned_file.append(line)
            

# translate each line to machine language
out = ''  # output for translated binary machine language
for line in cleaned_file:
    
    if line[0] == '@':   # if it is an A-instruction
        out += '{0:016b}'.format(int(line[1:]))    # output the 16-bit binary result
        out += '\n'    # make it a line
        
    else:   # if it is a C-instruction
        partition = line.partition('=')
        if partition[1] == '=':      # if '=' exists in the command
            dest = DEST_MNEMONIC_TO_BINARY[partition[0]]     # look for code for dest
            line = partition[2]
        else:      # if '=' doesn't exist in the command
            dest = DEST_MNEMONIC_TO_BINARY['null'] 
            
        partition = line.partition(';')
        if partition[1] == ';':      # if '=' exists in the command
            jump = JUMP_MNEMONIC_TO_BINARY[partition[2]]     # look for code for dest
            line = partition[0]
        else:      # if '=' doesn't exist in the command
            jump = DEST_MNEMONIC_TO_BINARY['null'] 
            
        comp = COMP_MNEMONIC_TO_BINARY[line]    # comp field of the instruction, mandatory
        code = '111' + comp + dest + jump
        out += code
        out += '\n'


# write to output file
output = open(outputFile, 'w') # output files
output.write(out)
output.close()


