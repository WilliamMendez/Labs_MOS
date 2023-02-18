

*************************************************************************
***      Ejercicio 3 Laboratorio 1                                    ***
*************************************************************************

Sets
    i iterador origenes  /o1,o2,o3/
    j iterador destinos  /d1,d2,d3,d4/

Variables
    x(i,j) cantidad de procesos que van del nodo i al j
    z      costo total a minimizar

Parameters
    oferta(i)  /o1 300,o2 500,o3 200/
    demanda(j) /d1 200,d2 300,d3 100,d4 400/

Table costo(i,j)
         d1      d2      d3      d4
o1       8       6       10      9
o2       9       12      13      7
o3       14      9       16      5

Integer variable x

Equations
objectiveFunction        costo total del transporte
restriOferta(i)          restricci�n que desocupa cada procesador
restriDemanda(j)         restricci�n que llena completamente cada procesador
;

objectiveFunction                           ..    z =e= sum(i, sum(j, costo(i,j)* x(i,j)));
restriOferta(i)$(ord(i)>=1 and ord(i)<=3)   ..    sum(j, costo(i,j)) =e= oferta(i);
restriDemanda(j)$(ord(j)>=1 and ord(j)<=4)  ..    sum(i, costo(i,j)) =e= demanda(j);

Model modell /all/;
Option mip=CPLEX
Solve modell using mip minimzing z;

Display z.l;
Display x.l;
