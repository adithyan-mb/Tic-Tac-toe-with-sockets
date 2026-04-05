# server.py

IP="127.0.0.1"
PORT=3000
import socket



# print("tic tac toe game")
import os
import time
# player can have more than 3 moves in a game
result_combination=[[0,1,2],[3,4,5],[6,7,8], 
                    [0,3,6],[1,4,7],[2,5,8],
                    [0,4,8],[2,4,6]]

user1_moves=[]
user2_moves=[]
all_moves=[" "," "," "," "," "," "," "," ", " "]
current_player=1
count=1


def print_grid():
    os.system("clear")
    print("       TIC - TAC -TOE game \n")
    print(" user1: 'X'    \n")
    print(f"   {all_moves[0]}  |  {all_moves[1]}  |  {all_moves[2]}")
    print("-------------------")
    print(f"   {all_moves[3]}  |  {all_moves[4]}  |  {all_moves[5]}")
    print("-------------------")
    print(f"   {all_moves[6]}  |  {all_moves[7]}  |  {all_moves[8]}")
    



def check_winner(user_moves):
    for result in result_combination:
        count=0
        for i in user_moves:
            if(i in result):
                count=count+1

        if(count ==3):
            return True
    
    return False


def move(user_input):
            global count
            global current_player
            if current_player==1:               
                all_moves[user_input]="X"
                user1_moves.append(user_input)
                current_player=2
                if(check_winner(user1_moves)):
                    return 1
                
                count=count+1
            
                

            else:                
                all_moves[user_input]="O"
                user2_moves.append(user_input)
                if(check_winner(user2_moves)):
                    return 2
               
                count=count+1
                current_player=1
            print_grid()
            
        

    



def start():
    print("Hello ! Welcome.......")
    
    time.sleep(2)
    os.system("clear")
    print("    TIC - TAC -TOE game \n Your are USER:1 \n")
    time.sleep(2)
    os.system("clear")

    server=socket.socket()
    server.bind((IP,PORT))
    server.listen()
    conn,addr=server.accept()

    print("client IP address and port",addr)

    global count

    print_grid()
    while (count<10):
        
        
        if(current_player==1):
            while True:
                user_input=(int(input("enter position (1-9)")) -1)
                if (all_moves[user_input] != " "):
                 print(" position already used ")
                 continue
                else:
                 break

         
            move(user_input)
            conn.send((str(user_input)).encode())
            if(check_winner(user1_moves)):
                    print_grid()
                    print("USER 1 : winner")
                    break
      

        elif(current_player==2):
             
              data=conn.recv(1024) 
              user_input=int(data.decode())
              move(user_input)
              if(check_winner(user2_moves)):
                    print_grid()
                    print("USER 2 : winner")
                    break
             


    else:
        if(check_winner(user1_moves)==False and check_winner(user2_moves)==False):
            time.sleep(2)
            print(" \nThe game ended in a DRAW")
            conn.send((str(-1)).encode())

        
    server.close()  
    

start()



