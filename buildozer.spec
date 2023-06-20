[app]

# Nombre de la aplicación (reemplaza con el nombre de tu aplicación)
title = Tz Calculator

# Icono de la aplicación (reemplaza con la ruta a tu propio icono)
#icon.filename = path/to/icon.png

# Versión de la aplicación (reemplaza con la versión deseada)
version = 1.0

# Descripción de la aplicación
description = Mi aplicación Kivy

# Directorio principal de tu aplicación
# (debe contener main.py y otros archivos fuente)
source.dir = C:\Users\Alienware\Documents\VSCode\kivy

# Módulos adicionales a incluir (separados por comas)
# Aquí debes incluir todos los módulos que estés utilizando en tu código
# Por ejemplo, si importas kivy.app, kivy.uix.gridlayout, kivy.uix.button, etc.
# debes incluir "kivy" en esta lista
requirements = kivy

# Nombre del paquete de la aplicación (reemplaza con el nombre de tu paquete)
# Por ejemplo: package.name = com.mycompany.myapp
package.name = com.mycompany.tzcalculator

# Archivos o carpetas adicionales a incluir en el paquete
# (separados por comas)
# Por ejemplo, si tienes archivos de datos, imágenes o cualquier otro recurso
# que necesites incluir en el paquete, puedes agregarlos aquí
# Por ejemplo: include_exts = py,png,jpg,kv,atlas
# o include_patterns = assets/*.png, data/*.txt
# Si no tienes archivos adicionales, déjalo como está
# include_exts =
# include_patterns =

# Exclusión de archivos o carpetas específicos
# Aquí puedes especificar archivos o carpetas que deseas excluir del paquete
# Por ejemplo: exclude_patterns = tests/*,bin/*.txt
# Si no tienes archivos o carpetas para excluir, déjalo como está
# exclude_patterns =

# Permiso de Internet para la aplicación (True o False)
# Si tu aplicación requiere acceso a Internet, establece esto en True
# De lo contrario, déjalo como False
# internet_permission = False

# Otras opciones personalizadas que desees configurar
# Puedes agregar aquí cualquier otra opción personalizada que necesites
# Por ejemplo, si necesitas permisos especiales, configuraciones de compilación, etc.
# Consulta la documentación de buildozer para obtener más información sobre las opciones disponibles
# Por ejemplo: android.permissions = INTERNET, CAMERA
# android.arch = arm64-v8a

[buildozer]

# Ajustes generales de buildozer
# Puedes modificar estos ajustes según tus necesidades
# Consulta la documentación de buildozer para obtener más información sobre las opciones disponibles

# Nombre del archivo de salida del APK (sin extensión)
# Por ejemplo: apk.filename = myapp
apk.filename = tzcalculator

# Versión de Gradle a utilizar
# Por defecto, utiliza la última versión estable
# Si experimentas problemas, puedes especificar una versión específica aquí
# Por ejemplo: android.gradle_version = 4.4.0

# Configuración adicional de Gradle
# Aquí puedes agregar configuraciones adicionales para Gradle si es necesario
# Por ejemplo: android.gradle_dependencies = 'implementation "com.example:library:1.0.0"'
