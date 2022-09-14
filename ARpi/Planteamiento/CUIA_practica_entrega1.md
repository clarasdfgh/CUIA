# Entrega 1: 27 marzo

### Objetivo

> Realización de una aplicación en la que se haga un uso destacado de la  realidad aumentada para resolver una necesidad de un nicho de mercado  bien definido

- **Uso de la realidad aumentada**: realidad aumentada de percepción directa
- **Necesidad**: familiarización con el piano, ayudar al desarrollo de la memoria muscular para músicos
- **Nicho de mercado bien definido**: conservatorios, asociaciones y escuelas de música

### Tareas

> Estudio de las características del software existente destinado a la creación de aplicaciones de Realidad Aumentada.

> > Entornos de desarrollo, bibliotecas...
> >
> > Open source, comercial, versiones de prueba, marcas de agua...

- ARtoolkit - software libre y de código abierto
- Unity -  software privativo con versión gratis
- ARcore - software libre
- OpenCV - software libre y de código abierto

----

> Identificación de un problema para el que el empleo de Realidad Aumentada pueda suponer una ayuda importante 

**Problema**: el piano es un instrumento en el cual es difícil iniciarse incluso si conoces solfeo y un instrumento previo: el trabajo paralelo independiente de las dos manos es un aspecto no se encuentra en casi ningún instrumento, y la lectura en acordes y dos claves se puede antojar muy difícil a músicos de otras disciplinas.

**Solución**: a modo de apoyo, la aplicación proyecta sobre el teclado las teclas a tocar, permitiendo al pianista centrarse en más aspectos de la partitura (tempo, intensidad, matiz, pedal...) sin sacrificar tanto tiempo en la lectura y colocación de los dedos. Así, el estudio y ensayo de las piezas será más ameno y se progresará más rápido, ayudando a crear la memoria muscular necesaria hasta que el músico se sienta cómodo con la pieza para tocarla sin la ayuda de ARPI.

> ¿Quién nos dice si supone una ayuda importante?
>
> > Usuarios
> >
> > Clientes
> >
> > Expertos

- **Usuarios**: alumnos noveles de piano, con ciertos conocimientos previos de música, pianistas
- **Clientes**: conservatorios, asociaciones y escuelas de música
- **Expertos**: pianistas, profesores de música, profesores de piano

> ¿En qué dispositivos debería funcionar?
>
> > Depende del problema
> >
> > Depende de nuestras posibilidades

- Programa de ordenador conectado a estructura sobre el piano (webcam+proyector)

> ¿Merece la pena? 									
>
> > Competencia, costes de desarrollo, plazo de amortización, cuota de mercado...

- **Competencia:** para la idea exacta, ninguna. Existen conceptos similares con gafas de realidad virtual (es decir, o en VR o en AR con percepción indirecta), o con aplicaciones móviles que muestran sobre la pantalla la progresión de las teclas. Pero no hemos visto proyectos de percepción directa de esta idea. 

  ARPI tendría la ventaja de "mantener al alumno en el mundo real", donde puede hablar con el profesor cómodamente o mirar la partitura.

- **Costes de desarrollo:** los costes de desarrollo incluirían...

  - Equipo humano y tiempo de trabajo - convenio colectivo (2020) para programador junior: 13.528,40€ anual bruto
    - Salario mínimo interprofesional por hora es de 7,82 €
  - Infraestructura - lugar donde llevar a cabo el desarrollo, equipos informáticos, internet...
  - Hardware - webcam, proyector, piano, soporte...

- **Plazo de amortización:**

  - https://mcr.es/como-valorar-la-amortizacion-de-los-proyectos-de-ingenieria/
  - **Modelo de negocio:** licencia + hardware/estructura
    - Licencia X€
    - Hardware estimado:
      - Cámara: lote 100 webcam al por mayor: 56.7$/ud
      - Proyector: lote 100 miniproyector al por mayor: 24.70$/ud
      - Soporte: precio diseño+impresión 3D pieza de soporte
        - Modelado 3D 24$/hora (único pago una vez se obtenga el modelo)
        - Precio impresión aprox 5$/hora, depende de material 
          - https://imprimakers.com/es/producto/calculadora-impresion-3d-online/

- **Cuota de mercado:** 

  - **Nuestro mercado**: software educativo, software educativo musical, aulas TIC
  - *La cuota de mercado es la proporción de mercado que consume los productos o servicios de una empresa determinada.*
    - *Por ejemplo, si tienes una empresa de calzado y tus beneficios totales trimestrales fueron de 100.000 $ y los de tu industria de 1.000.000 $, tu cuota de mercado es del 10%. La fórmula exacta debería ser similar a esta: 100.000 $ / 1.000.000 $ = 0,10 x 100 = 10% de cuota de mercado.*

### Primera entrega - 27 de marzo

> Título

ARPI (Augmented Reality PIano): Realidad aumentada directa aplicada a la enseñanza de instrumentos de tecla

> Autores

Leire Requena y Clara Romero

> Descripción general de la aplicación

Programa de ordenador basado en realidad aumentada de percepción directa. Mediante un proyector y una webcam, y dada una partitura en formato digital, se proyecta sobre el piano un indicador de las teclas que corresponde tocar. 

> Justificación/Motivación
>
> > Interés del problema a resolver
> >
> > Competencia
> >
> > Opiniones de expertos/clientes/usuarios acerca de la idea
> >
> > Software/Hardware a utilizar						

**Justificación/Motivación:** 

- **Problema**: el piano es un instrumento en el cual es difícil iniciarse incluso si conoces solfeo y un instrumento previo: el trabajo paralelo independiente de las dos manos es un aspecto no se encuentra en casi ningún instrumento, y la lectura en acordes y dos claves se puede antojar muy difícil a músicos de otras disciplinas.

- **Solución**: a modo de apoyo, la aplicación proyecta sobre el teclado las teclas a tocar, permitiendo al pianista centrarse en más aspectos de la partitura (tempo, intensidad, matiz, pedal...) sin sacrificar tanto tiempo en la lectura y colocación de los dedos. Así, el estudio y ensayo de las piezas será más ameno y se progresará más rápido, ayudando a crear la memoria muscular necesaria hasta que el músico se sienta cómodo con la pieza para tocarla sin la ayuda de ARPI.

**Competencia:**

- En percepción directa, prácticamente nula. Los proyectos de percepción directa suelen ser costosos y difíciles de implementar, pero creemos que podemos ofrecer esta herramienta a un precio asequible y que las ventajas contra nuestros competidores superan a los inconvenientes
- Existen competidores en el campo de realidad virtual o de realidad aumentada indirecta, pero creemos que un accesorio aparatoso como las gafas VR los aleja demasiado del modelo educativo junto al profesor que nos gustaría alentar

**Opiniones de expertos/clientes/usuarios:**

- Director de banda y presidente de asociación musical
- Pianistas
- Profesores de piano
- Pianista y pedagogo musical con enfoque TIC

**Software/Hardware a utilizar:**

- **Software:** 
  - ARtoolkit - software libre y de código abierto
  - Unity -  software privativo con versión gratis
  - ARcore - software libre
  - OpenCV - software libre y de código abierto
- **Hardware:**
  - Cámara
  - Proyector
  - Soporte
  - Piano

