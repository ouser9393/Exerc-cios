"""
GERENCIADOR DE LISTA DE COMPRAS DA VOVÓ

Sua avó precisa de um programa para controlar suas compras mensais.
Ela quer:
1. Adicionar itens à lista
2. Marcar itens como comprados
3. Ver o que ainda falta comprar
4. Sair do programa

Crie um menu simples que atenda essas necessidades.
"""

def gerenciador_compras():
    lista_compras = []
    
    while True:
        print("\n--- LISTA DA VOVÓ ---")
        print("1. Adicionar item")
        print("2. Marcar como comprado")
        print("3. Ver lista atual")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            # TODO: Implementar adição de itens
            pass
        elif opcao == "2":
            # TODO: Implementar marcação como comprado
            pass
        elif opcao == "3":
            # TODO: Mostrar lista atual
            pass
        elif opcao == "4":
            print("Até a próxima compra!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Teste seu código aqui
# gerenciador_compras()