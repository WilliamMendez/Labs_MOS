clc, clear all, close all

%Inicializacion de parámetros y variables
NMAX=100;
Na=0; %número de llamadas
Nb=0; %número de llamadas aceptadas
Nc=0; %número de llamadas finalizadas
N_llamDen=0; %número de llamdas denegadas

Free=6; %el callcenter está disponible para atender n llamadas, este valor se modifica para representar el número de teléfonos.
% Aunque con n = 4 se puede conseguir en algunos casos un porcentaje de 100
% este no es consistente, por lo que se sube a 5
% Con n = 5 se puede conseguir un porcentaje de 100 en más ejecuciones pero
% aún no es completamente asegurado conseguirlo cada vez que se simula.
% Con n = 6 se observa que es suficiente para asegurar un porcentaje de 100
% en todas las simulaciones

%inicialización del tiempo.
t=0;

%vectores para mostrar grafica al final de la simulación
vec_t=[]; %almacena el valor del tiempo en cada iteración
vec_porcLlamAcep=[]; %almacena el porcentaje de llamadas aceptadas a medida que avanza el tiempo

%Programacion del evento inicial
evt.t=unidrnd(10);
evt.type='A';

%Programacion en la cola de eventos
evtQueue=evt;

%Desarrollo de la simulacion
while length(evtQueue)>0
    evtAct=evtQueue(1);
    evtQueue(1)=[];

    t=evtAct.t;

    %Procesamiento del evento
    if evtAct.type=='A'
        %Modificacion de variables
        Na=Na+1;

        %Programacion de nuevos eventos
        newEvt.t=t;
        newEvt.type='B';
        evtQueue=[evtQueue newEvt];
        if Na<NMAX
            newEvt.t=t+unidrnd(10);
            newEvt.type='A';
            evtQueue=[evtQueue newEvt];
        end
        fprintf('Ocurre evento A: Llamada nueva \n');
    end

    if evtAct.type=='B'
        %Modificacion de variables
        if Free>0
            Free= Free-1;

            Nb=Nb+1;

            newEvt.t=t+unidrnd(20);
            newEvt.type='C';
            evtQueue=[evtQueue newEvt];
            fprintf('Llamada aceptada. \n');
        else
            N_llamDen = N_llamDen + 1;
        end
        fprintf('Ocurre evento B: Atención de la llamada \n');

    end

    if evtAct.type=='C'
        %Modificacion de variables
        Nc=Nc+1;
        Free=Free+1;
        fprintf('Ocurre evento C: Finalización de la llamada \n');
    end

    vec_t=[vec_t t];
    porcLlamAcep=((Na-N_llamDen)/Na)*100;
    vec_porcLlamAcep=[vec_porcLlamAcep porcLlamAcep];

    %Variables de estado actuales
    fprintf('T=%f -> Na=%d, Nb=%d, Nc=%d, Free=%d PorcLlamAcep=%2d \n',t, Na, Nb, Nc, Free, porcLlamAcep);

    %Organizacion de la cola de eventos
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
        fprintf('Evento %s en t=%f\n',evtQueue(i).type,evtQueue(i).t);
    end
    fprintf('----------------\n');
    %pause(1);
end




