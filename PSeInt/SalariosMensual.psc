Algoritmo SalariosMensual
	Definir CantHorasSemanales Como Entero;
	Definir PrecioHoraOrdinaria Como Entero;
	CantHorasSemanales <- 0;
	PrecioHoraOrdinaria <- 4833;
	Escribir 'Introduzca cuantas horas trabajo esta semana: ';
	Leer CantHorasSemanales;
	Si CantHorasSemanales <= 40 Entonces
		Escribir 'Tu sueldo este mes es de: ', (CantHorasSemanales*PrecioHoraOrdinaria)*4;
	SiNo
		HorasExtras <- (CantHorasSemanales-40);
		HorasConExtras <- (40*PrecioHoraOrdinaria)+(HorasExtras*PrecioHoraOrdinaria)*1.5;
		Escribir 'Tu sueldo este mes es de: ',HorasConExtras*4;
	Fin Si
FinAlgoritmo

