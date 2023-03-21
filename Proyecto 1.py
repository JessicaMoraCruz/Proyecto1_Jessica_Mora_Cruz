lista_de_profesores=[['N°','ID','       Nombre',' Cant.Est.','Años expe'],
                    [1,112340981,'Jose \t\t',      3,15],
                    [2,114560981,'Julio \t\t  ',2,5],
                    [3,113450876,'Axel \t\t   ',6,6],
                    [4,111230567,'Jessica \t',5,10],
                    [5,113450967,'Ernesto\t\t',4,8]]
b=''
for i in range(6):
    for j in range(5):
        b+=str(lista_de_profesores[i][j])+'\t'
    print (b)
    b=''