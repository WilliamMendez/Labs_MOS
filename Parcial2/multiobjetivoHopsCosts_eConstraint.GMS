*************************************************************************
***      Multiobjective case                                          ***
***                                                                   ***
***      Author: Germán Montoya                                       ***
*************************************************************************

Sets
  i   network nodes / n1, n2, n3, n4, n5 /

alias(j,i);

Table h(i,j) link capacity
                  n1       n2    n3     n4     n5
n1                999       1     1    999    999
n2                999     999   999    999      1
n3                999     999   999      1    999
n4                999     999   999    999      1
n5                999     999   999    999    999;

Table c(i,j) link cost
                 n1      n2      n3      n4      n5
n1               999     10      5       999     999
n2               999     999     999     999     10
n3               999     999     999     5       999
n4               999     999     999     999     5
n5               999     999     999     999     999;


Variables
  x(i,j)      Indicates if the link i-j is selected or not.

  z           Objective function

  f1          funcion 1
  f2          funcion 2;

Binary Variable x;

Equations
objectiveFunction        objective function
sourceNode(i)            source node
destinationNode(j)       destination node
intermediateNode         intermediate node
valor_f1                 resultado f1
valor_f2                 resultado f2
f1constraint             f1constraint

;

valor_f1                    ..      f1=e= sum((i,j), h(i,j) * x(i,j));

valor_f2                    ..      f2=e= sum((i,j), c(i,j) * x(i,j));

objectiveFunction           ..      z =e= f2;

sourceNode(i)$(ord(i) = 1)   ..  sum((j), x(i,j)) =e= 1;

destinationNode(j)$(ord(j) = 5)  ..  sum((i), x(i,j)) =e= 1;

intermediateNode(i)$(ord(i) <> 1 and ord(i) ne 5)
..  sum((j), x(i,j)) - sum((j), x(j,i)) =e= 0;

f1constraint                    ..  f1 =l= 5;

Model model1 /all/ ;

option mip=CPLEX;
Solve model1 using mip minimizing z;

display z.l;
display x.l;
display f1.l;
display f2.l;
