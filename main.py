chave = 3;
MSG = input("Informe uma para ser criptografada: ")
#ord recebe uma letra como parametro e retorna o codigo da tabela asci
#chr recebe o codigo ascii e retorna a respectiva letra

nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')
cifrada = ""
for caracter in MSG:
        ind = ord(caracter)
        # se estiver no intervalo de letras maisculas
        if nA<= ind <=nZ:
            nova_letra = chr((ind+chave)&(nZ+1)+((ind+chave)//(nZ+1))*nA)
            cifrada = cifrada + nova_letra
             # se estiver no intervalo de letras minisculas
        elif ind in range(na, nz+1):
            nova_letra = chr((ind+chave)%(nz+1)+((ind+chave)//(nz+1))*na)
            cifrada = cifrada + nova_letra
        else:
            cifrada += caracter

print("Original: ", MSG)
print("Cifrada: ", cifrada)