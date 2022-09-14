# CUIA 21/22 - Tema 1: Introducción

### 1. Vivimos en un mundo digital

Hay cada vez más dispositivos digitales diseñados para asistir y automatizar tareas y actividades humanas y realzar la interacción con  el entorno. En 2015-2016 el número de usuarios de dispositivos móviles supera al de sobremesa.

**Omnipresencia de dispositivos**: el entorno se va llenando de dispositivos digitales provistos de sensores capaces de percibir nuestra presencia y actuar en consecuencia. Para eso necesita múltiples sensores - pero no solo es importante la cantidad, sino la calidad.

**Múltiples sensores:** las redes inalámbricas facilitan la interconexión de dispositivos en el entorno

- Dispositivos + sensores + red inalámbrica -> interconexión de todos esos dispositivos (en cantidad y de calidad, o sea, con velocidad)

- Dispositivos + sensores + red inalámbrica + integración -> los dispositivos son más pequeños, baratos, fiables, eficientes... 

**AALIANCE** (The European Ambient Assisted Living Innovation Platform) - Desarrollada a nivel europeo por el envejecimiento de la población. Estandarización e interoperabilidad de los principios para el AAL, automatización del hogar, telecomunicaciones, medicina...

> *Las tecnologías más significativas son aquellas que desaparecen. Se entretejen en el tejido de la vida cotidiana hasta que no se pueden distinguir.* 
>
> Mark Weiser
> The computer of the 21st century, 1991

> *Technology is anything that wasn't around when you were born.* 
>
> Alan Kay



### 2. Eras de la computación

Inversión de la multiplicidad (de un ordenador para muchos, a muchos ordenadores para uno):

1. **Mainframe**: un gran ordenador con el que interactuaban muchos usuarios
2. **PC**: un ordenador para cada usuario
3. **Computación Ubicua**: muchos ordenadores usados por una persona

![image-20220613090300769](/home/clara/.config/Typora/typora-user-images/image-20220613090300769.png)



### 3. Computación ubicua

#### Definiciones

- *Visión de la tecnología futura que estará siempre disponible,  frecuentemente monitorizando o anticipándose a las necesidades del  usuario, incluso cuando el usuario no es consciente de la existencia de dicha tecnología.* -- Mark Weiser
- *Omnipresencia de computadores muy pequeños interconectados sin cables que se incrustan de forma casi invisible en cualquier tipo de objeto cotidiano.* --  Friedmam Mattern

Sinónimos:

- Computación pervasiva
- Things that think
- Calm technology
- Everyware

#### Dos dimensiones fundamentales: movilidad e integración

- **Movilidad** - capacidad de llevar con nosotros los objetos computacionales
- **Integración** - los dispositivos computacionales están embebidos en objetos cotidianos

|                      | Movilidad baja                                               | Movilidad alta                                               |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Integración alta** | Computación pervasiva (ideamos un aula inteligente, pizarra, luz, pupitres... pcs por todos lados, pero el aula es un único sitio) | Computación ubicua (Todos los entornos integrados, o sea, salimos del aula inteligente a un pasillo inteligente, facultad inteligente... no es que me sigan los dispositivos, sino que no salgo del entorno) |
| **Integración baja** | Computación clásica (tengo un pc, el pc es un pc, si quiero usarlo tengo que ir al despacho) | Computación móvil (tengo un móvil que llevo donde quiero, el móvil es un pequeño pc) |

#### Propiedades básicas de la computación ubicua

1. **Computadores interconectados, distribuidos y accesibles de modo transparente**

- Múltiples sistemas computacionales interconectados. Son:

  - Heterogéneos
  - Conectados o desconectados en cualquier momento
  - Diseñados para descubrir y acceder a nuevos servicios

  En conjunto se comportan como si fuese un único sistema, de forma que el usuario percibe un único sistema computacional.

  

2. **Interacción hombre-máquina (HCI) más natural**

- HCI: disciplina relacionada con el diseño, evaluación e implementación de  sistemas informáticos interactivos para ser usados por personas, y con el estudio de los fenómenos más importantes que están involucrados. Para hacerla más natural, HCI implícita.

