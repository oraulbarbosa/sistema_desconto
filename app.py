# SISTEMA DE DESCONTO PARA COMPRAS
# ============================================================
# Regras:
#   - Compras >= R$ 300,00: 15% de desconto
#   - Compras >= R$ 200,00: 10% de desconto
#   - Compras <  R$ 200,00: 5% de desconto
# ============================================================

# CONSTANTE 
FATOR_DESCONTO_15 = 0.85   # Paga 85% (15% de desconto)
FATOR_DESCONTO_10 = 0.90   # Paga 90% (10% de desconto)
FATOR_DESCONTO_5 = 0.95    # Paga 95% (5% de desconto)

# Percentuais de desconto (para exibir)
PERCENTUAL_DESCONTO_15 = 15
PERCENTUAL_DESCONTO_10 = 10
PERCENTUAL_DESCONTO_5 = 5

# ENTRADA DE DADOS
nome_cliente = input("Digite o nome do cliente: ") 
valor_compra = float(input("Digite o valor total da compra: ")) 

# PROCESSAMENTO DE DADOS
if valor_compra >= 300.00:
    valor_final = valor_compra * FATOR_DESCONTO_15 # Aplica 15% de desconto para compras acima de R$300;
    desconto_final = PERCENTUAL_DESCONTO_15
    
elif valor_compra >= 200.00:
    valor_final = valor_compra * FATOR_DESCONTO_10 # Aplica 10% de desconto para compras acima de R$200;
    desconto_final = PERCENTUAL_DESCONTO_10

else: 
    valor_final = valor_compra * FATOR_DESCONTO_5 # Aplica 5% de desconto para compras abaixo de R$199;
    desconto_final = PERCENTUAL_DESCONTO_5

# SAÍDA DE DADOS
print(f"Olá {nome_cliente}, o valor de desconto foi de {desconto_final}% e o valor para pagamento é de R$ {valor_final:.2f}.") 