'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json

def abrirJSON(arquivo):
    with open(arquivo, 'r') as arquivo:
        faturamento = json.load(arquivo)

    return faturamento

def faturamento(caminho_arquivo):
    arquivo = abrirJSON(caminho_arquivo)

    faturamento_valido = [dia['valor'] for dia in arquivo if dia['valor'] > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = len([dia['valor'] for dia in arquivo if dia['valor'] > media_faturamento])

    print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")