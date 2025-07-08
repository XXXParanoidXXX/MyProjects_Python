# Verificação de Cartão de Cliente
# Este código verifica se o cliente possui um cartão e se o número do cartão é válido.
# O número do cartão deve ter exatamente 16 dígitos e ser composto apenas por números.
# Se o cliente não tiver um cartão, uma mensagem é exibida solicitando que ele solicite um cartão.
# Se o número do cartão for inválido, uma mensagem de erro é exibida.
# Se tudo estiver correto, uma mensagem de sucesso é exibida.

while True:
    nome_cliente = input("Digite o nome do cliente: ").strip()
    tem_cartao_input = input("Você tem cartão? (Sim/Nao) ").strip().lower()

    if tem_cartao_input == "sim":
        numero_cartao = input("Digite o número do cartão: ").strip()
        if len(numero_cartao) == 16 and numero_cartao.isdigit():
            print(f"Cartão de {nome_cliente} verificado com sucesso!")
            break  # Encerrar o programa com sucesso
        else:
            print("Número de cartão inválido. Deve conter exatamente 16 dígitos numéricos.\n")
            print("Reiniciando o processo...\n")
            continue  # Reiniciar o processo
    elif tem_cartao_input == "nao":
        print(f"{nome_cliente}, você não possui cartão.")
        print("Por favor, solicite um cartão para acessar os serviços.")
        break  # Encerrar o programa após exibir a mensagem
    else:
        print("Resposta inválida. Por favor, responda apenas com 'Sim' ou 'Nao'.\n")
        print("Reiniciando o processo...\n")

