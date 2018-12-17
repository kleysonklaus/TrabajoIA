from django.db import models
from django.utils import timezone

import sys

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

# Create your models here.



class tabla (models.Model):
	nombre = models.CharField(max_length=35)
	comida = models.PositiveSmallIntegerField()
	cantidad = models.PositiveSmallIntegerField()
	edad = models.PositiveSmallIntegerField()
	fecha_publicacion = models.DateTimeField(auto_now_add = True)
	def get_cantidad(self):
		return self.cantidad
	def get_comida(self):
		return self.comida
	def get_edad(self):
		return self.edad

	def datos(self):
		#datos = self.objects.all()
		#cadena="Dato->, {0}, {1}, {2}, {3}, {4}"
		#return cadena.format(self.nombre, self.comida,self.cantidad,self.edad,self.fecha_publicacion)
		#cadena="{0}, {1}, {2}, {3}"
		#return cadena.format(self.nombre, self.cantidad, self.comida, self.edad)		
		nuevo = [[self.cantidad,self.comida,self.edad]]

		n = [[70,50,10], [50,100,15],[24,20,41],
			[15,10,23], [15,15,20],[34,24,31],
			[52,54,19], [44,54,19],[38,25,42],
			[47,26,37], [51,46,52],[21,64,31],
			[60,30,20], [22,35,35],[50,49,30],
			[49,37,26], [44,45,19],[29,34,20],
			[31,33,50], [31,33,50],[46,29,18],
			[25,25,25], [23,20,40],[20,41,20],
			[20,35,20], [30,40,20],[15,34,30],
			[12,35,20], [45,70,22],[50,50,19],
			[12,30,21], [25,50,20],[6,40,20],
			[75,90,22], [30,50,20],[30,10,20],
			[18,20,25]]

		#SOLO FALTA CAMBIAR EL PARAMETRO "CADENA3" ,... POR LA MATRIZ DE TODOS LOS DATOS
		kmeans = KMeans(n_clusters=3).fit(n)
		centroids = kmeans.cluster_centers_

		#x_new =([[self.cantidad,self.comida,self.edad]])
		tarjeta = kmeans.predict(nuevo)
		if tarjeta == 0:
			cad = "{0} : le toca la tarjeta = {1}, CLIENTE BLACK"
			return cad.format(self.nombre,tarjeta)
		if tarjeta == 1:
			cad = "{0} : le toca la tarjeta = {1}, CLIENTE GRAY"
			return cad.format(self.nombre,tarjeta)
		if tarjeta == 2:
			cad = "{0} : le toca la tarjeta = {1}, CLIENTE BLUE"
			return cad.format(self.nombre,tarjeta)
        #return centroids

	def __str__(self):
		return self.datos()




"""
class Alumno (models.Model):
	ApellidoPaterno = models.CharField(max_length=35)
	ApellidoMaterno = models.CharField(max_length=35)
	Nombres = models.CharField(max_length=35)
	DNI = models.CharField(max_length=8)
	FechaNacimiento = models.DateField()
	SEXOS = (('F','femenino'),('M','masculino'))
	Sexo = models.CharField(max_length=1, choices=SEXOS,default='M')

	def NombreCompleto(self):
		cadena="{0} {1}, {2}"
		return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno,self.Nombres)

	def __str__(self):
		return self.NombreCompleto()

class Curso (models.Model):
	Nombre = models.CharField(max_length=50)
	Creditos = models.PositiveSmallIntegerField()
	Estado = models.BooleanField(default=True)

	def __str__(self):
		return "{0} ({1})".format(self.Nombre, self.Creditos)

class Matricula (models.Model):
	Alumno = models.ForeignKey (Alumno, null=False, blank=False, on_delete=models.CASCADE)
	Curso = models.ForeignKey (Curso, null=False, blank=False, on_delete=models.CASCADE)
	FechaMatricula = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Alumno, self.Curso.Nombre)

"""