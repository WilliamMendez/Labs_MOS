*************************************************************************
***      Ejercicio 3 Laboratorio 3                                    ***
*************************************************************************
Sets
    i canciones /1,2,3,4,5,6,7,8/
    j tipos /blues, randr/
;

Variables
    a(i) Indicador de si la cancion i esta en el lado A
    b(i) Indicador de si la cancion i esta en el lado B
    z duracion total de las canciones
;

Parameters
    t(i,j) tipos de las canciones
    d(i)   duraciones             /1 4,2 5,3 3,4 2,5 4,6 3,7 5,8 4/
;

Table t(i,j)
  blues  randr
1 1      0
2 0      1
3 1      0
4 0      1
5 1      0
6 0      1
7 0      0
8 1      1
;

Binary variable a(i);
Binary variable b(i);

Equations
objectiveFunction
noRepetir(i)
dosBluesA(j)
dosBluesB(j)
tresRockA(j)
condicion1
condicion2
limiteMenorA
limiteMenorB
limiteMayorA
limiteMayorB
;

objectiveFunction            ..       z =e=  sum(i, a(i)*d(i) + b(i)*d(i));
noRepetir(i)                 ..       a(i)+b(i) =l= 1                     ;
dosBluesA(j)$(ord(j)=1)      ..       sum(i, a(i)*t(i,j)) =e= 2           ;
dosBluesB(j)$(ord(j)=1)      ..       sum(i, b(i)*t(i,j)) =e= 2           ;
tresRockA(j)$(ord(j)=2)      ..       sum(i, a(i)*t(i,j)) =g= 3           ;
condicion1                   ..       1-a('5') =g= a('1')                 ;
condicion2                   ..       b('1') =g= a('2')+a('4')-1          ;
limiteMenorA                 ..       sum(i, a(i)*d(i)) =g= 14            ;
limiteMenorB                 ..       sum(i, b(i)*d(i)) =g= 14            ;
limiteMayorA                 ..       sum(i, a(i)*d(i)) =l= 16            ;
limiteMayorB                 ..       sum(i, b(i)*d(i)) =l= 16            ;

Model modell /all/;
Option mip=CPLEX
Solve modell using mip maximizing z;

Display z.l;
Display a.l;
Display b.l;




