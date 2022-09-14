### Preguntas sobre el piano

- Queremos feedback o no?? (sabe la app que me he equivocado? como reacciona?)
  - No feedback: la partitura tira palante basandose en la duración de las notas. NO sabe si has tocado la tecla correcta
  - Feedback:
    - Captar micro
    - Diferencia visual entre una tecla pulsada/no pulsada

- Qué sería más factible y más conveniente: 
  - una app de móvil (con el problema implicado de conectarle un proyector) 
  - un programa de ordenador (con el problema implicado de tener que tirar la webcam sobre el soporte)
- Plan de ruta del desarrollo?

### Concepto

- Aplicación PC a proyector (si ya necesitas la parafernalia que es el proyector no necesitas la portabilidad de un móvil) pero si vamos a usar la cámara y el micro, pues igual renta el móvil como dispositivo de captación y app
- Feedback / no feedback:
  - No feedback: la partitura tira palante basandose en la duración de las notas. NO sabe si has tocado la tecla correcta
  - Feedback:
    - Captar micro
    - Diferencia visual entre una tecla pulsada/no pulsada

- Pasos:
  1. Captación de la imagen, calibración (determinar donde empieza y donde acaba el piano)
     1. Si no es factible calcular un número dinámico de octavas, se harían cálculos previos para saber cuantas octavas caben cómodamente en la cámara
  2. Cargar partitura
  3. Generar imágenes (básicamente bloques de color sólido) de anchura y posición basadas en el tamaño de las teclas
  4. Proyectar la imagen, continuar generando/proyectando imágenes al ritmo de la partitura

### Recursos

- ARtoolkit + Unity + Android Studio + ARcore 
  - Tuts4today 9 vídeo tutoriales
  - Gamedevacademy.org tutorial realidad aumentada 

### Preguntas práctica

- Identificación de un problema para el que el empleo de Realidad Aumentada pueda suponer una ayuda importante

  - **La gente no sabe leer música. Al igual que hay gente que aprende a tocar la guitarra sin saber leer partituras, esto haría que el piano fuera un instrumento más accesible. También es una buena herramienta de refuerzo para pianistas.**

  - ¿Quién nos dice si supone una ayuda importante? 									

    - Usuarios
      - **Gente normal, "novelty", quiero tocar el piano y me da igual como que yo voy a tocar river flows in you**
      - **Gente que sabe leer música y no se acostumbra a las teclas del piano**
    - Clientes
      - **Gente normal**
      - **Escuelas de música que no llegan a ser conservatorios, más informales (ej. banda del pueblo)**
      - **Profesores particulares**
    - Expertos
      - **Músicos profesionales**
      - **Profesores de piano**

  - ¿En qué dispositivos debería funcionar? 									

    - Depende del problema
      - **Parece que lo más adecuado a como lo estamos planteando (básicamente un soporte sobre el piano sobre el que colocamos el proyector y la cámara) sería un teléfono**
    - Depende de nuestras posibilidades
      - **Disponemos de PC Linux y Windows, Teléfonos Android y iPad**

  - ¿Merece la pena? 									

    - Competencia,

    - Costes de desarrollo

      - **convenio colectivo (2020) para programador junior 13.528,40 anual bruto, unos 8€/h**

        **salario** mínimo **interprofesional por hora** es de 7,66 €

      - **y se le añadiría infraestructura preexistente (ordenadores, piano, internet, lugar de trabajo) además de los materiales específicos al proyecto: proyector, soporte, webcam...**

    - Plazo de amortización

    - Cuota de mercado (de lo que producimos, qué porcentaje consume qué gente)

      - G**ente normal 30% (freemium y subscripción)**
      - **Músicos 20%**
      - **Escuelas 40% (cuentan con la infraestructura y vender licencias es mas $$$)**
      - **A las escuelas se les vende licencia, a los usuarios individuales plazo de prueba gratuita y luego freemium con opción a suscripción; partnership con proyectores**

- Justificación/Motivación:					

  - Interés del problema a resolver - tocar música sin nociones de solfeo 
  - Competencia - ya existe en formato virtual
  - Opiniones de expertos/clientes/usuarios acerca de la idea - :)
  - Software/Hardware a utilizar
    - ARtoolkit + Unity + Android Studio + ARcore 
    - PC, Piano, Móvil [Cámara, micro], Proyector

### Otras ideas

- Invizimals (buscar animales y luego interactuar con ellos) - si son animales de verdad, se puede dar un enfoque educativo
  - La disponibilidad de los animales depende del entorno (ej, animales acuáticos agua, pájaros silbar, etc..)
- Juego de baile baldosas de colores - 
- Aplicación decoración de interiores (colocar muebles en una habitación)
- Ambient assisted living - cámaras ubicadas en lugarse clave de la casa, desde un panel de control se configuran prompts y steps para hacer las cosas relacionadas con ese punto de la casa - un altavoz indica las instrucciones
- Constelaciones - google sky map pero usando la cámara
- Aplicación filtros faciales (instagram, tiktok)