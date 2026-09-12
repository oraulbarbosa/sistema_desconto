# 💰 Sistema de Desconto para Compras

O programa calcula o valor final de uma compra aplicando descontos progressivos conforme o valor gasto pelo cliente. 

## 🛠️ Tecnologias: 
<img width="48" height="48" alt="Image" src="https://github.com/user-attachments/assets/290dee08-55dc-467e-8e7a-c50aff5bb869" /> 
<img width="48" height="48" alt="Image" src="https://github.com/user-attachments/assets/6e49349f-02ce-4bb7-921b-c081ec378c88" /> 
<img width="48" height="48" alt="Image" src="https://github.com/user-attachments/assets/3f419076-3161-42c1-80a8-55ad8c3037ac" /> 

## 📋 Descrição

Este programa em Python ajuda você a:

- Calcular o **valor final** de uma compra com desconto
- Aplicar **descontos progressivos** conforme o valor gasto
- Exibir o **percentual de desconto** aplicado e o **valor a pagar**

## ⚡ Funcionalidades

- Solicita o **nome do cliente**
- Solicita o **valor total da compra**
- Verifica em qual **faixa de valor** a compra se encaixa
- Aplica o **desconto correspondente** (5%, 10% ou 15%)
- Calcula o **valor final a pagar** com desconto
- Exibe o **percentual de desconto** aplicado
- Exibe o **valor final formatado** em reais (R$)

## 🚀 Como Executar

**Pré-requisitos**
- Python 3.x instalado

**Passo a passo**

1. Clone o repositório:
    ```bash
    git clone https://github.com/oraulbarbosa/sistema_desconto.git
    ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema_desconto
   ```
3. Execute o programa:
   ```bash
   python app.py
   ```
4. Digite o nome do cliente e o valor da compra quando solicitado.

## ⚙️ Regras de Desconto

| Valor da Compra | Desconto | Valor Pago |
|-----------------|----------|------------|
| R$ 300,00 ou mais | 15% | 85% do valor |
| De R$ 200,00 a R$ 299,99 | 10% | 90% do valor |
| Abaixo de R$ 200,00 | 5% | 95% do valor |

## Exemplo 01

**Constantes utilizadas:**

Fatores de desconto:
- 0.85 (equivale a 15%) </br>
- 0.90 (equivale a 10%) </br>
- 0.95 (equivale a 5%) </br>

Percentual de desconto para visualização final: 
- 15 </br>
- 10 </br>
- 5 </br>

**Entrada:**

Qual o nome do cliente: Raul </br>
Qual o valor de compra: 300.00 </br>

**Processamento:**

O programa calcula percentual de desconto de acordo com a regra pré-estabelecida:

valor_final = 300.00 * 0.85 </br>

**Saída:**

Olá **Raul**, o valor de desconto foi de **15**% e o valor para pagamento é de R$ **255.00**. 

## Exemplo 02 

**Constantes utilizadas:**

Fatores de desconto:
- 0.85 (equivale a 15%) </br>
- 0.90 (equivale a 10%) </br>
- 0.95 (equivale a 5%) </br>

Percentual de desconto para visualização final: 
- 15 </br>
- 10 </br>
- 5 </br>

**Entrada:**

Qual o nome do cliente: Raul </br>
Qual o valor de compra: 200.00 </br>

**Processamento:**

O programa calcula percentual de desconto de acordo com a regra pré-estabelecida:

valor_final = 200.00 * 0.90 </br>

**Saída:**

Olá **Raul**, o valor de desconto foi de **10**% e o valor para pagamento é de R$ **180.00**.

## Exemplo 03

**Constantes utilizadas:**

Fatores de desconto:
- 0.85 (equivale a 15%) </br>
- 0.90 (equivale a 10%) </br>
- 0.95 (equivale a 5%) </br>

Percentual de desconto para visualização final: 
- 15 </br>
- 10 </br>
- 5 </br>

**Entrada:**

Qual o nome do cliente: Raul </br>
Qual o valor de compra: 150.00 </br>

**Processamento:**

O programa calcula percentual de desconto de acordo com a regra pré-estabelecida:

valor_final = 150.00 * 0.95 </br>

**Saída:**

Olá **Raul**, o valor de desconto foi de **5**% e o valor para pagamento é de R$ **142.50**.

## 👤 Autor 

**Raul Barbosa**

- GitHub: [@oraulbarbosa](https://github.com/oraulbarbosa)

## 📄 Licença

Este projeto está sob a licença MIT.
