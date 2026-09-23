# Fundamentos de Internet 

## 1. Del Cliente al Servidor
Cuando escribimos www.youtube.com en el navegador y presionamos Enter, ocurren varios procesos entre nuestro dispositivo, el DNS y los servidores de YouTube hasta que el video aparece en pantalla.
1. El cliente: el navegador
El cliente es nuestro dispositivo y, principalmente, el navegador (por ejemplo, Chrome, Firefox, Edge o Safari).
Primero, escribimos: www.youtube.com en la barra de direcciones y presionamos Enter. El navegador interpreta que queremos acceder a un sitio web y necesita encontrar dónde está ubicado ese sitio en Internet.
2. El navegador consulta el DNS
Los seres humanos utilizamos nombres fáciles de recordar, como www.youtube.com, pero las computadoras se comunican utilizando direcciones IP.
Por eso, el navegador necesita conocer la dirección IP asociada a ese nombre. Para conseguirla utiliza el DNS (Domain Name System).
El DNS funciona como una especie de "agenda telefónica de Internet": recibe el nombre de dominio y busca la dirección IP correspondiente.
Por ejemplo: www.youtube.com → dirección IP
El navegador puede obtener esta información de una caché local, del sistema operativo, del router o consultando un servidor DNS.
3. Se obtiene la dirección IP
Una vez realizada la consulta, el dispositivo obtiene una dirección IP correspondiente al servicio al que debe conectarse.
La dirección IP permite localizar el servidor o servicio de destino dentro de Internet.
Es importante destacar que YouTube utiliza una infraestructura distribuida, por lo que la dirección obtenida puede variar dependiendo de la ubicación, la red y otros factores.
4. El navegador se conecta con el servidor
Con la información necesaria, el navegador establece una comunicación con el servidor de YouTube.
Como YouTube utiliza HTTPS, la comunicación está protegida mediante cifrado. Antes de intercambiar los datos de la página, se establece una conexión segura utilizando TLS.
De esta manera, la información que viaja entre el navegador y el servidor está protegida frente a personas que intenten observarla o modificarla durante el transporte.
5. Entra en juego HTTP/HTTPS
HTTP es el protocolo utilizado para solicitar y transferir recursos de la Web. HTTPS es HTTP protegido mediante TLS.
El navegador envía una solicitud al servidor, indicando qué recurso necesita. El servidor procesa la solicitud y devuelve una respuesta.
De forma simplificada:
Navegador → solicitud HTTPS → servidor de YouTube
Servidor de YouTube → respuesta HTTPS → navegador
La respuesta puede contener información necesaria para construir la página: HTML, hojas de estilo (CSS), JavaScript, imágenes y otros recursos.
6. El servidor procesa la solicitud
El servidor recibe la solicitud y determina qué información debe enviar al navegador.
En un sitio como YouTube no existe necesariamente un único servidor que haga todo. Hay muchos sistemas y servidores distribuidos que pueden encargarse de diferentes tareas, como entregar la página, gestionar información de los videos o proporcionar el contenido multimedia.
Cuando seleccionamos un video, el navegador realiza las solicitudes necesarias para obtener los datos del video.
7. El video llega al navegador
El contenido del video se transmite desde los servidores de YouTube hacia nuestro dispositivo en pequeñas partes.
El navegador recibe esos datos, los procesa y los entrega al reproductor de video. Mientras recibe suficiente información, puede comenzar la reproducción.
8. El navegador muestra el video
Finalmente, el navegador combina y procesa todos los elementos necesarios para mostrar la página.
El reproductor utiliza los datos recibidos para decodificar el video y enviarlo a la pantalla. También se reproduce el audio a través de los dispositivos de sonido.
Por eso, después de unos segundos, podemos ver y escuchar el video.

![Diagrama del proceso] (Fundamentos-internet\Diagrama del proceso.jpeg) 

## 2. Frontend y Backend en acción
1. ¿Qué corresponde al frontend?
El frontend es la parte de la aplicación que el usuario puede ver y utilizar. Es decir, es la interfaz con la que interactúa el paciente.

Por ejemplo, en nuestra aplicación, el frontend incluiría:
Una pantalla para iniciar sesión.
Un formulario para elegir médico, fecha y hora.
Un calendario para consultar los horarios disponibles.
Un botón para confirmar una cita.
Una pantalla que muestre las citas agendadas.

Tres tecnologías posibles para el frontend:
HTML: estructura y contenido de las páginas.
CSS: diseño, colores, tamaños y distribución de los elementos.
JavaScript: permite agregar interactividad y comunicarse con el backend.

2. ¿Qué corresponde al backend?
El backend es la parte que funciona detrás de la aplicación. El usuario normalmente no la ve directamente. Se encarga de procesar la información, aplicar las reglas del sistema y comunicarse con la base de datos.

En nuestra aplicación médica, el backend podría:
Comprobar si un médico tiene disponibilidad.
Registrar una nueva cita.
Consultar las citas de un paciente.
Evitar que dos pacientes reserven el mismo horario.
Autenticar a los usuarios.
Guardar y consultar información en la base de datos.

Tres tecnologías posibles para el backend:
Node.js: permite ejecutar JavaScript en el servidor.
Python: puede utilizarse con frameworks como Django o Flask.
Java: puede utilizarse, por ejemplo, con Spring Boot para desarrollar servicios web.

