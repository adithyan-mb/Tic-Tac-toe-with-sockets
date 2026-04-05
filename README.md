A two-player Tic Tac Toe game played over a network using Python sockets. Built with core Python and no external libraries.


Features
Two players can play over a local network
Real time move updates using TCP sockets
Win detection for both players
Draw detection when all 9 cells are filled
Input validation — prevents overwriting occupied cells


Game flow:
          Player 1 (X) (Server)            Player 2 (O) (Client)
               |                              |
               |  <---- socket open-------->  |
               |                              |
  makes move   |                  |
 checks winner |  ---- sends cell no:------>  | updates board
               |                              | checks winner 
               |                              |
               |                              |
               |  <---- sends cell no: ----   | makes move
updates board  |                              | checks winner
checks winner  |                              |  
               |                              |       
