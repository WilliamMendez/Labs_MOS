clc, clear all, close all

%% Inicio Graficar Nodos
% Posiciones de los nodos---------------------------------------------------            
nodesCoordinates=zeros(30,2);
nodesCoordinates(1,1)=34; nodesCoordinates(1,2)=14; nodesCoordinates(2,1)=34; nodesCoordinates(2,2)=10;
nodesCoordinates(3,1)=24; nodesCoordinates(3,2)=38; nodesCoordinates(4,1)=2; nodesCoordinates(4,2)=3;
nodesCoordinates(5,1)=1; nodesCoordinates(5,2)=28; nodesCoordinates(6,1)=24; nodesCoordinates(6,2)=5;
nodesCoordinates(7,1)=32; nodesCoordinates(7,2)=25; nodesCoordinates(8,1)=3; nodesCoordinates(8,2)=3;
nodesCoordinates(9,1)=6; nodesCoordinates(9,2)=32; nodesCoordinates(10,1)=4; nodesCoordinates(10,2)=10;
nodesCoordinates(11,1)= 10;nodesCoordinates(11,2)=5; nodesCoordinates(12,1)=35; nodesCoordinates(12,2)=28;
nodesCoordinates(13,1)=30; nodesCoordinates(13,2)=27; nodesCoordinates(14,1)=21; nodesCoordinates(14,2)=14;
nodesCoordinates(15,1)=27; nodesCoordinates(15,2)=5; nodesCoordinates(16,1)=6; nodesCoordinates(16,2)=1;
nodesCoordinates(17,1)=39; nodesCoordinates(17,2)=39; nodesCoordinates(18,1)=5; nodesCoordinates(18,2)=19;
nodesCoordinates(19,1)=27; nodesCoordinates(19,2)=12; nodesCoordinates(20,1)=31; nodesCoordinates(20,2)=23;
nodesCoordinates(21,1)=18; nodesCoordinates(21,2)=11; nodesCoordinates(22,1)=31; nodesCoordinates(22,2)=36;
nodesCoordinates(23,1)=30; nodesCoordinates(23,2)=17; nodesCoordinates(24,1)=38; nodesCoordinates(24,2)=11;
nodesCoordinates(25,1)=22; nodesCoordinates(25,2)=39; nodesCoordinates(26,1)=11; nodesCoordinates(26,2)=11;
nodesCoordinates(27,1)=38; nodesCoordinates(27,2)=3; nodesCoordinates(28,1)=12; nodesCoordinates(28,2)=24;
nodesCoordinates(29,1)=9; nodesCoordinates(29,2)=26; nodesCoordinates(30,1)=32; nodesCoordinates(30,2)=21;

RC = 10; % Radio de cobertura
for i=1:length(nodesCoordinates)
    for j=1:length(nodesCoordinates)
        
            dij=sqrt( ( nodesCoordinates(i,1)-nodesCoordinates(j,1) )^2+( nodesCoordinates(i,2)-nodesCoordinates(j,2) )^2);
            if(dij<=RC) & i~=j
                
                matrLinks(i,j)=dij;
                
                line([nodesCoordinates(i,1), nodesCoordinates(j,1)], [nodesCoordinates(i,2), nodesCoordinates(j,2)],'LineStyle',':', 'Color','k', 'LineWidth',1);
                hold on;
            else
                matrLinks(i,j)=inf;
            end
        
    end
end

for i=1:length(nodesCoordinates)
        x=nodesCoordinates(i,1);
        y=nodesCoordinates(i,2);
        plot(nodesCoordinates(i,1), nodesCoordinates(i,2), 'o', 'LineWidth',1,'MarkerEdgeColor','k', 'MarkerFaceColor','k', 'MarkerSize',7);
        text(x+1, y+0.5, num2str(i), 'FontSize',8, 'FontWeight', 'bold', 'Color','k');
        title('Red Celular')
        % axis([0 110 0 60])
end

%% Fin Graficar Nodos

%% SIMULADOR DE EVENTOS DISCRETOS
% Inicializacion de variables
inicio = 9;
final = 17;
visitados = containers.Map('KeyType','int32','ValueType','int32'); % Almacena el nodo por el que se llega más rápido al nodo llave
visitados(inicio) = inicio;
completo = 0;

