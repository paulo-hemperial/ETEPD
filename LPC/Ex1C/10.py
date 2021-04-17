gen = str(input('Qual é o seu genero? (F ou M) '))
if gen.lower() == 'f':
        print('Seu genero, é Feminino.')
elif gen.lower() == 'm':
        print('Seu genero é Masculino.')
else:
        print('Seu genero NÃO EXISTE!')
##Esse código não funciona se algum deficiente coloca seu genero como "não-binário".
