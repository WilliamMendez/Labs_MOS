

*************************************************************************
***      Ejercicio 1 Laboratorio 2                                    ***
*************************************************************************

Sets
    i iterador origenes  /o1,o2,o3/
    j iterador destinos  /d1,d2/;

Variables
    x(i,j) cantidad de procesos que van del nodo i al j (Kernel)
    y(i,j) cantidad de procesos que van del nodo i al j (Usuario)
    z      costo total a minimizar

Parameters
    ofertaKernel(i)  /o1 60,o2 80,o3 50/
    ofertaUsuario(i) /o1 80,o2 50,o3 50/
    demandaUsuario(j) /d1 60,d2 120/
    demandaKernel(j) /d1 100, d2 90/;

Table costo(i,j)
         d1      d2
o1       300     500
o2       200     300
o3       600     300;

Positive variable x,y;

Equations
objectiveFunction               costo total del transporte
restriOfertaKernel(i)           restricci�n que desocupa cada procesador
restriDemandaKernel(j)          restricci�n que llena completamente cada procesador
restriOfertaUsuario(i)          restricci�n que desocupa cada procesador (Usuario)
restriDemandaUsuario(j)         restricci�n que llena completamente cada procesador (Usuario)
;

objectiveFunction            ..       z =e=  sum((i,j), costo(i,j)* x(i,j) + costo(i,j)*y(i,j));
restriOfertaKernel(i)        ..       sum(j, x(i,j)) =e= ofertaKernel(i) ;
restriDemandaKernel(j)       ..       sum(i, x(i,j)) =e= demandaKernel(j) ;
restriOfertaUsuario(i)       ..       sum(j, y(i,j)) =e= ofertaUsuario(i) ;
restriDemandaUsuario(j)      ..       sum(i, y(i,j)) =e= demandaUsuario(j) ;

Model modell /all/;
Option mip=CPLEX
Solve modell using mip minimzing z;

Display z.l;
Display x.l;
Display y.l;
