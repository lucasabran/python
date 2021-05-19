print("control de acceso")
edad_usuario=int(input("introduce tu edad por favor: "))
if edad_usuario<18:
	print("no puedes pasar")
elif edad_usuario>100:
	print("edad incorrecta")
else:
		print("puedes pasar")