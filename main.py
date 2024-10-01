from questoes.soma import soma
from questoes.fibonacci import fibonacci
from questoes.faturamento import faturamento
from questoes.distribuidora import distribuidora
from questoes.inverte import inverte

def main():
    print("\nDESAFIO TARGET\n")

    print(f"1 - Primeira questão:\nO valor da SOMA é de: {soma()}")

    print(f"\n2 - Segunda questão:")
    numero = int(input("Insira o número desejado: "))
    fibonacci(numero)

    print(f"\n3 - Terceira questão:")
    caminho_arquivo = 'dados/dados.json'
    faturamento(caminho_arquivo)

    print(f"\n4 - Quarta questão:")
    faturamento_cidades = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
    }
    distribuidora(faturamento_cidades)

    print(f"\n5 - Quinta questão:")
    string = input("Insira a string desejada: ")
    inverte(string)

if __name__ == "__main__":
    main()