
Contents of the folder:
-- src folder: 
It contains three python code files: Parser.py, CodeWriter.py, VMTranslator.py.
(1) Parser.py: used to parse a single .vm file, reads VM commands, parses them, and provides convenient access to their components.
(2) CodeWriter.py: translates VM commands into Hack assembly code.
(3) VMTranslator.py: The main piece of the translator which makes use of the Parser and CodeWriter modules to do translation. It takes a single '.vm' file input or a file path and translates every '.vm' file in that folder. It outputs a single translated '.asm' file in the same directory.

-- FunctionCalls / ProgramFlow:
These folders and their subfolders contains test files for the translator. Each originally has a '.cmp' '.tst' '.vm' file. The '.asm' file is written by my translator. To test for the program, load the translated '.asm' program and the '.tst' script into the CPU Emulator.


What works for the Project?
- I confirm that I have tested for all provided test scripts and for each I got the message 'End of script - Comparison ended successfully'.
- The '.asm' files for 'BasicLoop', 'FibonacciSeries', and 'SimpleFunction' are without bootstrapping codes. Others are with bootstrapping codes.


How to run the program? 
To run the program, use the 'VMTranslator.py', which requires import of Parser.py and CodeWriter.py modules.
Open the terminal, type python3 VMTranslator.py path_name(or file_name)
For example, if you have HuangShuqiProject8 at Desktop, and you want to run 'NestedCall' program. You can do one of the following:
- python3 VMTranslator.py ~/Desktop/HuangShuqiProject8/FunctionCalls/NestedCall/Sys.vm
- python3 VMTranslator.py ~/Desktop/HuangShuqiProject8/FunctionCalls/NestedCall
- python3 VMTranslator.py ~/Desktop/HuangShuqiProject8/FunctionCalls/NestedCall/

All three work. They will produce an output 'NestedCall.asm' in the same folder. The output file is named after the folder it is in.

