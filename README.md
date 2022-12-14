# nuestro-primer-mvt
Nuestro Primer MVT
Principios Básicos de Funcionamiento de la Página
Primero se crea una carpeta contenedora del proyecto. En ella se cargan automáticamente los archivos básicos de funcionamiento, que son configurados para interactuar con las app. Módulos preconfigurados, como el settings.py, donde se agregan las aplicaciones "instaladas". Urls dónde se agregan los path de los html. Un script de funcionamiento, manage.py que es el gestor del proyecto, marco sobre el cual correran nuestras app.
También se carga una base de datos integrada, el motor de dicha base de datos, se ejecuta como parte de las app y es aquí donde se guardan los datos proveniente de los CRUD (Create, Read, Update and Delete) que se llevan a cabo a través del proyecto, las aplicaciones, la página en definitiva.
Luego se crea una aplicación, en este caso se ha nombrado familiares_app.
La aplicación, crea automáticamente una serie de módulos de Python. Dentro del paquete o carpeta de app, creamos una carpeta de plantillas html, llamada "templates".
Luego, adaptamos los módulos a los problemas que queremos resolver.
En el módulo models.py creamos las clases de los objetos, que van a trabajar con la base de datos, definimos los atributos y tipos de datos.
Podemos agregar un módulo forms.py, para configurar formularios y sus campos, a través del módulo "form" preconfigurado de Django.
En el módulo views se colocan las funciones, funciones de "renderizado". Se importan todos los módulos necesarios, algunos previamente creados en moldels.py y otros nativos de Django o instanciados en forms.py, por ejemplo.
Para hacer correr las funciones que escribimos en views, dentro del paquete templates se crean los html necesarios que serán llamados a modo de retorno.
En este caso, en views, se plantean 2 maneras de renderizar los html, uno "artesanal" y el predefino del frameworks que utiliza el módulo django.views.generic.
Para que el framework pueda encontrar las funciones escritas en views.py, es necesario pasarle los path en el módulo urls.py del proyecto. Indicando cual va a ser la distribución de las páginas, por tanto va a determinar el índice. Agregando dichos path en la barra de direcciones, permite navegar por ellas.

