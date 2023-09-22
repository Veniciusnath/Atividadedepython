def Categorias_contatos():
    
    Pessoal = 1
    Profissional = 2
    Romanticos = 3 
    
    print("\nOpções disponíveis:")
    print("1. Definir como Pessoal")
    print("2. Definir como Profissional")
    print("3. Definir como Romantico")
    
    opcao = input("Escolha uma opção (1/2/3/4/5): ")
    if opcao == "1":
        Pessoal()
    if opcao == "2":
        Profissional()
    if opcao == "3":
        Romanticos()
