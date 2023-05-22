clc, clear all, close all

syms y x;

y = x^5-8*x^3+10*x+6;

encontrados = [];

salto = 0.1;
i = -2.5;

figure
fplot(y)
hold on;
xlim([-2.6 2.7]);
ylim([-10 21]);

while i <= 2.5
    minencontrado = nRaphsonMin(i);

    if abs(minencontrado) < 2.5 && minencontrado - i > 0
        if ~ismember(minencontrado, encontrados)
            encontrados = [encontrados, minencontrado];
            i = minencontrado;
            y_crit = double(subs(y,minencontrado));
            plot(i,y_crit,'or')
            str = num2str(y_crit);
            text(i,y_crit-1,str);
        end
    end

    maxencontrado = nRaphsonMax(i);
    if abs(maxencontrado) < 2.5 && maxencontrado - i > 0
        if ~ismember(maxencontrado, encontrados)
            encontrados = [encontrados, maxencontrado];
            i = maxencontrado;
            y_crit = double(subs(y,maxencontrado));
            plot(i,y_crit,'or')
            str = num2str(y_crit);
            text(i,y_crit+1,str);
        end
    end

    i = i+salto;
end

max_glob = double(subs(y,max(encontrados)));
min_glob = double(subs(y,min(encontrados)));

str_max = ['max = ',num2str(max_glob)];
str_min = ['min = ',num2str(min_glob)];

text(-2.5,-8,str_max);
text(-1,-8,str_min);

function resul = nRaphsonMax(x_i)
    syms y x;
    y = x^5-8*x^3+10*x+6;
    convergencia = 0.01;
    a = 0.005;
    d1_y=diff(y);  
    d1_y_i=double(subs(d1_y, x, x_i));
    avance = 1;
    while abs(d1_y_i)>convergencia && abs(x_i) < 2.5 && avance > 0
        d1_y_i=double(subs(d1_y,x_i)); %Primera derivada evaluada en x_i
        avance = a*(d1_y_i);
        x_i_new=x_i + avance; %Expresión de Newton Raphson: x(i+1) = x(i) - a*f'(x(i))/f''(x(i))
        x_i=x_i_new;  %Actualizamos el x_i

        %f_x_i=double(subs(y,x_i)); %Evaluamos el x_i en la f(x) para graficar posteriormente
        %plot(x_i, f_x_i, 'ob')
    end
    resul = x_i;
end

function resul = nRaphsonMin(x_i)
    syms y x;
    y = x^5 - 8*x^3 + 10*x + 6;
    convergencia = 0.01;
    a = 0.005;
    d1_y = diff(y);
    d1_y_i = double(subs(d1_y, x, x_i));
    avance = -1;
    while abs(d1_y_i) > convergencia && abs(x_i) < 2.5 && avance < 0     
        d1_y_i = double(subs(d1_y, x_i)); % Primera derivada evaluada en x_i
        avance = a * (d1_y_i);
        x_i_new = x_i - avance; % Expresión de Newton Raphson modificada: x(i+1) = x(i) + a*f'(x(i))/f''(x(i))
        x_i = x_i_new; % Actualizamos el x_i
        
        %f_x_i=double(subs(y,x_i)); %Evaluamos el x_i en la f(x) para graficar posteriormente
        %plot(x_i, f_x_i, 'ob')
    end
    resul = x_i;
end