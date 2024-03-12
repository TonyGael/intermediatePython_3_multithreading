# intermediate python #3: Multithreading

El multithreading en Python se refiere a la capacidad de ejecutar múltiples hilos de ejecución (threads) simultáneamente en un programa. Un hilo es una unidad básica de ejecución que puede realizar tareas de forma independiente. Python proporciona el módulo `threading` para trabajar con hilos.

Es importante tener en cuenta que, debido al Global Interpreter Lock (GIL) en la implementación de referencia de Python (CPython), los hilos en Python no logran paralelismo real en tareas intensivas en CPU. El GIL evita que varios hilos ejecuten instrucciones de Python simultáneamente. Sin embargo, el multithreading puede ser útil en situaciones en las que la concurrencia es más importante que el paralelismo, como cuando se trabaja con operaciones de entrada/salida (I/O) o tareas que no son intensivas en CPU.

A continuación, se muestra un ejemplo simple de cómo utilizar el módulo `threading` en Python:

```python
import threading
import time

def tarea_hilo(identificador):
    print(f"Hilo {identificador} iniciado.")
    time.sleep(2)
    print(f"Hilo {identificador} completado.")

# Crear dos hilos
hilo1 = threading.Thread(target=tarea_hilo, args=(1,))
hilo2 = threading.Thread(target=tarea_hilo, args=(2,))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen antes de continuar
hilo1.join()
hilo2.join()

print("Todos los hilos han terminado.")
```

Explicación del código:

- Se define una función `tarea_hilo` que simula una tarea que lleva tiempo completar.
- Se crean dos objetos `Thread` llamados `hilo1` y `hilo2`, que apuntan a la función `tarea_hilo`.
- Se inician los hilos llamando al método `start()`. Esto permite que los hilos comiencen a ejecutar la función `tarea_hilo` de forma concurrente.
- Se utiliza el método `join()` para esperar a que ambos hilos terminen antes de continuar con la ejecución del programa principal.
- Se imprime un mensaje indicando que todos los hilos han terminado.

Este es un ejemplo básico, y hay otras formas de trabajar con hilos en Python, como el uso de la clase `Thread` en combinación con la interfaz `Runnable` de `concurrent.futures`, o el uso de la biblioteca `asyncio` para programación asíncrona. La elección depende de los requisitos específicos de tu aplicación.

# args = (valor, )

En el código proporcionado, `args=(2,)` se refiere a los argumentos que se pasarán a la función `tarea_hilo` cuando se cree e inicie un nuevo hilo. El formato `(2,)` indica una tupla con un solo elemento, en este caso, el valor `2`. Es común utilizar una tupla incluso si solo hay un argumento para asegurar que sea un iterable.

En la función `threading.Thread(target=tarea_hilo, args=(2,))`, se crea un nuevo hilo (`Thread`) que ejecutará la función `tarea_hilo`. La tupla `(2,)` se pasa como argumento a la función cuando el hilo se inicie.

Dentro de la función `tarea_hilo`, este argumento se recibe como `identificador`. Por lo tanto, cuando el hilo con `args=(2,)` se inicie, el valor `2` se asignará a la variable `identificador` dentro de la función `tarea_hilo`.

En resumen, `args=(2,)` se utiliza para pasar el valor `2` como argumento a la función `tarea_hilo` cuando se crea e inicia el hilo. Es una forma de comunicar información específica a cada hilo en el momento de su creación.
