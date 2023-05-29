clc, clear all, close all

%Inicializacion de par�metros y variables
NMAX=100;
Na=0; %n�mero de llamadas
Nb=0; %n�mero de llamadas aceptadas
Nc=0; %n�mero de llamadas finalizadas
N_llamDen=0; %n�mero de llamdas denegadas
Free=1; %el callcenter est� disponible para atender llamadas.

%inicializaci�n del tiempo.
t=0;

%vectores para mostrar grafica al final de la simulaci�n
vec_t=[]; %almacena el valor del tiempo en cada iteraci�n
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
        if Free==1
            Free=0;

            Nb=Nb+1;

            newEvt.t=t+unidrnd(20);
            newEvt.type='C';
            evtQueue=[evtQueue newEvt];
            fprintf('Llamada aceptada. \n');

        end
        fprintf('Ocurre evento B: Atenci�n de la llamada \n');

    end

    if evtAct.type=='C'
        %Modificacion de variables
        Nc=Nc+1;
        Free=1;
        fprintf('Ocurre evento B: Finalizaci�n de la llamada \n');
    end

    vec_t=[vec_t t];
    porcLlamAcep=(Nb/Na)*100;
    vec_porcLlamAcep=[vec_porcLlamAcep porcLlamAcep];

    %Variables de estado actuales
    fprintf('T=%f -> Na=%d, Nb=%d, Free=%d PorcLlamAcep=%2d \n',t, Na, Nb, Free, porcLlamAcep);

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

figure
plot(vec_t,vec_porcLlamAcep, '-o')
title('Desempe�o del Callcenter');
xlabel('Tiempo [min]');
ylabel('% de aceptaci�n de llamadas');
ylim([0 110])


