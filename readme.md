
## 🚀 TESTING CON PYTEST

## Requerimientos

### 1. Instalar Python
En Windows: Descarga el instalador de Python desde [Aqui](https://www.python.org/downloads/windows/). (se recomienda la versión 3.10.12 o similar)

Asegúrate de marcar la casilla **"Add Python to PATH"** al comienzo de la instalación. Sigue las instrucciones del instalador para completar la instalación.

### 2. Instalar Entorno Virtual (opcional)
Crea una carpeta y abre la terminal para introducir los siguientes comandos:

- Instalar el paquete de virtualenv
```
  pip install virtualenv
```
- Crea un nuevo entorno virtual dentro de la carpeta
```
  virtualenv venv
```
- Activar el entorno virtual desde cmd (no powershell)

```
  .\venv\Scripts\activate 
  o 
  . venv\Scripts\activate
```
### 3. Clonar o descargar el repositorio


Para clonar o descargar el repositorio testing_pytest desde GitHub, primero necesitas tener Git instalado en tu sistema. Para clonarlo, abre la terminal o Command Prompt, navega al directorio donde deseas guardar el proyecto, y ejecuta:

 ``` git clone https://github.com/Sirmauricio10000/testing_pytest.git``` 
 
Esto creará un directorio llamado testing_pytest con todo el contenido del repositorio. 

Si prefieres descargarlo como un archivo ZIP, ve a la página del repositorio [Aquí](https://github.com/Sirmauricio10000/testing_pytest), haz clic en el botón verde Code y selecciona Download ZIP. Después, extrae los archivos del ZIP en el directorio deseado.

### 4. Instalar Dependencias

Si estás trabajando con entorno virtual, asegúrate de que esté activado. verifica que tienes el archivo **"requirements.txt"** en el directorio de tu proyecto, luego ejecuta:

```
pip install -r requirements.txt

```

Esto instalará las dependencias necesarias para trabajar con pytest. Tambien puedes descargarlas de forma manual, una por una con el comando:

```
pip install <paquete a instalar>

```


### 5. Empezar a Trabajar con Pytest
Con el entorno virtual activado y las dependencias instaladas, puedes empezar a usar Pytest.
Para verificar que Pytest está instalado correctamente, ejecuta:
```
pytest --version
```
Para ejecutar tus pruebas con Pytest, navega al directorio donde se encuentran tus archivos de prueba y ejecuta:

```
pytest --html=report.html
```

Esto generará un reporte donde podrás comprobar el estado de tus pruebas.



## Ejemplo

```javascript
import secrets
import httpx
import pytest

@pytest.mark.asyncio
async def test_positivo_crear_nota_correctamente():
    async with httpx.AsyncClient() as client:

        randomString = secrets.token_hex(5)
        nombreCategoria = f"Categoria_{randomString}"
        response = await client.post(
            "http://localhost:8000/api/v1/categorias", 
            json={                                      
                "nombre": nombreCategoria,
            }
        )

        print("Respuesta del servidor:")
        print(response.json())


        assert response.status_code == 200       
        assert response.json()["nombre"] == nombreCategoria 
        assert isinstance(response.json()["id"], str) 
```
### Explicación 
Este código es una prueba unitaria escrita para Python utilizando las bibliotecas httpx, pytest, y secrets, junto con el decorador **@pytest.mark.asyncio** para indicar que se trata de una prueba asíncrona. 

La prueba verifica que una solicitud **HTTP POST** a una API para crear una nueva categoría se maneje correctamente. A continuación, se desglosa cada parte del código para entender su propósito y funcionamiento:

### Importaciones:

- **secrets**: Se utiliza para generar un string hexadecimal aleatorio, garantizando que cada prueba use un nombre de categoría único.
- **httpx**: Una biblioteca HTTP para Python que permite realizar solicitudes HTTP asíncronas. Es similar a requests pero con soporte completo para asyncio.
- **pytest**: Un marco de pruebas para Python que facilita la escritura de pequeñas pruebas, pero puede escalar para soportar pruebas funcionales complejas.
### Definición de la Prueba Asíncrona:

- **@pytest.mark.asyncio**: Un decorador de pytest que marca la función como una prueba asíncrona. Esto le dice a pytest que debe ejecutar la función de prueba en un bucle de eventos asyncio.
- **async def test_positivo_crear_nota_correctamente()**: Define una función de prueba asíncrona. El nombre de la función sigue la convención de nombrado de pytest, empezando con test_, lo cual es necesario para que pytest reconozca automáticamente la función como una prueba.
### Cuerpo de la Prueba:

- **async with httpx.AsyncClient() as client:** Crea un cliente asíncrono usando httpx. Este cliente se utilizará para hacer solicitudes HTTP asíncronas dentro de un contexto que garantiza el cierre adecuado del cliente al finalizar la prueba.
- **randomString = secrets.token_hex(5)**: Genera un string hexadecimal aleatorio de 10 caracteres (5 bytes) para asegurar que el nombre de la categoría sea único en cada ejecución de la prueba.
- **nombreCategoria = f"Categoria_{randomString}"**: Construye el nombre de la categoría combinando un prefijo estático con el string aleatorio generado.
- **response = await client.post(...)**: Realiza una solicitud POST asíncrona a la API, enviando un objeto JSON con el nombre de la categoría. await se utiliza para esperar que la solicitud se complete antes de continuar con la ejecución.
- **print(response.json())**: Imprime la respuesta de la API convertida a un objeto Python mediante el método **.json()**. Esto es útil para fines de depuración, para ver los datos que la API retorna en respuesta a la solicitud POST.
### Aserciones:

- **assert response.status_code == 200**: Verifica que el código de estado de la respuesta HTTP sea 200, indicando una operación exitosa.
- **assert response.json()["nombre"] == nombreCategoria**: Comprueba que el nombre de la categoría retornado por la API en el cuerpo de la respuesta coincide con el que se envió en la solicitud.
- **assert isinstance(response.json()["id"], str)**: Asegura que el id retornado en la respuesta es una cadena de caracteres (str). Esto verifica indirectamente que se creó una nueva categoría y que la API devolvió un identificador para ella.