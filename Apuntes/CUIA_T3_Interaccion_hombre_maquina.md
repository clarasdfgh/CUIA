# CUIA 21/22 - Tema 3: Interacción hombre-máquina

### 1. HCI

- **Interacción**: bidireccional, diversos tipos de interacción.
- **Hombre**: uno o varios usuarios de diversas capacidades físicas y mentales. Interacción cooperativa o competitiva.
- **Máquina**: cualquier elemento con capacidades computacionales, una o varias máquinas participando en la interacción. Interacción unidireccional o bidireccional.

Interacción hombre-máquina, definición:

> *Disciplina relacionada con el diseño, evaluación e implementación de sistemas informáticos interactivos para ser usados por personas, y con el estudio de los fenómenos más importantes que están involucrados.* 

La HCI es un campo multidisciplinar:

- **Informática**: diseño de aplicaciones y sus interfaces
- **Psicología**: teorías de procesos cognitivos y análisis empírico del comportamiento humano
- **Antropología**: interacción entre tecnología, trabajo y empresa
- **Sociología**: fenómenos colectivos producidos por la actividad social de los seres humanos
- **Diseño** **industrial**: creación de productos interactivos

#### Historia de la HCI

- Años 60 - En los inicios de la computación no había interacción propiamente dicha entre el usuario y el ordenador

- Años 70 - La aparición de los monitores junto con el uso del teclado aceleran el intercambio de información con el usuario, pero la interacción aún es muy pobre:

  - Interfaces no ergonómicas y mal diseñadas
  - Interfaces difíciles de usar y aprender
  - Cada aplicación dispone de su propia interfaz

- Años 80 - Los ordenadores personales acercan la computación a muchos usuarios, y la existencia de muchos usuarios con habilidades limitadas demanda la creación de interfaces más simples y eficientes:

  - Primeros estudios formales sobre HCI
  - La UI clásica va dando paso a la GUI
    - Codificación verbal y espacial de la información en menús
    - Acciones ejecutadas en la misma pantalla usando el ratón = Mejor realimentación

- Años 90 - El diseño de interfaces se convierte en una disciplina tratada científicamente

  - Importantes cambios en el diseño de las GUI
  - La interfaz se convierte en un sistema centrado en el usuario

- Los 2000 - HCI es vista como una interacción que se desarrolla en contextos sociales y de organización

  - Diferentes sistemas tratan de satisfacer las variadas necesidades humanas
  - El componente humano se estudia según...
    - Psicología
    - Habilidades
    - Limitaciones físicas

#### HCI moderna

Se consideran las características del ser humano que influyen en la interacción:

- Limitadas capacidades de procesado de información

- Las emociones influyen en las capacidades humanas

- Los usuarios tienen capacidades comunes pero no debe ignorarse que son individuos distintos

- El ser humano emplea diversos canales de recepción y emisión de información

- - Imagen, sonido, háptica (tacto y el resto de sentidos)
  - Movimiento, actuadores en general

- La información se almacena en memoria

- - Corto plazo, largo plazo, episódica...

- La información es procesada

- - Razonamiento, resolución de problemas...

### 2. Interfaces de Usuario UI 

La interfaz de usuario (UI) es el medio que permite al usuario comunicarse con el sistema. Un diseño pobre de la UI acarrea problemas. Un mal diseño...

- Ralentiza el aprendizaje
  - El usuario pasa mucho tiempo entendiendo el funcionamiento
- Hace que el usuario cometa más errores
  - Esto puede no ser admisible en sistemas críticos
- Dificulta el uso
  - La UI fuerza al usuario a hacer tareas de un modo que puede no ser deseable
  - El usuario debe entrenar en el nuevo modo de realizarlas, reduciendo así su productividad
- Reduce las ventas

Una UI es efectiva si es:

- Útil - Capacidad para realizar una tarea que el usuario necesita
- Usable - La interacción se realiza de modo fácil, natural y seguro
- Usada - De nada vale el sistema si no se usa
  - Debe enriquecerse la experiencia del usuario haciendo el sistema atractivo

### 3. HCI explícita 

Pone al usuario en el centro del proceso, es él quien controla las operaciones del sistema. 

