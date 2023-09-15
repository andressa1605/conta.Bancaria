def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "tipo_de_conta": "corrente" 
    }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, tipo_de_conta, valor):
    if tipo_de_conta == "corrente" or tipo_de_conta == "poupanca":
        if conta["saldo"] >= valor:
            conta["saldo"] -= valor
        else:
            print("Saldo insuficiente.")
    else:
        print("Tipo de conta inválido. Tipos válidos: 'corrente' ou 'poupanca'.")

def extrato(conta):
    print(f"Numero da conta: {conta['numero']}")
    print(f"Saldo: R${conta['saldo']:.2f}")


minha_conta = cria_conta(13456, "Andressa", 2000.0, 300.0)
extrato(minha_conta) 
deposita(minha_conta, 900.0)
extrato(minha_conta) 
saca(minha_conta, "corrente", 600.0)
extrato(minha_conta)  
saca(minha_conta, "poupanca", 900.0)



