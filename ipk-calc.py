#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:09:14 2020

@author: dooriq
"""

import sys

class Mahasiswa:                                                            #class mahasiswa
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.total_sks = 0
        self.total_nilai = 0
        self.total_matkul = 0
        
    def input_nilai(self, nilai, sks):
        self.total_nilai += nilai*sks
        self.total_sks += sks
        self.total_matkul += 1
        
    def tambah_mahasiswa(self, username, nama, npm):
        username = Mahasiswa(nama, npm)
        
    def cek_ipk(self):
        ipk = round(self.total_nilai/self.total_sks,2)
        print(ipk)
        
    def keluar():
        sys.exit()

menu = {}
menu['1'] = "Tambahkan Mahasiswa"
menu['2'] = "Cek IPK Mahasiswa"
menu['3'] = "Keluar"

while True:
    options = menu.keys()
    for pil in options:
        print(pil, menu[pil])
    select = input("Pilih Menu :")
    if select == '1':
        print("1")
    elif select == '3': 
        break
    else: 
        print("Unknown Option Selected!")   

uname = input("uname :")
nama = input("uname :")
npm = input("uname :")

uname = Mahasiswa(nama, npm)

uname.input_nilai(3.4,4)
uname.cek_ipk()
    