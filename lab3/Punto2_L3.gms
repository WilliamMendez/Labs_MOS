*************************************************************************
***      Ejercicio 2 Laboratorio 3                                    ***
*************************************************************************
Sets
  i      jugadores    /p1*p6/
  alias(i,j)
;

Variables
  x(i)     Se escoje o no dadas las condiciones de tiempo
  z        Objective function;

table tp(i,j) tiempo entre pueblos

    p1  p2  p3  p4  p5  p6
p1  0   10  20  30  30  20
p2  10  0   25  35  20  10
p3  20  25  0   15  30  20
p4  30  35  15  0   15  25
p5  30  20  30  15  0   14
p6  20  10  20  25  14  0;


loop((i,j),
    if(tp(i,j) <= 15,
       tp(i,j) = 1;
    )
    if(tp(i,j) > 15,
       tp(i,j) = 0;
    )
)

Binary variable x;

Equations
objectiveFunction           objective function
restriccionTiempo(i)        restriccion del tiempo
;

objectiveFunction        ..  z =e= sum(i, x(i));
restriccionTiempo(i)     ..  sum(j, x(j)*tp(i,j))=g=1; 


Model model1 /all/ ;
option lp=CPLEX
Solve model1 using mip minimizing z;

Display z.l;
Display x.l;