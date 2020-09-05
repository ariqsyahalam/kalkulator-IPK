#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:09:14 2020

@author: dooriq
"""

import os
import time

class Mahasiswa: 
                                                     
    def input_nilai(npm, nilai, sks):   
        Main.Menu.mahasiswa[npm]['total_nilai'] += nilai*sks
        Main.mahasiswa[npm]['total_sks'] += sks
        Main.mahasiswa[npm]['total_matkul'] += 1
        Main.mahasiswa[npm]['ipk'] = round(Main.mahasiswa[npm]['total_nilai']/Main.mahasiswa[npm]['total_sks'],2)
        
    def ipk_mahasiswa(npm):
        return Main.mahasiswa[npm]['ipk']
        
    def cek_ipk(npm):
        print('Mahasiswa atas nama ', Main.mahasiswa[npm]['nama'] ,
              ' mendapatkan IPK sebesar ', Mahasiswa.ipk_mahasiswa(npm))
        
    def ganti_nama(npm ,nama_baru):
        Main.mahasiswa[npm]['nama'] = nama_baru
        
    def cek_npm(npm):
        if npm not in Main.mahasiswa:
            print()
            print("NPM yang Anda Masukan Tidak Terdaftar")
            Menu.return_menu()
        
    def informasi_mahasiswa(npm):
        print('''
              DATA MAHASISWA
              ''')
        print('NPM : ',npm)
        print('Nama Mahasiswa : ', Main.mahasiswa[npm]['nama'])
        print('Jumlah Mata Kuliah : ',Main.mahasiswa[npm]['total_matkul'])
        print('Total SKS yang Telah diambil : ', int(Main.mahasiswa[npm]['total_sks']))
        print('IPK : ', Main.mahasiswa[npm]['ipk'])
    

class Menu:    
    menu = {}
    menu['1'] = "Tambahkan Mahasiswa"
    menu['2'] = "Tambahkan Nilai"
    menu['3'] = "Cek IPK Mahasiswa"
    menu['4'] = "Ganti Nama Mahasiswa"
    menu['9'] = "Informasi Detail"
    menu['0'] = "Keluar"
    
    def menu_utama():    
        while True:
            options = Menu.menu.keys()
            print('''
                  ======= IPK CALCULATOR MAIN MENU =======
                  ''')
                  
            for pil in options:
                print(pil,"-", Menu.menu[pil])
            select = input("Pilih Menu :")
            Menu.clear_console()
            
            if select == '1':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                      
                input_npm = input("Masukan NPM Mahasiswa :")
                input_nama = input("Masukan Nama Mahasiswa :").upper()
                Menu.clear_console()
                
                if len(input_npm) != 10:
                    print("NPM Berisikan Angka 10 Digit")
                    Menu.menu_utama()
                
                if input_npm not in Main.mahasiswa.keys():
                    Main.mahasiswa[input_npm] = {'nama': input_nama, 'ipk':0 ,
                                            'total_nilai':0, 'total_sks':0,
                                            'total_matkul':0, 'ipk' :0}
                else:
                    print("NPM Anda Telah Terdafar")
                    Menu.menu_utama()
                
        
            elif select == '2':
                print('''
                      Menambahkan Nilai Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                
                Mahasiswa.cek_npm(ask_npm)
        
                while True:
                    ask_nilai = float(input("Masukan Nilai Mahasiswa :"))
                    ask_sks = int(input("Masukan SKS Mahasiswa :"))
                    
                    Mahasiswa.input_nilai(ask_npm, ask_nilai, ask_sks)
                    
                    lanjut = input("Apakah masih ingin masukan nilai lain? (Y/N) ").upper()
                    if lanjut == "N":
                        Menu.return_menu()
                        break
                
                    
            elif select == '3':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                Mahasiswa.cek_npm(ask_npm)
                Mahasiswa.cek_ipk(ask_npm)
                
            elif select == '9':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                Mahasiswa.cek_npm(ask_npm)
                Mahasiswa.informasi_mahasiswa(ask_npm)
                Menu.return_menu()
                   
            elif select == '0': 
                print('''
                              TERIMA KASIH ^.^
                      ''')
                time.sleep(4)
                Menu.clear_console()
                break
            
            
            else: 
                print("Menu Tidak Tersedia!")
                Menu.return_menu()
                
    def clear_console():
        os.system("clear")
        
    def count_down(t = 3):
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            Menu.clear_console()
            time.sleep(1) 
            t -= 1
            
    def return_menu():
        print("Kembali ke Menu Utama dalam 3 Detik")
        time.sleep(4)
        Menu.clear_console()
        Menu.menu_utama()

class Main:
    mahasiswa = {}
    
    def __init__():
        Menu.menu_utama()
        
Main.__init__()