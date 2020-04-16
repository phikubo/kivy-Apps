# Program to create a calculator 
	
# Program to Show how to create a switch 
# import kivy module	 
import kivy 
import time
# base Class of your App inherits from the App class.	 
# app:always refers to the instance of your application 
from kivy.app import App 
	
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 


# for making multiple bttons to arranging 
# them we are using this 
from kivy.uix.gridlayout import GridLayout 

# for the size of window 
from kivy.config import Config 

# Setting size to resizable 
Config.set('graphics', 'resizable', 1) 
## Config.set('graphics', 'width', '400') 
## Config.set('graphics', 'height', '400') 


# Creating Layout class 
class Layout_calculadora(GridLayout): 

	# Function called when equals is pressed 
	def calcular(self, calculation): 
		if calculation: 
			try: 
				# Solve formula and display it in entry 
				# which is pointed at by display 
				self.display.text = str(eval(calculation)) 
			except Exception: 
				self.display.text = "Error"

	def filtrar(self, param):
		test="comando"
		if param:
			if param!=test:
				print(type(param), type(test))
				self.display1.text = "STATUS: Comando Invalido!"
			else:	
				print("filtrar")
				time.sleep(3)
				#proceso
				print("terminado filtrar")
				self.display1.text = "STATUS: Terminado. \n-ok (350, 350), -xA (50) -xB(39)"
			
		else:
			self.display1.text = "STATUS: Comando no especificado"
			#time.sleep(1)
			#self.display1.text = "STATUS: Ready"

	def comparar(self, param1, param2):
		if param1 and param2:
			print("comparar")
			time.sleep(3)
			#proceso
			print("terminado filtrar")
			self.display2.text = "STATUS: Terminado. \n Encontrado: 3 [ok] ---- 4 [nok]"
		else:
			self.display2.text = "STATUS: Lineas no especificadas"
			#time.sleep(1)
			#self.display2.text = "STATUS: Ready"
	
	

# Creating App class 
class CalculadoraApp(App): 
	def build(self): 
		return Layout_calculadora() 

# creating object and running it 


if __name__ == "__main__":
	calcApp = CalculadoraApp() 
	calcApp.run() 
else:
	pass