3. ¿Cómo se comunican el frontend y el backend?
El frontend y el backend se comunican normalmente mediante una API (Application Programming Interface).
La API proporciona diferentes operaciones que el frontend puede solicitar al backend. Estas solicitudes se realizan utilizando el protocolo HTTP o HTTPS.
Request y Response
La comunicación se basa principalmente en dos conceptos:
Request (solicitud): el frontend envía una petición al backend. Por ejemplo, puede solicitar los horarios disponibles de un médico o enviar los datos de una nueva cita.
Response (respuesta): el backend procesa la petición y devuelve información al frontend. Por ejemplo, puede responder que el horario está disponible y que la cita fue registrada correctamente.
En conclusión, el frontend se encarga de la parte visual e interactiva, mientras que el backend procesa los datos y las operaciones. Ambos se comunican mediante una API, utilizando HTTP/HTTPS para enviar requests y recibir responses.

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|-----------------------|------------------------------|----------------------------------|
| REST        |       JSON/XML         |          Alta         |             Baja             |             Alta                 |
| SOAP        |          XML           |          Baja         |             Alta             |             Media                |
| GraphQL     |         JSON           |        Muy Alta       |          Media-Alta          |             Alta                 |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
REST suele ser la mejor opción para una startup porque es relativamente sencilla de implementar, tiene una gran cantidad de herramientas y documentación, y es ampliamente utilizada en aplicaciones web y móviles. Además, permite trabajar fácilmente con JSON y HTTP.
GraphQL también puede ser una excelente opción, especialmente si la aplicación necesita mucha flexibilidad para que el cliente solicite exactamente los datos que necesita. Sin embargo, puede requerir una mayor complejidad inicial y más cuidado en su mantenimiento.
Para comenzar rápidamente y mantener una arquitectura sencilla, elegiría REST. Si la aplicación necesita consultas muy flexibles y tiene requisitos de datos más complejos, consideraría GraphQL.

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:**
JSONPlaceholder
- **Descripción:**
Permite realizar pruebas de solicitudes HTTP sin necesidad de crear una cuenta.

### 4.2 Configuración en Postman
- **Nombre de la colección:**
Collection JSONPlaceholder
- **Solicitudes agregadas:**
  - GET - Obtener publicaciones
  - POST - Crear una publicación
  - PUT - Actualizar una publicación
  - DELETE - Eliminar una publicación

### 4.3 Ejecución y análisis

|      Solicitud         |   Método  |  Endpoint | Código de estado |
|------------------------|-----------|-----------|------------------|
| Obtener publicaciones  |   GET     | /posts    |     200 OK       |
| Crear publicación      |   POST    | /posts    |     201 Created  |
| Actualizar publicación |   PUT     | /posts/1  |     200 OK       |
| Eliminar publicación   |   DELETE  | /posts/1  |     200 OK       |


### 4.4 Explicación técnica

#### 1. Solicitud GET — Obtener información
- **Método HTTP:**
GET
- **Endpoint:**
https://jsonplaceholder.typicode.com/posts/1
Content-Type: application/json
- **Descripción de la respuesta:**
La respuesta tiene código 200, lo que indica que la solicitud fue procesada correctamente. 
El servidor devuelve los datos en formato JSON.

#### 2. Solicitud POST — Crear una publicación
- **Método HTTP:**
POST
- **Endpoint:**
https://jsonplaceholder.typicode.com/posts
- **Parámetros / body:**
{
  "title": "Mi nueva publicación",
  "body": "Esta publicación fue creada mediante una solicitud POST.",
  "userId": 1
}
Content-Type: application/json; charset=utf-8
- **Descripción de la respuesta:**
El código 201 Created indica que el servidor aceptó la solicitud de creación. 
La respuesta devuelve los datos enviados y un identificador para el nuevo recurso.

#### 3. Solicitud PUT — Actualizar una publicación
- **Método HTTP:**
PUT
- **Endpoint:**
https://jsonplaceholder.typicode.com/posts/1
- **Parámetros / body:**
{
  "id": 1, 
  "title": "Publicación actualizada", 
  "body": "Este contenido fue modificado mediante PUT.", 
  "userId": 1 
  }
- **Descripción de la respuesta:**
La solicitud PUT se utiliza para actualizar un recurso existente. 
En este caso, se indica el identificador 1 dentro del endpoint. 
El servidor devuelve el recurso con los nuevos valores.

#### 4. Solicitud DELETE — Eliminar una publicación
- **Método HTTP:**
DELETE
- **Endpoint:**
https://jsonplaceholder.typicode.com/posts/1
- **Descripción de la respuesta:**
La solicitud DELETE indica al servidor que se desea eliminar el recurso identificado con el número 1. 
JSONPlaceholder devuelve una respuesta exitosa, aunque, al tratarse de una API de prueba, la eliminación no modifica permanentemente los datos.

**¿Qué aprendiste del proceso?**
Durante esta práctica aprendí que una API permite la comunicación entre diferentes aplicaciones mediante solicitudes HTTP. 
También comprendí la función de los principales métodos HTTP: GET sirve para obtener información, POST para enviar o crear información, 
PUT para actualizar un recurso y DELETE para eliminarlo.
También aprendí que las respuestas de una API incluyen códigos de estado que permiten saber si una operación fue exitosa o si ocurrió algún problema.

### 4.5 Reflexión final
Durante esta actividad aprendí cómo funcionan las APIs y cómo permiten la comunicación entre un cliente y un servidor. 
Comprendí que cada método HTTP tiene una función específica: GET permite consultar información, POST permite enviar datos para crear un recurso, 
PUT permite actualizar información y DELETE permite eliminar un recurso. También aprendí a interpretar los códigos de estado HTTP y las respuestas en formato JSON.

Postman me ayudó a comprender de una manera más práctica la comunicación entre cliente y servidor porque pude enviar solicitudes y observar directamente las respuestas. 
Además, pude revisar los headers, el cuerpo de las respuestas y los códigos de estado. 
Entendí que una API funciona como un medio de comunicación que permite que una aplicación solicite o envíe información a un servidor siguiendo reglas y formatos definidos.