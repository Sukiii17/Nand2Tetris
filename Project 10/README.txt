
Contents of the folder:
-- src folder: 
It contains three python code files: JackTokenizer.py, CompilationEngine.py, JackAnalyzer.py.
(1) JackTokenizer.py: This module ignores all comments and white space, and enables accessing the input one token at a time. It also provides the type of each token. It is used to tokenize a single .jack file.
(2) CompilationEngine.py: The compilation engine gets its input from a JackTokenizer and emits its output to an output file. The output is generated by a series of compilexxx routines according to the grammar of Jack language. The parsing tree is top-down.
(3) JackAnalyzer.py: The main piece doing translation. It takes a single '.jack' file input or a file path and translates every '.jack' file in that folder. It outputs '.xml' files in the same directory.

-- ArrayTest / Square / ExpressionLessSquare:
These folders and their subfolders contains (1) original .jack files (2) .xml files generated by my program (3) Compare Files (.xml files provided)


What works for the Project?
- I confirm that all my .xml files are identical to the original .xml files provided, up to whitespaces.
- The terminal command I run is diff -w -s my_file compare_file
  which checks that my .xml files are identical to the provided ones up to whitespaces.


How to run the program? 
To run the program, open the terminal, type python3 JackAnalyzer.py path_name(or file_name)
For example, if you have HuangShuqiProject10 at Desktop, and you want to run 'ArrayTest' program. You can do the following:
- python3 JackAnalyzer.py ~/Desktop/HuangShuqiProject10/ArrayTest
It will produce an output 'Main.xml' in the same folder.
