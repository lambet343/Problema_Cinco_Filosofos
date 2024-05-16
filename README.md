# -- Problema de Sincronización de Procesos: Cinco Filósofos --
## Descripción del problema
El problema de los cinco filósofos es un clásico problema de sincronización y concurrencia en ciencia de la computación.
Fue presentado por primera vez por Edsger Dijkstra en 1965 como un ejemplo de una situación donde varios procesos compiten por un conjunto limitado de recursos compartidos, y cómo la sincronización entre ellos puede llevar a condiciones de carrera y bloqueo. 
El problema plantea una situación en la que cinco filósofos están sentados alrededor de una 
mesa redonda, y entre cada par de filósofos hay un tenedor. Cada filósofo necesita dos tenedores para comer, pero solo hay cinco tenedores disponibles, uno entre cada par de 
filósofos. Los filósofos pasan su tiempo alternando entre dos estados: pensando y comiendo. El problema surge cuando todos los filósofos intentan comer simultáneamente. Si cada 
filósofo toma el tenedor a su izquierda y espera a que el tenedor a su derecha esté disponible, pueden quedar atrapados en un estado de bloqueo mutuo, donde cada filósofo tiene 
un tenedor y espera el otro para comenzar a comer.

## Solución
Este código implementa una simulación utilizando **semáforos** en Python. Cada filósofo está representado por un hilo que alterna entre pensar y querer comer, y utiliza semáforos 
para controlar el acceso a los tenedores y evitar condiciones de carrera y bloqueo.
