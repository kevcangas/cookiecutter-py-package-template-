import subprocess

#Entorno Virtual
print("\033[1;34m"+"Instalando modulo localmente..."+"\033[0;m")
subprocess.run(['pip','install','-e','./'],shell=True)
print("\033[1;34m"+"Instalación terminada, fin de la creación del template"+"\033[0;m")