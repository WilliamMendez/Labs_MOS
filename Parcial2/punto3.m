clc, clear all

syms z x y;

z=(1-x)^2 + 100*(y-x^2)^2;

figure
ezsurf(z)
hold on;

i = 1;

salto = 0.8;
epsilon = 0.001;

x_i = 0;
y_i = 10;

grad_z = gradient(z);
grad_z_i = subs(subs(grad_z,x,x_i),y, y_i);

hess_z = hessian(z);

while abs(grad_z_i) > epsilon
    display(i);
    i = i+1;
    z_i = subs(subs(z,x,x_i),y,y_i);
    hess_z_i = subs(subs(hess_z,x,x_i),y,y_i);
    P_j = salto*((hess_z_i\grad_z_i));


    x_j = double(P_j(1));
    x_i1 = x_i - x_j;
    y_j = double(P_j(2));
    y_i1 = y_i - y_j;

    z_i1 = double(subs(subs(z,x,x_i1),y,y_i1));

    %display(x_i1)
    %display(y_i1)
    %display(z_i1)
    plot3([x_i,x_i1],[y_i,y_i1],[z_i,z_i1],'b-o');

    x_i = x_i1;
    y_i = y_i1;
    grad_z_i = subs(subs(grad_z,x,x_i),y, y_i);
end


plot3(x_i,y_i,z_i,'r-o')
str = num2str(x_i);
str2= num2str(y_i);
text(x_i,y_i,1,['Minimo x=',str,' y=',str2],"BackgroundColor",'white','HandleVisibility','on')

