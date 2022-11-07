a = 8        
mas = ['.'] * 8 
for i in range(a): 
    mas[i] = ['.'] * a
mas[7][7] = 'aa'
print(mas[7][7])
