Algoritmo sin_titulo
	Escribir "Ingrese la coordenada del eje X"
	Leer coordenada_x
	Escribir "Ingrese la coordenada Y"
	Leer coordenada_y
	Si coordenada_x > 0 & coordenada_y > 0 Entonces
		Escribir "El punto esta en el primer cuadrante"
	SiNo
		Si coordenada_x < 0 & coordenada_y > 0 Entonces
			Escribir "El punto esta en el segundo cuadrante"
		SiNo
			Si coordenada_x < 0 & coordenada_y < 0 Entonces
				Escribir "El punto esta en el tercer cuadrante"
			SiNo
				Si coordenada_x > 0 & coordenada_y < 0 Entonces
					Escribir "El punto esta en el cuarto cuadrante"
				SiNo
				Fin Si
			Fin Si
		Fin Si
		Escribir "El punto esta en el origen"
	Fin Si
FinAlgoritmo
