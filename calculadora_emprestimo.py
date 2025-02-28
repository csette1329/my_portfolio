global pessoas
pessoas = {} # Dicionário que armazena o valor que cada pessoa deve receber ou pagar.

def calc_emprestimo(n, valor, participou):
    if participou:
        emprestimo = valor - valor/n
    else:
        emprestimo = valor
    return emprestimo

def contar_participantes(lista):
    return len(lista)

def registrar_compra(compra):
    n = contar_participantes(compra['participantes'])
    emprestimo = calc_emprestimo(n, compra['valor'], compra['pagante'] in compra['participantes'])
    for nome in compra['participantes']:
        if nome != compra['pagante']:
            pessoas[nome] += compra['valor']/n
    pessoas[compra['pagante']] -= emprestimo            
    return pessoas

def registrar_pessoas():
    while True:
        try:
            num_pessoas = int(input("Quantas pessoas participarão? "))
            break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    for i in range(num_pessoas):
        nome = input(f"Digite o nome da pessoa {i + 1}: ")
        pessoas[nome] = 0

def registrar_compras():
    num_compras = 1
    while True:
        participantes = input(f"Digite os participantes da compra {num_compras} separados por vírgula: ").split(", ")
        
        while True:
            try:
                valor = float(input(f"Digite o valor da compra {num_compras}: "))
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        
        pagante = input(f"Quem pagou a compra {num_compras}? ")
        compra = {'participantes': participantes, 'valor': valor, 'pagante': pagante}
        registrar_compra(compra)
        
        mais_compras = input("Deseja registrar mais uma compra? (s/n): ")
        if mais_compras.lower() != 's':
            break
        num_compras += 1

def mostrar_saldos():
    print("\nSaldos finais:")
    for pessoa, saldo in pessoas.items():
        print(f"{pessoa}: {saldo:.2f}")

def calcular_transacoes():
    credores = [(pessoa, saldo) for pessoa, saldo in pessoas.items() if saldo < 0]
    devedores = [(pessoa, saldo) for pessoa, saldo in pessoas.items() if saldo > 0]
    
    transacoes = []
    
    while credores and devedores:
        credor, valor_a_receber = credores.pop(0)
        devedor, valor_a_pagar = devedores.pop(0)
        
        valor_transacao = min(abs(valor_a_receber), valor_a_pagar)
        transacoes.append(f"{devedor} deve transferir {valor_transacao:.2f} para {credor}")
        
        novo_saldo_credor = valor_a_receber + valor_transacao
        novo_saldo_devedor = valor_a_pagar - valor_transacao
        
        if novo_saldo_credor < 0:
            credores.append((credor, novo_saldo_credor))
        if novo_saldo_devedor > 0:
            devedores.append((devedor, novo_saldo_devedor))
    
    print("\nTransações necessárias para quitar as dívidas:")
    for transacao in transacoes:
        print(transacao)

# Executa o registro das pessoas e compras
registrar_pessoas()
registrar_compras()
mostrar_saldos()
calcular_transacoes()
