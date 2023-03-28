*************************************************************************
***      Ejercicio 1 Laboratorio 3                                    ***
*************************************************************************
Sets
    i jugadores   /1,2,3,4,5,6,7/
    j habilidades /control, disparo, rebotes, defensa/
    k roles /ataque, centro, defensa/
;



Variables
    x(i)   Lista que representa si se escoje el jugador i
    z      Capacidad defensiva del equipo a maximizar

Parameters
c(i,j)        Clasificacion de los jugadores respecto a sus habilidades
r(i,k)        Roles que cumple el jugador i
necesarios(k) /ataque 2, centro 1, defensa 4/
promMin(j)    /control 2,disparo 2,rebotes 2,defensa 0/
;

Table c(i,j)
   control disparo rebotes defensa
1  3       3       1       3
2  2       1       3       2
3  2       3       2       2
4  1       3       3       1
5  3       3       3       3
6  3       1       2       3
7  3       2       2       1
;

Table r(i,k)
   ataque  defensa  centro
1  1       0        0
2  0       0        1
3  1       1        0
4  0       1        1
5  1       1        0
6  0       1        1
7  1       1        0
;

Binary variable x(i);

Equations
objectiveFunction(j)        Cantidad total de torres
njugadores               Restriccion que asegura que exista una cobertura
nDeCada(k)
promedios(j)
dosOTres
;

objectiveFunction(j)$(ord(j)=4)  ..    z =e=  sum((i), c(i,j)*x(i));
njugadores                       ..    sum(i, x(i)) =g= 5;
nDeCada(k)                       ..    sum(i, x(i)*r(i,k)) =g= necesarios(k);
promedios(j)                     ..    (sum(i, c(i,j)*x(i))/ sum(i, x(i))) =g= promMin(j);
dosOTres                         ..    x("2")+x("3") =l= 1;

Model modell /all/;
Option mip=CPLEX;
Solve modell using mip maximizing z;

Display z.l;
Display x.l;