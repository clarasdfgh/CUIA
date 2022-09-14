# CUIA 21/22 - Tema 2: Redes de sensores

### 1. Sensores

**Sensor**: dispositivo (natural o artificial) que obtiene información de un objeto físico o un proceso. Son básicamente transductores que transforman un tipo de energía en otro

#### Clasificación

Dependiendo de la necesidad de una fuente de energía...

- **Pasivos**: Perciben y miden una energía emitida por el entorno. 

  Ej. Sensor de infrarrojos

- **Activos**: Necesitan actuar en el entorno para recibir una respuesta que medir.

  Ej. Sensor ecolocalizador

Dependiendo del método empleado para convertir las señales físicas en eléctricas...

- **Resistivos**: Miden cambios en la resistividad.

  Ej. Sensor de temperatura

- **Capacitivos**: Miden cambios en la capacidad.

  Ej. Sensor de movimiento

- **Inductivos**: Miden cambios en la fuerza electromagnética inducida.

  Ej. Sensor de fuerza

- **Piezoeléctricos**: Miden la respuesta de materiales piezoeléctricos.

  Ej. sensor de presión

  

### 2. Redes de sensores

Red de ordenadores equipados con sensores que miden algunas propiedades del entorno.

#### Características

- Ordenadores muy pequeños (nodos) con el hardware mínimo imprescindible
  - Suele haber un número alto de nodos
  - Distribuidos en un entorno que puede ser hostil
    - No limitar los entornos inteligentes a las estructuras (Ej. un olivar puede ser un entorno inteligente)
    - El entorno hostil factor determinante - no puedo garantizar la calidad de los nodos o de la red. No puedo poner todas mis esperanzas en que un determinado nodo esté bien
  - Algunos componentes se incorporarán solo a algunos nodos para reducir costes
  - Es importante que el consumo energético sea reducido
  - Autónomo, de operación desatendida y adaptable a cambios en el entorno
    - El nodo debe poder funcionar autónomamente, sin precisar de otros nodos, y adaptarse a los nodos que queden vivos a su alrededor
- Conexión inalámbrica entre los nodos (WSN)
  - Las conexiones entre nodos no están planificadas de antemano sino que surgen espontáneamente (instalación muy fácil)
    - No se pueden planificar "sobre el papel", bien sea por entorno hostil; o bien sea porque los sensores no se mantienen fijos en el espacio. No podemos plantear con qué nodos se va a comunicar otro nodo.
      - Esto plantea que el nodo debe descubrir con qué nodo se puede comunicar
      - Aunque existe una estación base, varios nodos más deben tener capacidad de transmitir los datos fuera de la red 
- El objetivo de la red es captar y transmitir mediciones de algunas propiedades físicas
  - La red no realiza procesamiento de los datos captados
  - Uno de los nodos de la red (sumidero/estación base) realizará la función de transmitir los datos fuera de la red

#### Objetivos de diseño

- **Reducción del tamaño** de los nodos para facilitar su distribución y reducir su costo y consumo
- **Reducción del costo del nodo** ya que son muy numerosos, están muy expuestos y no suelen ser  reutilizables
  - Nodo que usamos, nodo que perdemos, seguramente no lo vamos a recuperar
- **Reducción del consumo energético** para alargar su vida útil, ya que el reemplazo o recarga de las baterías suele ser difícil o imposible
- **Autoconfiguración de los nodos** ya que suelen distribuirse sin una planificación previa y están sujetos a cambios en la topología de la red
- **Escalabilidad en los protocolos de red** para hacer frente a redes de decenas, cientos o miles de nodos

- **Adaptabilidad** para hacer frente a cambios en la topología de la red
- **Fiabilidad** en el envío de los datos de los sensores a través de canales con ruido y sujetos a fallos
- **Tolerancia a fallos** para que la red sea capaz de superar condiciones adversas de nodos que fallan
- **Seguridad** para prevenir el uso no autorizado de la información
- **Aprovechamiento del canal**, que suele disponer de un limitado ancho de banda
- **Soporte de QoS** para un correcto tratamiento de la latencia y la pérdida de paquetes en función de las aplicaciones

