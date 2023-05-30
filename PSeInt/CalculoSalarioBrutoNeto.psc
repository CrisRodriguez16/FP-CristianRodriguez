Algoritmo CalculoSalarioBrutoNeto
	Definir NombreEmpleado Como Caracter;
	Definir CantHorasTrabajadas Como Real;
	Definir Impuestos Como Real;
	CantHorasTrabajadas <- 0;
	Escribir 'Nombre del trabajador: ';
	Leer NombreEmpleado;
	Escribir 'Cuantas horas trabajo: ';
	Leer CantHorasTrabajadas;
	Escribir 'Cuanto se paga en impuestos: ';
	Leer Impuestos;
	Escribir 'Para el empleado', NombreEmpleado ,' corresponde lo siguiente:';
	Escribir 'El salario bruto es: ',((CantHorasTrabajadas*4833)+Impuestos)*30;
	Escribir 'El salario neto es: ',((CantHorasTrabajadas*4833)-Impuestos)*30;
FinAlgoritmo
