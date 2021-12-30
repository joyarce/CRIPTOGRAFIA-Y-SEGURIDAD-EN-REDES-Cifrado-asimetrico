# Criptografía y seguridad en redes: Cifrado simétrico 

Es bien sabido que las filtraciones de bases de datos con contraseñas hasheadas es algo común, como el caso dado de la filtración de los hash de contraseñas del gobierno de Chile.

Inicialmente se identifica con qué algoritmos fueron hasheadas las contraseñas de los siguientes archivos: [diccionarios](https://github.com/joyarce/CRIPTOGRAFIA-Y-SEGURIDAD-EN-REDES-Cifrado-asimetrico/tree/main/archivos/diccionario "Link archivo") y [hashes](https://github.com/joyarce/CRIPTOGRAFIA-Y-SEGURIDAD-EN-REDES-Cifrado-asimetrico/tree/main/archivos/hashes "Link archivo").

Mediante la implementación de un software de crackeo de hash como lo es Hashcat en Python se obtiene el texto plano de cada uno de los hash de los archivos anteriormente mencionados. Estimando el tiempo que se demora en crackear cada uno de ellos.

Luego, este listado de contraseñas en texto plano son hasheadas con un algoritmo que es considerado más seguro. Estimando nuevamente el tiempo que toma este proceso.

Desde el código Python con el que se ha realizado todo el proceso anteriormente señalado, se hace una solicitud a un segundo archivo python para este le envíe la llave pública mediante socket, debido a que generó tanto la llave pública como la privada. 

Una vez recibida la llave pública, se encripta cada nuevo hash con un algoritmo de cifrado asimétrico, generando un archivo .txt que los contenga, el que será enviado mediante sockets hacia el anteriormente mencionado código Python que generó las llaves, el cual además descifrará los hash encriptados.
