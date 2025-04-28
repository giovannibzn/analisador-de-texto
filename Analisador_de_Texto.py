def analisar_texto(texto):
    linha = texto.splitlines()
    numero_linhas =len(linha)

    palavras = texto.split()
    numero_palavras = len(palavras)

    numero_caracteres = len(texto)

    return numero_linhas, numero_palavras, numero_caracteres

def main():
    print("Bem vindo ao analisador de texto")
    print("Digite seu texto abaixo, e para finalizar precione enter duas vezes")

    texto = ""
    while True:
        linha = input()
        if linha == "":
            break
        texto += linha + "\n"

    linha, palavra, caracteres = analisar_texto(texto)

    print("Resultado da análise: ")
    print(f"número de linhas: {linha}")
    print(f"número de palavras: {palavra}")
    print(f"número de caracteres: {caracteres}")

if __name__ == "__main__":
    main()