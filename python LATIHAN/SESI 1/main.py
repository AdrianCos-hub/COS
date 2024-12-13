from libs import welcome_message,exit_program
from games import cos
from tools import warung
def menu():
     print("SIHLAKAN BOLEH PILIH YANG ADA DI MENU !")
     user_option= int(input(f'MENU PROGRAM :\n1. GAMES COS\n2. WARUNG MINI\n3. EXIT PROGRAM\n\nSIHLAHKAN PILIH :'))
     
     if user_option == 1:
          cos.start()
     elif user_option == 2:
          warung.start()
     elif user_option == 3:
          exit_program()
     else:
          ("HANYA BOLEH PILIH YANG ADA DI MENU !")
     

def main():
     welcome_message()
     menu()

if __name__ =='__main__':
     main()


    





    





