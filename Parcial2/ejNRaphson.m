clc, clear all, close all

syms f_x x;

f_x=3*x.^3 - 10*x.^2 - 56*x + 505;

figure
ezplot(f_x)
hold on;

x_i=-6;  %valor inicial

d1_f_x=diff(f_x); %primera derivada
d2_f_x=diff(d1_f_x); %segunda derivada

d1_f_x_i=double(subs(d1_f_x, x, x_i));

convergencia=0.001;  % convergencia

a=0.1;

cont=1;
while abs(d1_f_x_i)>convergencia
    cont=cont+1;       
    
    d1_f_x_i=double(subs(d1_f_x,x_i)); %Primera derivada evaluada en x_i
    
    d2_f_x_i=double(subs(d2_f_x,x_i)); %Segunda derivada evaluada en x_i
    
    x_i_new=x_i - a*(d1_f_x_i/d2_f_x_i); %Expresión de Newton Raphson: x(i+1) = x(i) - a*f'(x(i))/f''(x(i))
      
    x_i=x_i_new;  %Actualizamos el x_i
    
    f_x_i=double(subs(f_x,x_i)); %Evaluamos el x_i en la f(x) para graficar posteriormente
    
    plot(x_i, f_x_i, 'or')
    
end


y_coor=double(subs(f_x,x_i_new));

plot(x_i_new,y_coor,'o')
str2 = num2str(y_coor);
if d2_f_x_i <0
    text(x_i_new -0.3,y_coor+30,['maximo ',str2])
else
    text(x_i_new -0.3,y_coor-30,['minimo ',str2])
end
