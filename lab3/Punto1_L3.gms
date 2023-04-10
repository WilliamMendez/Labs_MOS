*************************************************************************
***      Ejercicio 2 Laboratorio 3                                    ***
*************************************************************************

Sets
  i      jugadores    /p1*p7/
  j      habilidades basquetbolistas  /cb, disp, reb, def/
  k      roles a jugar  /de, c, at/;

Variables
  x(i)   Se toma o no un jugador dadas las condiciones
  z      Objective function;

Parameters
  restricciones(k)  numeros por cada posicion /de 4, c 1, at 2/;


Table h(i,j) puntajes habilidades basquetbolistas
    cb  disp  reb  def
p1  3   3     1    3
p2  2   1     3    2
p3  2   3     2    2
p4  1   3     3    1
p5  3   3     3    3
p6  3   1     2    3
p7  3   2     2    1;

Table r(i,k) roles a jugar
    de  c     at
p1  0   0     1
p2  0   1     0
p3  1   0     1
p4  1   1     0
p5  1   0     1
p6  1   1     0
p7  1   0     1;


Binary variable x;

Equations
objectiveFunction           objective function
restriccionLJ               restriccion del limite de jugadores
restriccionDef              restriccion del limite de jugadores de rol defensa
restriccionAt               restriccion del limite de jugadores de rol ataque
restriccionC                restriccion del limite de jugadores de rol central
restruccionJugadores2y3     restriccion de que solo 1 de los jugadores 2 y 3 puede ser titular
restriccionPromedio(j)      restriccion promedio;

;

objectiveFunction        ..  z =e= sum(i, h(i,"def")*x(i));
restriccionLJ            ..  sum(i, x(i))=e=5;
restriccionDef           ..  sum(i, x(i)*r(i,"de"))=g=restricciones("de");
restriccionAt            ..  sum(i, x(i)*r(i,"at"))=g=restricciones("at");
restriccionC             ..  sum(i, x(i)*r(i,"c"))=g=restricciones("c");
restriccionPromedio(j)   ..  sum(i, x(i)*h(i,j))/5=g=2;
restruccionJugadores2y3  ..  x("p2") + x("p3") =e= 1;


Model model1 /all/ ;
option lp=CPLEX
Solve model1 using mip maximizing z;

Display z.l;
Display x.l;