Dependiendo del ámbito de aplicación, pueden hacerse algunas consideraciones:

- En algunos entornos puede ser más provechosa una comunicación/alimentación cableada (Ej. en una casa)

- Los sensores no tienen por qué estar estáticos (aunque es lo más habitual)

- - Ej. Redes de sensores corporales obteniendo información de parámetros biométricos, crowdsourcing obteniendo información de comunidades de individuos

### 3. Componentes redes de sensores

#### Nodo sensor

- Microcontrolador
- Emisor/receptor de comunicaciones (frecuentemente inalámbricas)
- Sensor (excepto en nodos exclusivos de comunicaciones)
- Memoria externa
- Batería
- Adaptador para la programación
- Carcasa protectora (en función de la localización)

#### Sistema Operativo

Muy ligero, su función es la de permitir a las aplicaciones interactuar con el hardware, planificar y priorizar tareas y gestionar eficientemente los recursos

- Contiki
- SOS
- TinyOS
- MANTIS
- Nano-RK
- LiteOS

#### Comunicaciones

Comunicación mediante ondas electromagnéticas

- Modulación / Desmodulación de la señal para transmitir información
  - Amplitud
  - Frecuencia
  - Fase

Las ondas se ven afectadas por diversos tipos de distorsión:

- **Atenuación**: degradación, pérdida de energía con la distancia
  - Más grave en la señal digital que la analógica - por eso para larga/media distancia se transmiten señales analógicas
- **Reflexión y refracción**: el medio por el que se transmite la onda magnética cambia de un medio a otro y sufre alteraciones
- **Difracción**: "rendija" 
- **Efecto Doppler**
- **Ruido electromagnético**: perturbación provocada por fuentes naturales
- **Interferencias**: perturbación provocada por fuentes externas

Problemas con las redes inalámbricas:

- **Nodo oculto**

  ![image-20220613101734026](/home/clara/.config/Typora/typora-user-images/image-20220613101734026.png)

- **Nodo expuesto** 

  ![image-20220613101744794](/home/clara/.config/Typora/typora-user-images/image-20220613101744794.png)

#### Protocolos de acceso al medio (MAC)

- **Objetivos:**
  - Escalabilidad
  - Minimizar colisiones
  - Minimizar overhearing
  - Minimizar esperas para recibir datos
  - Minimizar transmisión de metadatos
  - Minimizar consumo energético
  - Minimizar retraso
  - Maximizar rendimiento

Existen tres tipos:

- **Con disputa**: los nodos compiten entre sí por el control del medio
  - ALOHA
  - CSMA
  - MACA
  - MACAW
- **Sin disputa:** se planifica cómo se va a establecer el uso del canal
  - Planificación estática
    - **Acceso múltiple por división de frecuencias FDMA**: bajo rendimiento
    - **Acceso múltiple por división temporal** **TDMA**: no hay colisiones pero las esperas son altas
    - **Acceso múltiple por escucha de portadora** **CDMA**: hay colisiones y elevado consumo de energía. Problemas de nodo oculto y expuesto en redes inalámbricas
    - **ZigBee** (IEEE 802.15.4): orientado a dispositivos de bajo consumo. Comunicaciones a través de un coordinador PAN.
  - Planificación dinámica
    - Paso de testigo
    - Votación
    - Sistema de reservas
- **Híbridos**



Algunos protocolos más adaptados a redes de sensores en los que se establecen periodos de descanso

- **Sensor MAC (SMAC)**
  - Cada nodo planifica sus momentos de actividad y reposo
  - Los nodos difunden sus planificaciones al entrar en reposo y al activarse
  - Cada nodo va adaptando su planificación para sincronizar con la de los nodos vecinos
- **Berkeley MAC (BMAC)**
  - Empleo de preámbulos suficientemente largos
  - Alto overhearing y susceptible a ataques por privación de sueño
- **X-MAC**
  - Envío de varios paquetes de preámbulo con información del destino
  - Menor rendimiento
- **BoX-MAC**
  - No necesita sincronización, esperas reducidas y bajo consumo



### 4. Gestión de enlace

En una red de sensores inalámbrica, los enlaces son:

- Poco fiables
- Asimétricos
- Muy variables en el espacio y tiempo

