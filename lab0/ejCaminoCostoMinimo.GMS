
*************************************************************************
***      Minimizing the number of hops in a directed graph            ***
***                                                                   ***
***      Author: Germán Montoya                                       ***
*************************************************************************

Sets
  i   network nodes / n1*n5 /
alias(j,i);

Parameter  c(i,j)   costo;
c(i,j)=999;
c('n1','n2')=5;
c('n1','n3')=2;
c('n2','n5')=8;
c('n3','n4')=3;
c('n4','n5')=2;

Variables
  x(i,j)      Indicates if the link i-j is selected or not.
  z           Objective function  ;

Binary Variable x;

Equations
objectiveFunction        objective function
sourceNode(i)            source node
destinationNode(j)       destination node
intermediateNode         intermediate node;

objectiveFunction                                  ..  z =e= sum((i,j), c(i,j) * x(i,j));

sourceNode(i)$(ord(i) = 1)                         ..  sum((j), x(i,j)) =e= 1;

destinationNode(j)$(ord(j) = 5)                    ..  sum((i), x(i,j)) =e= 1;

intermediateNode(i)$(ord(i) <> 1 and ord(i) ne 5)  ..  sum((j), x(i,j)) - sum((j), x(j,i)) =e= 0;

Model model1 /all/ ;
option mip=cplex
Solve model1 using mip minimizing z;

Display c;
Display x.l;
Display z.l;

