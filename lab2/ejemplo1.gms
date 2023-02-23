*************************************************************************
***     Problema de la Mochila                                        ***
***                                                                   ***
***      Autor: Germán Montoya                                        ***
*************************************************************************

Sets
  i   articulos / a1*a5 /


Scalar PESO_MAXIMO /10/;

Scalar GRAVEDAD /9.8/;

Parameter  valor(i)   valor de cada articulo i
                     /    a1 12, a2 5, a3 9, a4 6, a5 4  /;

Parameter  masa(i)   peso de cada articulo i
                     /    a1 0.91, a2 0.204, a3 0.714, a4 0.102, a5 0.306  /;

Parameter  peso(i);

loop(i,
    peso(i)=masa(i)*GRAVEDAD;

);


Variables
  x(i)        Indica si incluyo o no un articulo en la mochila.
  z           Objective function  ;

Binary Variable x(i);

*x.up(i,j)=1000;

Equations
objectiveFunction        objective function
res1                     res1;

objectiveFunction            ..  z =e= sum((i), valor(i) * x(i));

res1                         ..  sum(i, peso(i)*x(i)) =l= PESO_MAXIMO;


Model model1 /all/ ;
option mip=CPLEX
Solve model1 using mip maximizing z;

Scalar PESO_RESULTANTE /0/;

PESO_RESULTANTE=sum(i, peso(i)*x.l(i));

Display PESO_RESULTANTE;
Display x.l;
Display z.l;


