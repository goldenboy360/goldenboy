# Cria o alfabeto minúsculo e maiúsculo
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = alfabeto_minusculo.upper()

print("Alfabeto Minúsculo:", alfabeto_minusculo)
print("Alfabeto Maiúsculo:", alfabeto_maiusculo)

def embaralhar(letra, lista):
    posicao = lista.find(letra)
    # Subtrai 13 da posição original para achar a nova letra
    return lista[posicao - 13]

def criptografar_texto(texto):
    resultado = ""

    for letra in texto:
        if letra in alfabeto_minusculo:
            resultado += embaralhar(letra, alfabeto_minusculo)
        elif letra in alfabeto_maiusculo:
            resultado += embaralhar(letra, alfabeto_maiusculo)
        else:
            # Mantém espaços, números e acentos sem alterar
            resultado += letra

    return resultado

# Teste rápido
mensagem_secreta = criptografar_texto("Caio")
print("Texto criptografado:", mensagem_secreta)

# Caixas de entrada para o aluno testar em tempo real
mensagem_usuario = input("Digite uma frase secreta para codificar: ")
mensagem_codificada = criptografar_texto(mensagem_usuario)

print("\n🔒 Mensagem Codificada:", mensagem_codificada)

# O legal do ROT13 é que rodar o código de novo na mensagem codificada revela o texto original!
mensagem_decodificada = criptografar_texto(mensagem_codificada)
print("🔓 Revelando a Mensagem:", mensagem_decodificada)