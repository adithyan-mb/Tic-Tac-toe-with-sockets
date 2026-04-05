#client.py
import os
import time
import socket

IP="127.0.0.1"
PORT=3000
client=socket.socket()
client.connect((IP,PORT))
count=1

user1_moves=[]
user2_moves=[]
all_moves=[" "," "," "," "," "," "," "," ", " "]
result_combination=[[0,1,2],[3,4,5],[6,7,8], 
                    [0,3,6],[1,4,7],[2,5,8],
                    [0,4,8],[2,4,6]]





def print_grid():
    os.system("clear")
    print("       TIC - TAC -TOE game \n")
    print(" user2: 'O'    \n")
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

    
def start():
    
    global count
    time.sleep(2)
    os.system("clear")
    print("    TIC - TAC -TOE game \n Your are USER:2 \n")
    time.sleep(2)
    os.system("clear")
    
    print_grid()
    while count<10:
        #getting data from server side
        
        user_input= int((client.recv(1024)).decode())
        user1_moves.append(user_input)
        all_moves[user_input]="X"
        count=count+1

        print_grid()
        if(check_winner(user1_moves)):
            print_grid()
            print("USER 1 : winner")
            break
        
           
        if (count!=10):
            while True:
                user_input=(int(input("enter position (1-9)")) -1)
                if ( all_moves[user_input] != " "):
                    print(" position already used ")
                    continue
                else:
                    break
                
                       
            user2_moves.append(user_input)
            all_moves[user_input]="O"
            client.send((str(user_input)).encode())
            count=count+1
            print_grid()

            if(check_winner(user2_moves)):
                print_grid()
                print("USER 2 : winner")
                break
            
    else:
            if(check_winner(user1_moves)==False and check_winner(user2_moves)==False):
                time.sleep(2)
                print(" \nThe game ended in a DRAW")
        

start()


client.close()