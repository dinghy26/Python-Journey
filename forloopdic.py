student ={
'male':['Mauro','Greg','Zack'],
'female':['Mariana','Mare','Marta','Paula']
}

for key in student.keys():
    for name in student[key]:
        if 'M'in name:
            print(name)
           