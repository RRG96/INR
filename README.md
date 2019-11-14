# INR
Instalar Raspbian

Pasos:
Descargar Raspbian Lite: **https://www.raspberrypi.org/downloads/raspbian/**
Descargar programa Etcher e  instalar: **https://www.balena.io/etcher/**
Insertar la memoria Micro SD al equipo.
Abrir el programa Etcher, seleccionar la imagen recién descargada y a continuación seleccionar la memoria Micro SD.
Finalizar el proceso y esperar a que la imagen sea grabada en la memoria.
Insertar la memoria en la ranura de la `Raspberry Pi` y conectar a alimentación*.

### Configuracion SSH (Opcional)

Para configurar la conexión a través de SSH, la memoria después de ser grabada deberá abrirse en una computadora con sistema operativo Ubuntu para acceder a los archivos raíz del sistema operativo.
Entrar a la carpeta root de la memoria, en esa carpeta crear un archivo sin extensión son el nombre ssh.
Abrir la terminal en la carpeta donde en la dirección /etc/wpa_supplicant/.
Modificar el fichero con el siguiente código “sudo nano wpa_supplicant.conf ».
Agregar los datos de la red WiFi deseada de la siguiente manera:
```	network=
	{
		ssid="nombre-de-tu-wifi“
		psk="password-de-tu-wifi”
	}
```
Insertar la memoria en la ranura de la `Raspberry Pi` y conectar a alimentación.
Entrar a la terminal de una computadora que este conectada a la misma red que se le indico a la Raspberry Pi y buscar la IP que la red le asigno.
Si se usa un computadora con Windows se puede ocupar Wireshark.
Si se usa una computadora con Ubuntu  utilizamos el comando `Nmap –sP`

## Instalación Librerías

Las librerías a instalar son las siguientes:
 - MNE versión 0.17
 - Mushu versión 0.2
 - PyUsb versión 1.0.0
 - Numpy versión 1.11.0
 - Python versión 2.7.0

### Pasos:
Verificar en la `Raspberry Pi`, que el lenguaje `Python` ya este instalado.
Instalar el módulo git con el comando “sudo apt-get install git” o “sudo apt-get install gitpython”.
Descargar la carpeta con el comando “sudo git clone https://github.com/RRG96/INR.git”.
Verificar la existencia de la carpeta en la Raspberry Pi con el comando “ls –l”.
Entrar en la carpeta con el comando `cd INR`.
Correr el programa InstalacionR.py con el comando `sudo python instalacionR.py`.
Correr el programa de Adquisicion.py con el comando `sudo python Adquiscion.py`.

## Método 1 (RECOMENDADO):
En la Raspberry Pi.
Instalar MNE con el comando `sudo apt-get mne` o `sudo apt-get python-mne`.
Instalar PyUsb con el comando `sudo apt-get pyusb`.
Instalar mushu con el comando `sudo apt-get libmushu` o `sudo apt-get python-mushu`.

## Método 2:
Clonar cada una de las carpetas de las librerías de git con el comando `git clone https://direccionweb.git`
- https://github.com/pyusb/pyusb.git
- https://github.com/mne-tools/mne-python.git
- https://github.com/bbci/mushu.git

Verificar que cada una de las carpetas se encuentren en la Raspberry Pi con el comando `ls –l`
Ingresar a cada una de las carpetas con el comando `cd nombredelacarpeta`
Dentro de cada una de las carpetas correr el comando `sudo python setup.py` 

## Posibles Errores

Los errores más comunes:
- `comando` no se reconoce como un comando interno o externo: significa que el módulo donde se encuentra este comando no esta instalado.
- TypeError: 'NoneType' object is not iterable: significa que el amplificador no esta conectado.
- ImportError: No module named `módulo`: significa que la librería que se esta tratando de importar no se instalo adecuadamente.
