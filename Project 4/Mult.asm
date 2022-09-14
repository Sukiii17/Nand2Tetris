// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// initialize R2 and loop hunter
      @R2    // initialize R2=0
      M=0
      @i     // initialize loop counter i=1
      M=1

// loop for adding R1 to itself R0 times, which gives R0*R1
(LOOP)
      @i
      D=M     // D=i
      @R0
      D=D-M     // D=i-R0
      @END
      D;JGT     // If (i-R0)>0 goto END
      @R1
      D=M     // Get the value of R1
      @R2
      M=D+M     // Add value of R1 and write back to R2
      @i
      M=M+1     // Increase the loop counter by 1
      @LOOP
      0;JMP     // Unconditional jump, goto LOOP
(END)
      @END
      0;JMP     // infinite loop