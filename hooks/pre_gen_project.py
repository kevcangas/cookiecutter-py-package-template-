import subprocess
import time

#Entorno Virtual
print("\033[1;34m"+"Creando entorno virtual..."+"\033[0;m")
subprocess.run(['python3','-m','venv','venv'])
print("\033[1;34m"+"Entorno virtual creado"+"\033[0;m")
time.sleep(4)

#Inicio repositorio
print("\033[1;34m"+"Iniciando repositorio..."+"\033[0;m")
subprocess.run(['git','init'])
print("\033[1;34m"+"Repositorio inciado"+"\033[0;m")

print("\033[1;34m"+"Proyecto configurado"+"\033[0;m")