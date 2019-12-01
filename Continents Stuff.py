print('Continents\tArea(in miles)\tPopulation(in millions)')
print('-----------------------------------------')
n_a = ['North America' , 9540000 ,  579]
s_a = ['South America' , 6888000  , 423]
asia = ['Asia' , 17210000 , 4463]
eu = ['Europe' , 3931000 ,  741]
af = ['Africa' , 11730000 , 1216]
aus = ['Australia' , 2970000 ,  25]
an = ['Antartica' , 5405000 ,  0]
world = [n_a, s_a, asia, eu, af, aus, an]

for i in range(len(world)):
    for j in range(len(world[0])):
        print(world[i][j],end='\t')
    print()
