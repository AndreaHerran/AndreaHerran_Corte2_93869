materias = ['calculo','estatica','programación','constitución','materiales','taller']
dia = ['martes','miercoles','jueves','viernes']
hora = ['7 a 9','9 a 11', '1 a 3', '3 a 5']
salon = ['307DB', '306DB','407DB', '303GO', '104PS']
profesor = ['Henry M', ' Elmer', 'David', 'Henry B', 'Jairo' ]
dato = ''
while dato != 'salir':
  dato = input('Ingrese el nombre de la materia: ')
  if dato == 'calculo':
        d = dia [0], dia [3]
        h = hora [0]
        s = salon [0]
        p = profesor [0]
        print(f'La materia {dato} se ve los días {d} de {h}, en el salon {s}, con el profesor {p}')
  elif dato == 'estatica':
        d = dia [0], dia [3]
        h = hora [1]
        s = salon [1]
        p = profesor [1]
        print(f'La materia {dato} se ve los días {d} de {h}, en el salon {s}, con el profesor {p}')
  elif dato == 'programación':
        d = dia [0], dia [3]
        h = hora [2]
        s = salon [3]
        p = profesor [2]
        print(f'La materia {dato} se ve los días {d} de {h}, en el salon {s}, con el profesor {p}')
  if dato == 'constitución':
        d = dia [1]
        h = hora [0]
        s = salon [2]
        p = profesor [3]
        print(f'La materia {dato} se ve los dia {d} de {h}, en el salon {s}, con el profesor {p}')
  if dato == 'materiales':
        d = dia [1], dia [3]
        h = hora [1]
        s = salon [2]
        p = profesor [1]
        print(f'La materia {dato} se ve los días {d} de {h}, en el salon {s}, con el profesor {p}')
  if dato == 'taller':
        d = dia [3]
        h = hora [3]
        s = salon [4]
        p = profesor [4]
        print(f'La materia {dato} se ve el dia {d} de {h}, en el salon {s}, con el profesor {p}')