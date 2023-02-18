SETS
    i   Sources
        / S1, S2, S3 /
    j   Destinations
        / D1, D2, D3, D4, D5 / ;

PARAMETERS
    a(i)    Capacity of sources
            / S1 150, S2 200, S3 250 /
    b(j)    Demand of destinations
            / D1 100, D2 150, D3 75, D4 200, D5 125 /
    c(i,j)  Cost of transportation per unit
            / S1.D1 4, S1.D2 5, S1.D3 6, S1.D4 8, S1.D5 10,
              S2.D1 6, S2.D2 4, S2.D3 7, S2.D4 9, S2.D5 8,
              S3.D1 3, S3.D2 5, S3.D3 9, S3.D4 11, S3.D5 7 /;

VARIABLES
    x(i,j)  Amount shipped from sources to destinations 
    z;

POSITIVE VARIABLES x ;

EQUATIONS
    supply(i)       Limit on the amount produced at each source
    demand(j)       Limit on the amount consumed at each destination
    obj             Objective function ;

supply(i) ..       sum(j, x(i,j)) =l= a(i) ;
demand(j) ..       sum(i, x(i,j)) =g= b(j) ;
obj ..             sum((i,j), c(i,j)*x(i,j)) =e=z;

MODEL transportation /all/ ;

OPTION LP = CPLEX ;
TRANSPORTATION.OPTFILE = 1 ;
OPTION LP = CPLEX ;

SOLVE transportation USING LP MINIMIZING z ;

DISPLAY x.l, z
.l ;
