print("Hola mundo en python de nuevo ajaja xD")
#Explicar directorio, staging, repositorio
#Antes de crear el primer commit se debe configurar git por lo menos (git config --list)
#con nombre de user and email comando: git config --global user.name// user.email
#Pasos git add nombreArchivo, git commit -m "Comentario"
#Para regresar un archivo de staging a directorio --> git rm --cached "nombreArchivo"
# git log nombreArchivo --> Para ver el historial de los commits de cada commit

#*Analizar cambios de un archivo*#
#git show nombreArchivo
# git diff host1 host2

#*Regresar a commits anteriores*
#git reset sadsada(host) --hard/soft --> el mas utilizado es hard
#Pero ojo se elimina lo que se habia hecho con hard
# git checkout asdasdas(hosts) nombreArchivo --> Regresa en el tiempo en el host indicado
# git checkout master nombreArchivo --> sinceramente no me agrada esta forma
#es mas practico crear otra rama y realizar ahi los experimentos y despues enviarlo a produccion

