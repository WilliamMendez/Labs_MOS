

*************************************************************************
***      Ejercicio 2 Laboratorio 1                                    ***
*************************************************************************

Sets
    i iterador empleados  /1,2,3,4/
    j iterador trabajos   /1,2,3,4/;

Variables
    x(i,j) Se escoge el trabajo o no
    z      costo total a minimizar

Table costo(i,j)
    1   2   3   4
1   14  5   8   7
2   2   12  6   5
3   7   8   3   9
4   2   4   6   10
;

Binary Variable x;

Equations
objectiveFunction        costo total del transporte
restriUnaPorCadaEmpleado(i)      restriccion de trabajo por empleado
restriUnaPorCadaTrabajo(j)       restriccion de empleado por trabajo
;

objectiveFunction           ..  z =e= sum((i,j), costo(i,j)* x(i,j));
restriUnaPorCadaEmpleado(i) ..  sum(j, x(i,j)) =e= 1;
restriUnaPorCadaTrabajo(j)  ..  sum(i, x(i,j)) =e= 1;

Model modell /all/;
Option mip=CPLEX
Solve modell using mip minimzing z;

Display z.l;
Display x.l;