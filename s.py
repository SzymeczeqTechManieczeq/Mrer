import psutil
import time
import os
os.system("clear")
#did by "github.com/SzymeczeqTechManieczeq" Based on "https://github.com/Marusiella" project.
c = input("\033[1;37;40mCzy masz w komputerze/laptopie Baterię? napisz tak lub nie: \n")
while True:
	os.system("clear")
	if c == "tak":
		bateria = (psutil.sensors_battery().percent)
		print("\033[1;32;40mProcent naładowania baterii: " + str(round(bateria)) + "%")
		czyladuje = str(psutil.sensors_battery().power_plugged)
		if czyladuje == "True":
			czyladuje = "tak"
			print("Czy sprzęt się ładuje? " + czyladuje)
		else:
			czyladuje = "nie"
			print("Czy sprzęt się ładuje? " + czyladuje)
	else:
		print("\033[1;32;40mNie masz Baterii")
	ram = str(psutil.virtual_memory().percent)
	print("\033[1;33;40mProcent wykorzystania ramu: " + ram + "%")
	cpu = str(psutil.cpu_percent())
	print("\033[1;36;40mProcent wykorzystania procesora: " + cpu + "%")
	watki = str(psutil.cpu_count())
	print("Ilość wątków: " + watki)
	rdzenie = str(psutil.cpu_count(logical=False))
	print("Ilość rdzeni: " + rdzenie)
	cpustatscurrent = (psutil.cpu_freq().current)
	cpusa = str(round(cpustatscurrent, 2))
	print("Aktualne taktowanie procesora: " + cpusa + " mhz")
	cpustatsmax = str(psutil.cpu_freq().max)
	print("Maksymalne możliwe taktowanie procesora: " + cpustatsmax + " mhz")
	cpustatsmin = str(psutil.cpu_freq().min)
	print("Najniższe możliwe taktowanie procesora: " + cpustatsmin + " mhz")
	swapbo = (psutil.swap_memory().total)
	swap = str(round(swapbo/1048576))
	print("\033[1;31;40mIlośc pamięci swap: " + swap + " mb")
	time.sleep(1)
