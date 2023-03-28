*************************************************************************
***      Ejercicio 4 Laboratorio 3                                    ***
*************************************************************************

$ontext
  Las losas se nombraron con el alfabeto de manera que se representan
  de la siguiente manera:
         a b c d
         e f g h
         i j k l
         m n o p
         q r s t
$offtext

Sets
    i tubos /1,2,3,4,5,6,7/
    j losas /a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t/
;

Variables
    z        numero de losas a levantar
    losas(j) indicador de si se levanta la losa j
;

Parameters
    cubre(i, j) tabla que indica si levantar la baldosa j deja conocer el tubo i
;

cubre("1","a")=1;
cubre("1","e")=1;
cubre("2","e")=1;
cubre("2","i")=1;
cubre("3","b")=1;
cubre("3","c")=1;
cubre("3","f")=1;
cubre("3","g")=1;
cubre("4","i")=1;
cubre("4","j")=1;
cubre("4","m")=1;
cubre("4","n")=1;
cubre("5","j")=1;
cubre("5","k")=1;
cubre("5","n")=1;
cubre("5","o")=1;
cubre("6","m")=1;
cubre("6","q")=1;
cubre("7","s")=1;
cubre("7","t")=1;
cubre("7","p")=1;
cubre("7","l")=1;
cubre("7","h")=1;

Binary variable
    losas(j)
;

Equations
    nLosas        calculo de cantidad de losas a minimizar
    unaPorZona(i) Revisar que todos los tubos queden descubiertos
;

nLosas         .. z =e= sum(j, losas(j));
unaPorZona(i)  .. sum(j, cubre(i,j)*losas(j)) =g= 1;



Model modell /all/;
Option mip=CPLEX
Solve modell using mip minimizing z;

Display z.l;
Display losas.l;