En una red de ordenadores se busca que los paquetes emitidos lleguen al receptor:

- Sin errores
- En el orden adecuado
- Sin duplicados
- Sin pérdidas

Pero en una red de sensores los duplicados y el orden no son parámetros muy relevantes, por lo que el objetivo es:

- Sin errores
  - Prevención de errores
  - Corrección de errores
- Sin pérdidas



#### Detección de errores

Los enlaces son propensos a error porque son muy cambiantes. Por eso usamos código detector de errores.

- Cuando el receptor recibe el paquete comprueba si hay errores - si los hay, manda un paquete de vuelta y se le vuelve a envíar el paquete original
- Pero, si no llega a su destino se pierde el paquete? El receptor espera eternamente, el emisor espera eternamente... se le pone un timeout
  - Si se alcanza, se da por perdido el paquete y se vuelve a enviar
- Y si lo que se pierde es el paquete de confirmación? timeout

Que los paquetes lleguen con identificadores duplicados o desordenados no nos preocupa tanto, porque los paquetes mandados por una red de sensores no suelen dividirse en varios paquetes - así que nos centraremos más en que no haya pérdidas ni errores

#### Enrutamiento

¿Cómo encaminar una transmisión hasta el destino?

- Requisitos
  - Eficiencia energética
    - Puede haber nodos en reposo
  - Flexibilidad
    - Nuevos nodos, nodos que fallan, enlaces cambiantes.

Mecanismos básicos de enrutamiento:

- Broadcast: un nodo envía datos a todos los nodos de la red
- Unicast: un nodo envía datos a otro nodo de la red
- Multicast: un nodo envía datos a múltiples destinatarios
- Convergecast: todos los nodos envían datos a un destinatario. Los datos de varias fuentes se van mezclando por el camino

La diferencia entre un unicast desde todos los nodos hacia la base, y un convergecast es que convergecast va acumulando de abajo a arriba, así que es más eficiente enviar los paquetes acumulados que uno por cada nodo.

#### Métricas para el enrutamiento

- **Tradicionales:**
  - Distancia geográfica: entonces los nodos necesitan un gps o algún modo de poder ubicarlos, se pueden generarse bucles en la red de nodos... Muy costoso y no tan práctico.
  - Número de saltos: calculamos al principio y periódicamente. Pero los saltos pueden ser muy grandes; además, el hecho de que los nodos se pueden mover cambiaría los resultados. Tampoco tiene en cuenta el estado actual de las conexiones entre los nodos.
  - Número de retransmisiones
  - Tiempo
  - QoS (rendimiento, latencia, jitter)
- **Basadas en la energía:**
  - Mínima energía consumida por paquete
  - Máximo tiempo antes de partición de la red
  - Mínima variación en energía de los nodos
  - Máxima capacidad de energía
  - Mínima capacidad de energía

Opciones de enrutamiento:

- Flooding. Envío del paquete a todos los nodos de la red.
- Enrutamiento basado en localización.
- Difusión dirigida (Ej. Collection Tree Protocol)
- Enrutamiento basado en gradiente

### 5. WSN grandes

El envío de datos a la estación base puede ser muy costoso

- Soluciones
  - Agregar los datos sobre la marcha
  - Reducir los datos generados por cada nodo
  - Descomponer la red en subredes (clustering)
    - Clustering aleatorio
    - Múltiples nodos base
    - Clustering geográfico

#### Procesado y agregación de datos en WSN grandes

Objetivo: aprovechar al máximo el uso del canal

- Compresión de varios paquetes en uno solo
- Agregación y resumen estadístico de datos
- Compressive sensing para toma de muestras al azar y no continua

#### Sincronizacion

Dos tipos:

- Sincronización externa
- Sincronización interna



- Lightweight Tree Synchronization
- Reference Broadcast Synchronization
- No Time Protocol

#### Localización

A tener en cuenta...

- Precisión
- Coste
- Interior / exterior

Posibles opciones:

- Triangulación: necesita 2 puntos de referencia
  - Necesita antenas direccionales para percibir la dirección
- Trilateración: necesita 3 puntos de referencia
- Localización basada en saltos
- Punto en triángulo