La existencia de múltiples dispositivos puede hacer que el usuario se abrume por tantos sistemas que controlar. Aunque la UI de todos los dispositivos esté bien diseñada, el uso en un ambiente de computación ubicua es complejo porque...

- Hay que realizar tareas que involucran a varios dispositivos
- Los dispositivos pueden ser usados por distintos tipos de usuarios
- El usuario puede afrontar varias actividades a la vez
- Las actividades pueden desarrollarse en múltiples entornos físicos
- Las actividades pueden estar compartidas
- A veces es necesario parar o retomar una actividad

### 4. HCI implícita 

Acción llevada a cabo por el usuario cuyo objetivo principal no es interactuar con el sistema pero que el sistema interpreta como una entrada. 

En la HCI explícita, el usuario tiene que tener un modelo mental del sistema para interactuar con él (H2C), mientras que en la implícita es la máquina la que tiene un modelo de usuario, contexto humano (C2H). 

#### Modelo de usuario

El modelo de usuario representa el contexto del usuario, es decir, las características del usuario que interactúa con el sistema.

Criterios en el diseño del modelo de usuario:

- Adquisición implícita o explícita
- Modelo de usuario o modelo de tipo de usuario
- Modelo estático o dinámico
- Modelo  genérico o  específico de aplicación

Las dificultades que nos podemos encontrar al crear el modelo de usuario son:

- Puede ser muy complejo determinar el contexto humano

- - Razonamiento cualitativo del usuario
  - El usuario puede estar indeciso
  - No determinismo del individuo
  - No determinismo en el entorno

- La determinación del contexto humano puede distraer al usuario o ser imprecisa

- El sistema puede necesitar bastante tiempo para construir un modelo de un usuario

#### Interfaces de usuario en un sistema de computación ubicua UUI

¿Cómo deben ser las interfaces de usuario en un sistema de computación ubicua (UUI)?

- **Grata**
  - El aprender un nuevo UUI no debería obligar a aprender una nueva actividad o un lenguaje complejo
- **Sin distracción**
  - No se debe solicitar constante atención sobre el UUI
  - El funcionamiento desatendido debe ser la norma, no la excepción
- **Respeto por el flujo cognitivo**
  - El sistema debe permitir al usuario centrarse por completo en la tarea que desea realizar
- **Menos manuales**
  - No se debe forzar al usuario a leer un manual de uso del UUI
  - Debe usarse la experiencia como mecanismo de aprendizaje
- **Transparencia**
  - No forzar al usuario a mantener en mente el estado de la aplicación para poder usar la UUI
- **Sin estados ocultos**
  - Se debe evitar que el sistema responda distinto a los mismos estímulos en función de algún estado oculto
- **Reducir el miedo a la interacción**
  - El miedo a hacer algo mal asusta a los usuarios
  - Es conveniente disponer de mecanismos sencillos para deshacer acciones
- **Notificaciones**
  - La información suministrada al usuario puede integrarse en interacciones con su entorno físico
- **Interacción natural**
  - La UUI debe dar soporte a acciones habituales de un usuario  contemplando diversos sentidos humanos y diversos mecanismos de  interacción
- **Acciones por defecto**
  - Una buena UUI debe aprovecharse de la información que conoce y la que puede deducir

#### Nuevas interfaces de usuario

- **Interfaz en superficie (SUI, Surface UI)**: se apoyan en superficies autoiluminadas que incorporan los mecanismos de control necesarios.

  - Diversos tamaños, desde dispositivos del tamaño de la palma de la mano a dispositivos grandes como una pizarra

- **Interfaz tangible (TUI, Tangible UI**): integra representación y control en el mismo objeto físico

  - Se reduce la distancia entre el mundo real y el virtual

  - El usuario interactúa principalmente mediante gestos realizados sobre un objeto real

  - No se diferencia entre dispositivos de entrada y de salida

- **Interfaz ambiental (AUI, Ambiental UI)**: no disponen de entrada de datos, sino que las entradas se infieren del contexto
  - La salida de datos se integra en el entorno
  - La información se presenta en la periferia de nuestra atención pero puede traerse a nuestro foco de atención bajo demanda
  - La influencia sobre el usuario es mucho más transparente
