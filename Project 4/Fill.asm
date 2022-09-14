// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

      @SCREEN
      D=A     // get the starting RAM address of SCREEN
      @pointer
      M=D     // initialize a pointer to keep track of memory location

(LOOP)
      @KBD
      D=M     // get value of KBD      
      @WHITE
      D;JEQ     // check if key is pressed and jump to white if yes
      @BLACK
      0;JMP     // otherwise jump to black

(BLACK)     // if it is pressed, fill the screen black
      @pointer
      D=M
      @KBD
      D=D-A
      @LOOP
      D;JGE     // jump if maximum achieved (KBD), note we don't include RAM[KBD]
      @pointer
      A=M
      M=-1     // fill the current address black
      @pointer
      M=M+1     // increase pointer by 1, if maximum not achieved     
      @LOOP
      0;JMP     // jump back to loop unconditionally            
    
(WHITE)     // if it is not pressed, fill the screen white
      @pointer
      D=M
      @SCREEN
      D=D-A
      @LOOP
      D;JLT     // jump if minimum achieved (SCREEN), note we include RAM[SCREEN]
      @pointer
      A=M
      M=0     // fill the current address white
      @pointer
      M=M-1     // decrease pointer by 1, if minimum not achieved     
      @LOOP
      0;JMP     // jump back to loop unconditionally  
