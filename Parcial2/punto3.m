clc, clear all, close all

syms z x y;

z=(1-x)^2 + 100*(y-x^2)^2;

figure
ezsurf(z)
hold on;

i = 1;

salto = 1;
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
    P_j = salto*((inv(hess_z_i)*grad_z_i));

    x_j = double(P_j(1));
    x_i = x_i - x_j;
    y_j = double(P_j(2));
    y_i = y_i - y_j;

    z_j = subs(subs(z,x,x_j),y,y_j);
    plot3([x_i,x_j],[y_i,y_j],[z_i,z_j],'b-o');

    grad_z_i = subs(subs(grad_z,x,x_i),y, y_i);
end



