#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Soal 1

import re
from datetime import datetime

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""
pola_tanggal = r'\b\d{4}-\d{2}-\d{2}\b'
tanggal_ditemukan = re.findall(pola_tanggal, teks)
tanggal_sekarang = datetime.now()

hasil = []

for tanggal_str in tanggal_ditemukan:
    tanggal_obj = datetime.strptime(tanggal_str, '%Y-%m-%d')
    tanggal_format_baru = tanggal_obj.strftime('%d-%m-%Y')
    selisih_hari = (tanggal_sekarang - tanggal_obj).days
    hasil.append(f"{tanggal_str} 00:00:00 selisih {selisih_hari} hari")

for item in hasil:
    print(item)


# In[ ]:


#Soal 2

import random
import string

email_list = [
    ("anton@mail.com", "antonius"),
    ("budi@gmail.co.id", "budi anwari"),
    ("slamet@getnada.com", "slamet slumut"),
    ("matahari@tokopedia.com", "toko matahari")
]

def extract_username(fullname):
    return fullname.split()[0]

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

result = []
for email, fullname in email_list:
    username = extract_username(fullname)
    password = generate_random_password()
    result.append((email, username, password))

for email, username, password in result:
    print(f"{email} username: {username} , password: {password}")

