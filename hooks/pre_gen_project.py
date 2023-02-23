import subprocess

#Entorno Virtual
print("\033[1;34;46m"+"Creando entorno virtual..."+"\033[0;m")
subprocess.run(['py','-m','venv','venv'])
print("\033[1;34;46m"+"Entorno virtual creado"+"\033[0;m")

#Inicio repositorio
print("\033[1;34;46m"+"Iniciando repositorio..."+"\033[0;m")
subprocess.run(['git','init'])
print("\033[1;34;46m"+"Repositorio inciado"+"\033[0;m")

print("\033[1;34;46m"+"Proyecto configurado"+"\033[0;m")