- HCI implícita: hacer desaparecer los elementos de la tecnología (ej. gafas y monturas)

  - Calm computer, no entra en conflicto con el entorno. Esta percepción cambia con la sociedad (ej. Antes ver a alguien caminando por la calle hablando solo con una mano en la oreja nos haría creer que está loco, ahora es simplemente un tío hablando por teléfono. No es precisamente un calm computer, pero sirve para ilustrar lo de que la percepción cambia con el tiempo).

    

3. **Computadores conscientes del contexto**

- El sistema percibe el contexto y modifica su comportamiento de forma adecuada ¿Cómo percibimos el contexto? Mediante sensores



Propiedades adicionales deseables son:

1. **Trabajo autónomo de los computadores**

- Autonomía: propiedad de un sistema que le permite tener control de sus propias acciones. Realizan acciones que les permitan...

  - Cumplir con unos objetivos (*policy*)
  - Alcanzar o dirigirse a unos objetivos (*goal*)

  Reducción de intervención humana = reducción complejidad percibida 

  - A veces la necesidad intervención humana es un cuello de botella (ej. conducción autónoma, se cruza un peatón)
  - Cuestiones:
    - El usuario no percibe el sistema = El usuario no sabe si está funcionando.
    - El usuario no sabe por qué el sistema hace algo.
    - Aumento de la dependencia, las cosas las hace la máquina y no yo. En caso de fallo no sé hacerlas.

2. **Toma de decisiones inteligente**

- La inteligencia artificial no es imprescindible, pero puede jugar un papel muy importante al determinar:
  - Interacción hombre-máquina
  - Consciencia de contexto
  - Autonomía

#### Errores comunes sobre la computación ubicua

- Hay una sola definición precisa de Computación Ubicua

  - Más que la definición, tenemos que entender el concepto y aplicarlo correctamente, con una visión o con otra: cada concepto nos va a llevar a una definición y unas propiedades distintas

- Lo ideal es que se cumplan por completo las 5 propiedades

  - Habrá casos en los que sobre alguna, o no se cumplan al 100%

    - Ej. HCI más natural - el ejemplo al 100% de naturalidad sería interacción cerebro-máquina, lo cual no solo plantea problemas (éticos y tecnológicos), sino que puede ser muy variable (imagina que pienso que tengo que pulsar un botón la semana que viene, pero la máquina detecta que estoy pensando en el botón y lo pulsa) .

      No siempre necesitamos el máximo de naturalidad, en tareas simples una forma muy explícita es más natural que liarla parda para hacerla menos "machine-like".

- Los servicios ofrecidos deben tener siempre acceso ubicuo

  - Ej. En este aula, tiene sentido que el control de la luz se controle desde dentro de la misma. No tiene sentido controlar la luz del aula desde mi casa. Los servicios que ofrece el aula ubicua no tienen por qué ser ubicuos en el mundo.

- La computación sustituirá la interacción en los entornos físico y humano

  - Es trabajo moral de los desarrolladores no hacer dependiente al usuario de la tecnología

  

### 4. Smart DEI

Framework propuesto para el análisis y diseño de sistemas ubicuos. Define 3 patrones de diseño arquitectónico para sistemas de Computación Ubicua:

- **Dispositivos inteligentes:** se centra la atención en la interacción con el entorno virtual
  - Menos autónomos, más dependientes del usuario
  - Menos atención al entorno real, más atención al modo de uso
  - Suelen ser dispositivos personales
  - El dispositivo centra el control y UI
  - Alta movilidad con descubrimiento dinámico de servicios
- **Entornos inteligentes: **presencia de dispositivos muy ligados al entorno físico
  - Los dispositivos suelen centrarse en una sola tarea
  - Pueden diseñarse para anticiparse a la interacción del usuario
  - Actúan frecuentemente de modo autónomo
  - Pueden encontrarse en una ubicación fija o ser móviles
  - Su tamaño puede variar en función de la movilidad
- **Interacciones inteligentes:** modelos complejos de interacción entre servicios de software distribuido y hardware
  - Participación de múltiples entidades para alcanzar objetivos individuales o colectivos
  - Menos atención al contexto físico y más atención al contexto del usuario
