Algoritmo SumaParesDosYCien
	Definir contador Como Real;
	Definir SumContador Como Real;
	contador <- 2;
	SumContador <- 0;
	Repetir
		contador <- contador+2
		SumContador <- SumContador+contador;
		Escribir ' - ',contador;
	Hasta Que contador = 100;
	Escribir 'La suma de los numeros pares entre 2 y 100 es: ', SumContador;
FinAlgoritmo
