# CUIA 21/22 - Tema 6: Inteligencia artificial

La inteligencia es el término global mediante el cual se describe una propiedad de la mente en la que se relacionan habilidades tales como:

- Pensamiento abstracto
- Entendimiento
- Comunicación
- Razonamiento
- Aprendizaje
- Planificación
- etc...

la Inteligencia Artificial (IA) tiene múltiples definiciones, en las que se reflejan dos aspectos:

- **Resultado**

  - **Actuar** (interesa el resultado)

    vs

    **Pensar** (interesa cómo se obtiene el resultado)

- **Funcionamiento**

  - **Como un ser humano** (Funciona como lo haría un ser humano)

    vs

    **Racionalmente** (Funciona según una medida ideal de rendimiento)

Algunas definiciones de Inteligencia artificial: 

> *Automatización de actividades que asociamos con el pensamiento humano, actividades como toma de decisiones, resolución de problemas,  aprendizaje...*
>
> > Hellman , 1978

> *Estudio de cómo hacer que los ordenadores hagan cosas que, por ahora, los humanos hacemos mejor.*
>
> > Rich y Knight, 1991

> *Estudio de las facultades mentales mediante el uso de modelos computacionales*
>
> > Charniak y McDermott, 1985

> Estudio del diseño de agentes inteligentes
>
> > Pool , 1998

> *Disciplina científica que se ocupa de crear programas informáticos que ejecutan operaciones **comparables** a las que realiza la mente humana, como el aprendizaje o el razonamiento lógico.*
>
> > R.A.E.

### 1. Agentes inteligentes

P.E.A.S :

- Se encuentran inmersos en un **E**ntorno
- Perciben el estado del entorno mediante **S**ensores
- Utilizan una medida de rendimiento (**P**erformance)
- Trasladan al entorno sus decisiones mediante **A**ctuadores
  - Ej.  Un conductor de taxi es un agente:
    - Entorno - calles, tráfico, peatones, clientes,... 
    - Sensores - cámaras, GPS, acelerómetro, ... 
    - Medida de rendimiento - distancia, tiempo, seguridad, confort,... 
    - Actuadores - volante, freno, acelerador,... 

#### Entornos

Diversos criterios nos permiten clasificarlos...

- **Completamente observable / Parcialmente observable**
  - ¿Tienen los sensores acceso a todos los aspectos relevantes del entorno? 
    - Ej. Ajedrez vs Póker
- **Determinista / No Determinista**
  - Es determinista si el siguiente estado del entorno solo depende del estado actual y la acción ejecutada por el agente. 
    - Ej. Análisis de imágenes vs conducción de taxi
- **Episódico / Secuencial**
  - En el episódico, la experiencia del agente se divide en episodios (percepción → acción) de modo que la decisión tomada en un episodio no depende de episodios anteriores. 
    - Ej. Ruleta vs Ajedrez
- **Estático / Dinámico**
  - Es estático si el entorno no cambia mientras el agente toma una decisión.
  - Es semidinámico si el entorno no cambia pero sí que cambia la medida de rendimiento.
    - Ej. Ajedrez vs conducción de taxi vs ajedrez con reloj
- **Discreto / Continuo**
  - Es discreto si el número de posibles estados es finito (y bajo). 
    - Ej. Crucigrama vs conducción de taxi

#### Arquitecturas de sistemas inteligentes

##### Modelo reactivo

El comportamiento inteligente surge de la interacción con el entorno más que de complejos procesos internos. No considera estados pasados.

![Reactivo](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/reactivo.png)

##### Modelo basado en el entorno

El sistema tiene en cuenta estados pasados así como modelos de cómo "funciona" el entorno

![Entorno](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/entorno.png)

##### Modelo basado en objetivos

El sistema posee un modelo que le permite conocer en qué medida sus acciones conducirán hacia algunos objetivos establecidos.

![Objetivos](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/objetivos.png)

##### Modelo basado en objetivos

El sistema posee un modelo que le permite conocer en qué medida sus acciones conducirán hacia algunos objetivos establecidos.

![Objetivos](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/objetivos.png)

##### Modelos híbridos

![Híbrido](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/hibrido.png)

##### Modelo basado en conocimiento

El sistema dispone internamente de una representación del conocimiento necesario para tomar decisiones

- Reglas de producción
- Pizarra
- Ontología

##### Modelo basado en aprendizaje

El sistema aprende de la experiencia

1. Capta el estado del entorno
2. A partir del conocimiento previo realiza una acción
3. Emplea una medida de rendimiento para valorar el nuevo estado del entorno
4. Estados y acciones son empleados para mejorar el conocimiento previo

