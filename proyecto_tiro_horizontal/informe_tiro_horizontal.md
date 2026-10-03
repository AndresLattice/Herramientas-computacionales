# Movimiento de un proyectil: tiro parabólico horizontal

**Integrante:** Andrés Agudelo

**Materia:** Herramientas computacionales

**Profesor:** Hernán Restrepo

## Introducción

Este trabajo trata sobre el tiro parabólico horizontal. Es cuando algo se lanza de lado desde una altura y cae haciendo una curva. Me basé en el video "Tiro parabólico horizontal" del canal Vitual, donde se resuelve el problema de un objeto lanzado horizontalmente desde una altura. 

## Planteamiento del problema

> Un arquero que se encuentra en la cima de una torre dispara una flecha horizontalmente con una velocidad de 175 m/s. Si la altura desde la cual se dispara es de 115 m, calcula el tiempo que tarda en caer y la distancia a la que llega la flecha.

Video: "Tiro parabólico horizontal" – https://www.youtube.com/watch?v=7PHLOFylz_I

### Datos

- Velocidad inicial en X: $v_{ix} = 175\ \text{m/s}$
- Velocidad inicial en Y: $v_{iy} = 0$ (se dispara horizontalmente)
- Posición inicial: $y_i = 115\ \text{m}$
- Posición final: $y_f = 0$ (cuando llega al suelo)
- Aceleración: $a = g = -9{,}81\ \text{m/s}^2$ (negativa porque la gravedad apunta hacia abajo)
- Piden: el tiempo que tarda en caer ($t$) y la distancia horizontal ($d$)

## Marco teórico

### Movimiento de proyectil

Es el movimiento de un cuerpo lanzado al aire sobre el que solo actúa la gravedad. Su trayectoria es una parábola. En este tipo de movimiento, la parte horizontal y la vertical solo comparten el tiempo.

El tiro puede ser **oblicuo**, si se lanza con un ángulo distinto de 0°, u **horizontal**, si se lanza a 0° desde una altura. Este trabajo trata el caso horizontal.

### Condiciones y sistema de referencia

Se ignora la resistencia del aire y la gravedad se toma constante. El origen está en el suelo, debajo del punto de lanzamiento, con el eje Y positivo hacia arriba. Por eso la gravedad es negativa: $a = -9{,}81\ \text{m/s}^2$.

### Ecuaciones

**Eje X.** No hay aceleración, así que la velocidad es constante (MRU). La velocidad es la distancia recorrida dividida entre el tiempo:

$$v_x = \frac{d}{t} \quad \Rightarrow \quad d = v_x \, t$$

**Eje Y.** La gravedad acelera el objeto de forma constante (MRUA). La posición vertical cambia con el tiempo así:

$$y_f = y_i + v_{iy}\,t + \tfrac{1}{2} a t^2$$

Donde $y_i$ es la altura inicial, $y_f$ la altura final, $v_{iy}$ la velocidad vertical inicial y $a$ la gravedad.

**Tiempo de caída.** 

$$t^2 = \frac{-2 y_i}{a} \quad \Rightarrow \quad t = \sqrt{\frac{-2 y_i}{a}}$$


## Desarrollo del ejercicio

### Paso 1: Tiempo que tarda en caer

Se reemplazan la altura y la gravedad en la fórmula del tiempo:

$$t = \sqrt{\frac{-2\,(115\ \text{m})}{-9{,}81\ \text{m/s}^2}} \approx 4{,}84\ \text{s}$$

### Paso 2: Distancia horizontal

Como la velocidad horizontal no cambia, se multiplica por el tiempo de caída:

$$d = v_x \, t = (175\ \text{m/s})(4{,}84\ \text{s}) \approx 847\ \text{m}$$

Con el tiempo sin redondear (4,8421 s) da 847,36 m, que también se aproxima a 847 m.
### Resultados

| Magnitud | Resultado |
|---|---|
| Tiempo que tarda en caer | ≈ 4,84 s |
| Distancia horizontal | ≈ 847 m |

## Conclusión

El tiro horizontal se separa en un movimiento horizontal con velocidad constante y uno vertical acelerado por la gravedad. Con $a = -9{,}81\ \text{m/s}^2$, igual que en el video, la flecha tarda unos 4,84 segundos en caer y llega a unos 847 metros.

## Referencias

- Vitual. (22 de enero de 2017). *Tiro parabólico horizontal* [Video]. YouTube. https://www.youtube.com/watch?v=7PHLOFylz_I
- Serway, R. A. Física para ciencias e ingeniería (capítulo de movimiento en dos dimensiones).
