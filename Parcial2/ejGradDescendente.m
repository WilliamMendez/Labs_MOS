
clc, clear all, close all

syms y x;

y=x^2;

figure

ezplot(y)
hold on;

%return;

x0=6;  %valor inicial

alfa=0.01;
N=10;

d_y=diff(y);
x0Buffer=[];

for i=1:N
    d_y=diff(y);
    d_y_eval=double(subs(d_y,x,x0));
    
    x0=x0-alfa*d_y_eval;
    
    x0Buffer=[x0Buffer x0];
    
    y_eval=double(subs(y,x,x0));
    plot(x0, y_eval, 'or')
    
    
end


