

*************************************************************************
***      Ejercicio 4 Laboratorio 2                                    ***
*************************************************************************

sets
    nodos /1*7/;
alias(nodos, i, j);

parameters
    x(i)
    y(j)
    d(i,j);
    
d(i,j)=1e6;

* Coordenadas de los nodos
x("1") = 20; y("1") = 6;
x("2") = 22; y("2") = 1;
x("3") = 9;  y("3") = 2;
x("4") = 3;  y("4") = 25;
x("5") = 21; y("5") = 10;
x("6") = 29; y("6") = 2;
x("7") = 14; y("7") = 12;

* Cálculo de la matriz de distancias
loop((i,j)$(ord(i) < ord(j)),
    d(i,j) = sqrt(sqr(x(i)-x(j)) + sqr(y(i)-y(j)));
    d(j,i) = d(i,j);
)

* Costo inf para los nodos no conectados
loop((i,j),
    if(d(i,j) > 20,
       d(i,j) = 1e6;
    )
)

variables
    costo_total costo total de la ruta
    si_no(i,j)  existe una conexión entre los nodos
;
    
Binary variable si_no;

equations
    objetivo                funcion objetivo
    source_node(i)          source node                 
    destination_node(j)     destination node
    intermediate_node       intermediate node;


objetivo                                            .. costo_total =e= sum((i,j), d(i,j)*si_no(i,j));

source_node(i)$(ord(i)=4)                           .. sum(j, si_no(i,j)) =e= 1;

destination_node(j)$(ord(j)=6)                      .. sum(i, si_no(i,j)) =e= 1;

intermediate_node(i)$(ord(i)<>4 and ord(i) ne 6)    .. sum(j, si_no(i,j)) - sum(j, si_no(j,i)) =e= 0; 

* Resolución del modelo
Model modell /all/;
Option mip=CPLEX
Solve modell using mip minimzing costo_total;

display si_no.l, costo_total.l;
