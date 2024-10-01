'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP: R$67.836,43
• RJ: R$36.678,66
• MG: R$29.229,88
• ES: R$27.165,48
• Outros: R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
'''

def distribuidora(faturamento):
    
    valor_total = sum(faturamento.values())

    for estado, valor in faturamento.items():
        percentual = (valor / valor_total) * 100
        print(f"Estado: {estado} - Percentual de representação: {percentual:.2f}%")