# CONSIGNA
Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a cuántos billetes equivale, considerando que existen billetes de $1000, $500,
$200 y $100. Desarrollar el programa de tal forma que se minimice la cantidad de billetes
entregados por el cajero, teniendo en cuenta lo siguiente:

- La cantidad de billetes de que dispone el cajero es limitada. Por tal motivo lo primero
que deberá ingresarse al iniciar el programa es la cantidad de billetes de cada denominación que contiene el mismo. Ejemplo: 40 billetes de $1000, 150 billetes de $500, etc.

- Si se agotan los billetes de alguna denominación deberán entregarse billetes de la denominación inmediata inferior hasta completar la suma. Ejemplo: Si quedan sólo 2 billetes de $1000 y hay que entregar $4000, el programa indicará 2 billetes de $1000 y 4
de $500.

- Al ingresar la cantidad de dinero a entregar se deberá verificar que dicho importe pueda
ser efectivamente entregado con los billetes actualmente disponibles; en caso contrario
se imprimirá un mensaje de error y se solicitará otra cantidad. Ejemplo: Si no queda
ningún billete de $100 y el cliente solicita $300, se le informará que no es posible
entregar dicha suma, aunque el cajero disponga de más dinero en otras denominaciones. En otros casos, como si solicita $600 y no hay ninguno de $100, debe verificarse si no es posible entregar tres billetes de $200 antes de rechazar el importe.

- Repetir la lectura de montos y visualización de billetes a entregar hasta ingresar -1.

- Finalizada la operación se deberá mostrar un listado con todas las extracciones realizadas (monto total y cantidad entregada de billetes de cada denominación). Este listado
debe ordenarse de mayor a menor según el monto total suministrado.