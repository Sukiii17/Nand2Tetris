
Contents of the folder:
-- src folder: 
It contains three python code files: Parser.py, CodeWriter.py, VMTranslator.py.
(1) Parser.py: used to parse a single .vm file, reads VM commands, parses them, and provides convenient access to their components.
(2) CodeWriter.py: translates VM commands into Hack assembly code.
(3) VMTranslator.py: The main piece of the translator which makes use of the Parser and CodeWriter modules to do translation. It takes a '.vm' file input (can be a file name or path) and outputs a translated '.asm' file in the same directory.

-- StackArithmetic / MemoryAccess:
These folders and their subfolders contains test files for the translator. Each originally has a '.cmp' '.tst' '.vm' file. The '.asm' file is written by my translator. To test for the program, load the translated '.asm' program and the '.tst' script into the CPU Emulator.


What works for the Project?
I confirm that I have tested for all provided test scripts and for each I got the message 'End of script - Comparison ended successfully'.


How to run the program? 
To run the program, use the 'VMTranslator.py', which requires import of Parser.py and CodeWriter.py modules.
Open the terminal, type python3 VMTranslator.py ~/filename.vm
For example, in my folder, if you want to translate SimpleAdd.vm, run the following:
python3 VMTranslator.py ~/HuangShuqiProject7/StackArithmetic/SimpleAdd/SimpleAdd.vm


Note: The implementation for Push is what Prof. Billingsley did for last week. It can actually be a bit more efficient (with 6 tick-tocks rather than 7), but I've asked her that I do not need to adjust the implementation for this assignment.
