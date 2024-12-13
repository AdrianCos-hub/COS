import random
import main
def start():
    while True:
        bentuk_goa ="|_|"
        goa_kosong = [bentuk_goa] * 4   #ini tetap harus kosong

        goa = goa_kosong.copy()         #ini adalah tempat baru COS
        COS_position =random.randint(1, 4)
        goa[COS_position -1]= "|0_0|"
        goa_kosong =' '.join(goa_kosong)
        goa = ' '.join(goa)
        print(f'COBA PERHATIKAN GOA DI BAWAH INI !\n\n{goa_kosong}\n')
        pilihan_user=int(input("MENURUTMU DI GOA NOMOR BERAPA COS BERADA ? [1 / 2 / 3 / 4 ] "))
        
        if pilihan_user == COS_position:
            print(f"{goa}\nSELAMAT KAMU MENANG !")
        else:
                print(f"{goa}\nMAAF KAMU KALAH !")

        play_again =input("\n\nAPAKAH INGIN MELANJUTKAN GAME NYA LAGI?[y/n]")
        if play_again == "n":
            main.menu()
    


if __name__ == '__main__':
    start()