import subprocess

print("\033[1;34;46m"+"Creando entorno virtual...")

subprocess.run(['py','-m','venv','venv'])

print("\033[1;34;46m"+"Entorno virtual creado")
print("\033[1;34;46m"+"Proyecto configurado")