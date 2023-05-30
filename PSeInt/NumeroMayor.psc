Algoritmo sin_titulo
	// Documentacion
	//Enunciado: Leer o capturar dos nueros por teclado, identificar el mayor e imprimirlo
	//Desarrollado por: Cristian Rodriguez
	//Version: 1.0
	//Fecha: 28-02-2023
		
	//Declaracion de Variables
	Definir v_Num1 Como Entero;
	Definir v_num2 Como Entero;
	
	//Inicializacion
	v_Num1 <- 0;
	v_num2 <- 0;
	
	//Lectura o captura de datos
	Escribir 'Escriba el primer numero: ';
	Leer v_Num1;
	Escribir 'Escriba el segundo numero: ';
	Leer v_Num2;
	
	//Procesos
	Si v_Num1 = v_Num2 Entonces
		Escribir 'Mi fai son iguales!';
	SiNo
		Si v_Num1 > v_Num2 Entonces
		Escribir 'El numero mayor es: ', v_Num1;
	SiNo 
		Escribir 'El numero mayor es: ', v_Num2;
	FinSi
	
	Fin Si
	
	//Salida
FinAlgoritmo
