//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue0
D;JEQ
@SP
A=M-1
M=0
(continue0)
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue1
D;JEQ
@SP
A=M-1
M=0
(continue1)
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue2
D;JEQ
@SP
A=M-1
M=0
(continue2)
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue3
D;JLT
@SP
A=M-1
M=0
(continue3)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue4
D;JLT
@SP
A=M-1
M=0
(continue4)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue5
D;JLT
@SP
A=M-1
M=0
(continue5)
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue6
D;JGT
@SP
A=M-1
M=0
(continue6)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue7
D;JGT
@SP
A=M-1
M=0
(continue7)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@continue8
D;JGT
@SP
A=M-1
M=0
(continue8)
//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
AM=M-1
D=M
A=A-1
M=D+M
//push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//neg
@SP
A=M-1
M=-M
//and
@SP
AM=M-1
D=M
A=A-1
M=D&M
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
AM=M-1
D=M
A=A-1
M=D|M
//not
@SP
A=M-1
M=!M