% Inicialización del tiempo de simulación
t=0;

% Programacion del evento inicial o los eventos iniciales.
% Adiciono el evento inicial o los eventos iniciales a la cola de eventos.
evtQueue = [];
for i=1:length(nodesCoordinates)
    if matrLinks(inicio, i) < inf
        newEvt.t = matrLinks(inicio,i)*3.333333333;
        newEvt.type = 'A';
        newEvt.origen = inicio;
        newEvt.destino = i;
        evtQueue = [evtQueue newEvt];
    end
end
% Organizacion de la cola de eventos
flag=1;
while flag==1
    flag=0; 
    for i=1:(length(evtQueue)-1)
        if evtQueue(i).t>evtQueue(i+1).t
            temp=evtQueue(i);
            evtQueue(i)=evtQueue(i+1);
            evtQueue(i+1)=temp;
            flag=1; 
        end
    end
end
%Mostrado de la cola de eventos:
fprintf('\nCola de eventos:\n');
for i=1:length(evtQueue)
    fprintf('Evento %s en t=%f de %d a %d\n',evtQueue(i).type,evtQueue(i).t, evtQueue(i).origen, evtQueue(i).destino);
end
fprintf('----------------\n');
%pause(5);

% Desarrollo de la simulacion
while ~isempty(evtQueue) && completo == 0
    evtAct=evtQueue(1); 
    evtQueue(1)=[];
    
    t=evtAct.t;
    ori = evtAct.origen;
    des = evtAct.destino;
    
    % Procesamiento del evento A
    if evtAct.type=='A' && ~isKey(visitados, des)
        if inicio == final
            completo = 1;
        else        
            fprintf('Entra un evento A\n')
            evtAct.type='B';
            visitados(des) = ori;  
            plot(nodesCoordinates(des,1), nodesCoordinates(des,2), 'o', 'LineWidth',1,'MarkerEdgeColor','b', 'MarkerFaceColor','b', 'MarkerSize',7);
            fprintf('Se llego desde %d a %d\n', ori, des)
            %evtQueue = [evtQueue evtAct];
            if des == final
                completo = 1;
            end
        end
    end 
    
    % Procesamiento del evento B
    if evtAct.type=='B'
        fprintf('Entra un evento B\n')
        for i=1:30 
            dij = matrLinks(des, i);
            if dij<inf && isKey(visitados, i) == 0 && i~=ori
                % crear evento
                newEvt.t = t + (dij*3.3333);
                newEvt.origen = des;
                newEvt.destino = i;
                newEvt.type = 'A';
                evtQueue = [evtQueue newEvt];
                fprintf('Se agrega %d a %d\n', des, i);
                %pause(0.2)
            end
        end     
    end

    fprintf('T=%f\n',t);

       
    % Organizacion de la cola de eventos
    flag=1;
    while flag==1
        flag=0; 
        for i=1:(length(evtQueue)-1)
            if evtQueue(i).t>evtQueue(i+1).t
                temp=evtQueue(i);
                evtQueue(i)=evtQueue(i+1);
                evtQueue(i+1)=temp;
                flag=1; 
            end
        end
    end
    % Mostrado de la cola de eventos:
    fprintf('\nCola de eventos:\n');
    for i=1:length(evtQueue)
        fprintf('Evento %s en t=%f de %d a %d\n',evtQueue(i).type,evtQueue(i).t, evtQueue(i).origen, evtQueue(i).destino);
    end
    fprintf('----------------\n');
    % pause;
end

% Pintar la ruta tomada de rojo
completo = 0;
% pintar de rojo el final
plot(nodesCoordinates(final,1), nodesCoordinates(final,2), 'o', 'LineWidth',1,'MarkerEdgeColor','r', 'MarkerFaceColor','r', 'MarkerSize',7);
actual = visitados(final);
while completo ~= 1
    %fprintf('%d',actual);
    if actual == inicio
        completo =1;
    end
    plot(nodesCoordinates(actual,1), nodesCoordinates(actual,2), 'o', 'LineWidth',1,'MarkerEdgeColor','r', 'MarkerFaceColor','r', 'MarkerSize',7);
    actual = visitados(actual);
    %pause(0.5)
end

fprintf('Tiempo transcurrido para llegar a %d : %f  \n',final, t);
