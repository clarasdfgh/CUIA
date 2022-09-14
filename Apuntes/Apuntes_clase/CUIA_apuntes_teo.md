## CUIA 07/03

- Omnipresencia de dispositivos
- 2015-2016 nº de usuarios/dispositivos móviles supera al de sobremesa
- Dispositivos+sensores capaces de detectar nuestra presencia y su entorno
  - No solo cantidad de sensores, sino calidad 
- Dispositivos+sensores+red inalámbrica, interconexión de todos esos dispositivos (cantidad y calidad, o sea, velocidad)
- Dispositivos+sensores+red inalámbrica+integración, los dispositivos son más pequeños, baratos, fiables, eficientes... 
  - Integración: capacidad de incorporar esos dispositivos en cualquier elemento cotidiano
- AALIANCE - Desarrollada a nivel europeo por el envejecimiento de la población
- Alan kay - Technology is anything that wasn't around when you were born. 
- Eras de la computación - inversión de la multiplicidad (de un ordenador para muchos, a muchos ordenadores para uno)
- Movilidad - capacidad de llevar con nosotros los objetos computacionales
- Integración - los dispositivos computacionales están embebidos en objetos cotidianos

|                  | Movilidad baja                                               | Movilidad alta                                               |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Integración alta | Computación pervasiva (ideamos un aula inteligente, pizarra, luz, pupitres... pcs por todos lados, pero el aula es un único sitio) | Computación ubicua (Todos los entornos integrados, o sea, salimos del aula inteligente a un pasillo inteligente, facultad inteligente... no es que me sigan los dispositivos, sino que no salgo del entorno) |
| Integración baja | Computación clásica (tengo un pc, el pc es un pc, si quiero usarlo tengo que ir al despacho) | Computación móvil (tengo un móvil que llevo donde quiero, el móvil es un pequeño pc) |

- HCI más natural (HCI implícita) - hacer desaparecer los elementos de la tecnología (ej. gafas y monturas)
  - Calm computer, no entra en conflicto con el entorno. Esta percepción cambia con la sociedad
- Reducción intervención humana = reducción complejidad percibida (incremento dependencia?)
  - A veces la necesidad intervención humana es un cuello de botella (ej. conducción autónoma, se cruza un peatón)
  - Cuestiones:
    - El usuario no percibe el sistema = El usuario no sabe si este está funcionando
    - El usuario no sabe por qué el sistema hace algo 

## CUIA 14/03

- Errores comunes:
  - Pensar que hay una única definición de CU - más que la definición, tenemos que entender el concepto y aplicarlo correctamente, con una visión o con otra: cada concepto nos va a llevar a una definición y unas propiedades distintas
  - Lo ideal es cumplir las 5 propiedades - habrá casos en los que sobre alguna, o no se cumpla al 100%
    - Ej. HCI más natural - el ejemplo al 100% sería interacción cerebro-máquina, lo cual no solo plantea problemas sino que puede ser muy variable - No siempre necesitamos el máximo de naturalidad, en tareas simples una forma muy explícita es más natural que liarla parda para hacerla menos "machine-like"
  - Los servicios ofrecidos deben tener siempre acceso ubicuo
    - Ej. en este aula tiene sentido que el control de la luz se controle desde dentro de la misma. No tiene sentido controlar la luz del aula desde mi casa. Los servicios que ofrece el aula ubicua no tienen por qué ser ubicuos en el mundo
  - Pensar que la computación reemplazará la interacción en los entornos físico y humano
    - Es trabajo moral de los desarrolladores no hacer dependiente al usuario de la tecnología
- Smart DEI: tres patrones de diseño
  - Dispositivos inteligentes - atención a la interacción de los dispositivos con el entorno virtual
    - Dispositivos personales, móviles - menos autonomía, dependen del usuario
  - Entornos inteligentes - dispositivos muy ligados al entorno físico

#### Redes de sensores

- No limitar los entornos inteligentes a las estructuras - ej. un olivar puede ser un entorno inteligente
- No es requisito que tengan una fuente de energía
- Entorno hostil factor determinante - no puedo garantizar la calidad de los nodos o de la red "no puedo poner todas mis esperanzas en que un determinado nodo esté bien"
- Consumo energético muy reducido, porque la mayoría de las veces va a tirar de baterías
- El nodo debe poder funcionar autónomamente, sin precisar de otros nodos, y adaptarse a "los nodos que queden vivos a su alrededor"
- No se pueden planificar "sobre el papel", bien sea por entorno hostil; o bien sea porque los sensores no se mantienen en el espacio. No podemos plantear con qué nodos se va a comunicar
  - Esto plantea que el nodo debe descubrir con qué nodo se puede comunicar
  - Aunque existe una estación base, varios nodos más deben tener capacidad de transmitir los datos fuera de la red 
- Reducción del costo - nodo que usamos, nodo que perdemos, no lo vamos a recuperar seguramente

## CUIA 21/03

Tipos de distorsión de las ondas:

- Atenuación - degradación, pérdida de energía con la distancia
  - Más grave en la señal digital que la analógica - por eso para larga/media distancia se transmiten señales analógicas
  - Reflexión y refracción - el medio por el que se transmite la onda magnética cambia de un medio a otro
  - Difracción - "rendija" 

## CUIA 28/03

- Los enlaces son propensos a error porque son muy cambiantes - por eso usamos código detector de errores
- Cuando el receptor recibe el paquete comprueba si hay errores - en tal caso, manda un paquete de vuelta y se le vuelve a envíar el paquete original
- Pero y si no llega a su destino, se pierde el paquete? El receptor espera eternamente, el emisor espera eternamente... se le pone un timeout - si se alcanza, se da por perdido el paquete y se vuelve a enviar
- Y si lo que se pierde es el paquete de confirmación? timeout
- y si los paquetes llegan con identificadores duplicados? o desordenados? Realmente eso no nos preocupa tanto porque los paquetes mandados por una red de sensores no suelen dividirse en varios paquetes - así que nos centraremos más en que no haya pérdidas ni errores
- Diferencia convergecast y unicast desde todos los nodos hacia la base - convergecast va acumulando de abajo a arriba así que es más eficiente enviar los paquetes acumulados que uno por cada nodo
- Métricas
  - Distancia geográfica - pero entonces los nodos necesitan un gps o algún modo de poder ubicarlos, pueden generarse bucles en la red de nodos... $$$
  - Número de saltos - calculamos al principio y periódicamente. Pero los saltos pueden ser muy grandes; además el hecho de que los nodos se pueden mover, cambiaría los resultados. Tampoco tiene en cuenta el estado actual de las conexiones entre los nodos
  - Tiempo