![Aprendizaje](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/aprendizaje.png)

¿Cómo se va a valorar el rendimiento?

- **Aprendizaje supervisado**: Se aprende a partir de ejemplos de los que se conoce su valoración.
  - Para cada ejemplo se compara la respuesta actual del sistema con la respuesta esperada
  - La función de rendimiento se ajusta para tratar de minimizar las diferencias
- **Aprendizaje no supervisado**: Se dispone de ejemplos pero se desconoce la clasificación de los mismos
  - El proceso permitirá aprender a diferenciar las clases
- **Aprendizaje por refuerzo**: Cada acción vendrá acompañada de una recompensa
  - La función de rendimiento se ajustará progresivamente para tratar de maximizar las recompensas

##### Modelos unilaterales

![Unilateral](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/unilateral.png)

##### Modelos bilaterales

![Bilateral](https://ccia.ugr.es/~bailon/clases/CUIA/imagenes/bilateral.png)

### 2. Representación del conocimiento

Primero, algunas definiciones:

- **Datos**: hechos concretos sin procesar ni organizar.
- **Información**: datos que han sido procesados, estructurados, interpretados y presentados en un contexto. Esto les da significado y los hace valiosos, relevantes y útiles para tomar decisiones.
- **Conocimiento**: el conocimiento se obtiene a partir del uso de la información y permite formar juicios, opiniones, predicciones o decisiones.
  - **Implícito** o **tácito**: conocimiento adquirido por medio de la experiencia. Difícil de extraer y codificar.
  - **Explícito**: conocimiento adquirido por memorización a partir de conocimiento ya codificado.

Un Sistema Inteligente basado en conocimiento necesita modelar el conocimiento para poder utilizarlo. Para representar el conocimiento necesitamos conocer:

- Su estructura
- Para qué va a ser usado
- Cómo va a ser usado
- Cómo será adquirido
- Cómo será almacenado y manipulado

#### Formalismos de representación del conocimiento

Representación del mundo real dentro de un ordenador

- **Dominio**: Qué es lo que queremos representar
- **Representación**: Cómo lo vamos a representar

- **Parte estática**: Estructuras de datos que codifican un problema junto con las operaciones necesarias para consultarlas y manipularlas

- **Parte dinámica**: Estructuras de datos que almacenan conocimiento del contexto y procedimientos para la manipulación

La representación siempre será incompleta debido a:

- Modificaciones (el mundo real es cambiante)
- Volumen (en el mundo real hay demasiados elementos a representar)
- Complejidad (el mundo real es demasiado rico en detalles)

##### Propiedades

Propiedades de los esquemas de representación

- **Adecuación representacional**
  - Capacidad de representar todo el conocimiento necesario en el dominio
- **Adecuación inferencial** 
  - Capacidad para manipular las estructuras para inferir nuevo conocimiento.
- **Eficiencia inferencial**
  - Capacidad del sistema para incorporar conocimiento adicional para optimizar los cómputos
- **Eficiencia en la adquisición**
  - Capacidad para adquirir nuevo conocimiento

#### Tipos de conocimiento

- **Declarativo**. Conocimiento que se representa de manera independiente a su uso

- **Procedimental**. Conocimiento que indica cómo se ha de usar, cómo realizar una tarea

Representación del conocimiento

- Lógica proposicional
- Lógica de predicados
- Lógica difusa
- Reglas de producción
- Redes semánticas
- Marcos
- Ontologías

### 3. Inteligencia artificial

¿Dónde se encuentra la Inteligencia Artificial?

- **IA en red**: Son unos nodos fijos en la red los que proporcionan la IA. Solo esos nodos precisan una potencia de cálculo que permita procesamiento de IA
  - Cualquier cambio percibido en el entorno es comunicado a través de la red a los nodos con la IA
  - La respuesta de los nodos con IA se envía a los nodos afectados por la decisión
  - Este proceso ha de ser muy rápido (prácticamented en tiempo real)
- **IA embebida**: Las técnicas de IA necesarias se meten dentro de los nodos de la red
  - Es conceptualmente la mejor solución
  - Cada nodo debe tener potencia de cálculo acorde a sus necesidades básicas más las impuestas por la IA
  - Una desventaja es que el sistema puede mostrar un comportamiento fragmentado en lugar de un comportamiento colaborativo
- **IA distribuida**: Las tareas de IA que ha de realizar un nodo se apoyan en un nodo servidor
  - Es una solución flexible

#### Inteligencia ambiental

> *Soporte eficaz y transparente para la actividad de los sujetos a través  del uso de las tecnologías de la información y las comunicaciones*