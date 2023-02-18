
*************************************************************************
***      Problema de la mochila                                       ***
***      Authors: Daniel Aguilera y William Mendez                    ***
***      Codigos: 202010592 y 202012662                               ***
*************************************************************************

Sets
    i      elementos /e1, e2, e3, e4, e5/;

Variables
    z      Objective function
    x(i)      CogerNoCoger;
    
Scalar
    maxP       peso maximo /10/
    maxC       cantidad maxima /5/;
    

binary variable x;

Parameters
  elementos(i)   elemento     /e1 12, e2 5, e3 9, e4 6, e5 4/
  pesos(i)       peso         /e1 9, e2 2, e3 2, e4 1, e5 3/;


Equations
objectiveFunction        objective function
restriccionCantidad      restriccion de cantidad
restriccionPeso          restriccion de peso
;

objectiveFunction                                 ..  z =e= sum(i, elementos(i)*x(i));
restriccionCantidad                               ..  sum(i,x(i)) =l= maxC;
restriccionPeso                                   ..  sum(i,pesos(i) * x(i)) =l= maxP;



Model model1 /all/ ;
option mip=CPLEX
Solve model1 using mip maximizing z;

Display z.l;
Display x.l;