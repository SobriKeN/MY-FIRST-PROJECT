# Parte1:Correção do documento

def corrigir_palavra (codigo):
    """
    1.1-Corrigir a palavra: string --> string. Esta função recebe uma cadeia de caracteres que representa uma palavra
    e nos dá a mesma palavra só que corrigida através da aplicação de reduções sugerida.
    """
    lista = list(codigo)
    i = 0
    tamanho = len(lista)
    while i < tamanho-1:
        if str(lista[i]) == str(lista[i+1]).upper() or str(lista[i]).upper() == str(lista[i+1]):
            del lista[i:i+2]
            i = 0
            tamanho = tamanho-2
        else:
            i = i+1
    codigo_resolvido =''.join(lista)
    return codigo_resolvido

def eh_anagrama(codigo1,codigo2):
    """
    1.2-Verificar se é anagrama: string,string --> booleano. Esta função recebe duas cadeias de caracteres e devolve
    True apenas se uma for anagrama da outra(isto é, se as palavras são constituídas pelas mesmas letras) onde é
    ignorada diferenças entre maisculas e minusculas.
    """
    codigo_arranjado1 = sorted(str.upper(codigo1))
    codigo_arranjado2 = sorted(str.upper(codigo2))
    i=0
    if len(codigo_arranjado1) != len(codigo_arranjado2):
        return False
    while i < len(codigo_arranjado1):
        if codigo_arranjado1[i] == codigo_arranjado2[i]:
            i += 1
        else:
            return False
    return True

def corrigir_doc(documento):
    """
    1.3-Corrigir o documento: string --> string. Esta função recebe uma cadeia de caracteres e devolve essa mesma cadeia
    mas corrigida através de aplicação de reduções e verificação de anagramas, levantando erro se receber um argumento
    inválido.
    """
    i1 = 0
    if type(documento) != str:
        raise ValueError('corrigir_doc: argumento invalido')
    if '  ' in documento or documento == '':
        raise ValueError('corrigir_doc: argumento invalido')
    lista_verificacao = list(documento)
    t1 = len(lista_verificacao)
    while i1 < t1:
        if ord(lista_verificacao[0])==32:
            raise ValueError('corrigir_doc: argumento invalido')
        if 65<=ord(lista_verificacao[i1])<=90 or 97<=ord(lista_verificacao[i1])<=122 or ord(lista_verificacao[i1])==32:
            i1 +=1
        else:
            raise ValueError('corrigir_doc: argumento invalido')
    documento_corrigido = corrigir_palavra(lista_verificacao)
    lista_corrigida = documento_corrigido.split()
    t2 = len(lista_corrigida)
    i2 = 0
    e2 = 0
    while i2 <= t2-1:
        while e2 <= t2-1:
            if lista_corrigida[i2] == lista_corrigida[e2]:
                e2 += 1
            elif eh_anagrama(lista_corrigida[i2],lista_corrigida[e2]) and \
                 lista_corrigida[i2].lower() != lista_corrigida[e2].lower():
                del lista_corrigida[e2]
                t2 -= 1
                e2 += 1
            else:
                e2 += 1
        i2 += 1
        e2 = 0
    documento_totalmente_corrigido = ' '.join(lista_corrigida)
    return documento_totalmente_corrigido

# Parte2:Descoberta do PIN:

def obter_posicao(codigo,inteiro):
    """
    2.1- Obter a posição: string, inteiro --> inteiro. Esta função recebe uma cadeia de caracteres de tamanho 1
    representando a direção do movimento e um numero que é a posição inicial antes do movimentoe devolve um inteiro que
    corresponde à posição após o movimento dado.
    """
    if 1<=inteiro<=9:
        if codigo == 'C' and (inteiro == 1 or inteiro == 2 or inteiro == 3):
            return inteiro
        elif codigo == 'B' and (inteiro == 7 or inteiro == 8 or inteiro == 9):
            return inteiro
        elif codigo == 'E' and (inteiro == 1 or inteiro == 4 or inteiro == 7):
            return inteiro
        elif codigo == 'D' and (inteiro == 3 or inteiro == 6 or inteiro == 9):
            return inteiro
        elif codigo == 'C':
            return inteiro - 3
        elif codigo == 'B':
            return inteiro + 3
        elif codigo == 'E':
            return inteiro - 1
        elif codigo == 'D':
            return inteiro + 1

def obter_digito(codigo,inteiro):
    """
    2.2-Obter o digito: string,inteiro --> inteiro. Esta função recebe uma cadeia de caracteres contendo uma sequência
    de movimentos e um inteiro contendo a posição inicial e devolve um inteiro que representa a posição final após
    todos os movimentos.
    """
    lista_codigo = list(codigo)
    i = 0
    tamanho = len(lista_codigo)
    while i < tamanho:
        if ord(lista_codigo[i]) > 69 or ord(lista_codigo[i]) < 66:
            raise ValueError('obter_pin: argumento invalido')
        inteiro = obter_posicao(lista_codigo[i],inteiro)
        i += 1
    return inteiro

def obter_pin (tuplo):
    """
    2.3-Obter o PIN: tuplo --> tuplo. Esta função recebe um tuplo contendo entre 4 a 10 sequências de movimentos e
    devolve um tuplo de inteiros contendo o código PIN, levantando erro se receber alguma informação incorreta.
    """
    if type(tuplo) != tuple:
        raise ValueError('obter_pin: argumento invalido')
    if len(tuplo) > 10 or len(tuplo) < 4:
        raise ValueError('obter_pin: argumento invalido')
    for e in range(len(tuplo)):
        if tuplo[e] == '':
            raise ValueError('obter_pin: argumento invalido')
    lista_combinacao = list(tuplo)
    lista_pin = []
    for i in range (len(lista_combinacao)):
        if i == 0:
            elemento_pin = obter_digito(lista_combinacao[i],5)
            lista_pin = lista_pin + [elemento_pin]
        else:
            elemento_pin = obter_digito(lista_combinacao[i], lista_pin[i-1])
            lista_pin = lista_pin + [elemento_pin]
    tuplo_pin = tuple(lista_pin)
    return tuplo_pin

#Parte3:Filtrar a BDB:

def eh_entrada(entrada):
    """
    3.1/4.1-verificar a entrada: universal --> booleano. Esta função recebe uma entrada qualquer e devolve True se
    corresponder a uma entrada BDB.
    """
    if type(entrada) != tuple:
        return False
    if len(entrada) != 3:
        return False
    if type(entrada[1]) != str:
        return False
    if type(entrada[2]) != tuple:
        return False
    for t in range(0, len(entrada)):
        lista_cifra = list(entrada[0])
        lista_checksum = list(entrada[1])
        lista_numeros = list(entrada[2])
        if len(lista_cifra) == 1:
            return False
        for i in range(0, len(lista_cifra)):
            if 97 > ord(lista_cifra[i]) > 45 or ord(lista_cifra[i]) > 122 or ord(lista_cifra[i]) < 45:
                return False
            if lista_cifra[0] == '-' or lista_cifra[len(lista_cifra)-1] == '-':
                return False
            if lista_cifra[i] == '-' and lista_cifra[i+1] == '-':
                return False
        if len(lista_checksum) != 7:
            return False
        for i in range(0, len(lista_checksum)):
            if type(lista_checksum[i]) != str or 48 <= ord(lista_checksum[i]) <= 57:
                return False
            if 93 < ord(lista_checksum[i]) < 97 or ord(lista_checksum[i]) > 122 or 91< ord(lista_checksum[i]) <93:
                return False
            if lista_checksum[0] != '[' or lista_checksum[len(lista_checksum)-1] != ']':
                return False
        if len(lista_numeros) < 2:
            return False
        for i in range(0, len(lista_numeros)):
            if type(lista_numeros[i]) != int:
                return False
            if lista_numeros[i] < 0:
                return False
        return True

def validar_cifra (cifra,checksum):
    """
    3.2-Validar a cifra- string,string --> booleano. Esta função recebe duas cadeias de caracteres(uma cifra e uma
    sequência de controlo) e devolve True se a sequência de controlo tiver de acordo com a cifra.
    """
    cifra_lista = list(cifra)
    checksum_lista = list(checksum)
    dicionario_frequencia = {}
    for e in range(0, len(cifra_lista)):
        if ord(cifra_lista[e]) == 45:
            dicionario_frequencia = dicionario_frequencia
        elif cifra_lista[e] not in dicionario_frequencia:
            dicionario_frequencia[cifra_lista[e]] = 1
        else:
            dicionario_frequencia[chr(ord(cifra_lista[e]))] += 1
    lista_frequencia = list(dicionario_frequencia.items())
    t = len(lista_frequencia)-1
    u = len(lista_frequencia)-1
    m = 1
    lista_chaves = []
    while t >= 0:
        for k in range(t):
            if lista_frequencia[k][1] < lista_frequencia[k+1][1]:
                lista_frequencia[k], lista_frequencia[k+1] = lista_frequencia[k+1], lista_frequencia[k]
        t -= 1
    while u >= 0:
        for e in range(u):
            if lista_frequencia[e][1] == lista_frequencia[e+1][1]:
                if ord(lista_frequencia[e][0]) > ord(lista_frequencia[e+1][0]):
                    lista_frequencia[e], lista_frequencia[e+1] = lista_frequencia[e+1], lista_frequencia[e]
        u -= 1
    while m <= len(checksum_lista)-2:
        if str(lista_frequencia[m-1][0]) == str(checksum_lista[m]):
            lista_chaves += [str(checksum_lista[m])]
            m += 1
        else:
            return False
    if lista_chaves[0:5] == checksum_lista[1:len(checksum_lista)-1]:
        return True
    return False

def filtrar_bdb(lista):
    """
    3.3-Filtrar a base de dados: lista --> lista. Esta função recebe uma lista com uma ou mais entradas da BDB e devolve
    uma lista com as entradas em que o sequência de controlo não está de acordo com a cifra, levantando erro se existir
    alguma informação incorreta.
    """
    if lista == [] or type(lista) != list:
        raise ValueError('filtrar_bdb: argumento invalido')
    for e in range(len(lista)):
        if type(lista[e]) != tuple or lista[e] == ():
            raise ValueError('filtrar_bdb: argumento invalido')
    lista_errados = []
    for i in range(0, len(lista)):
        if not eh_entrada(lista[i]):
            lista_errados += [lista[i]]
        else:
            lista_errados = lista_errados
    for j in range(0, len(lista)):
        lista_posicoes = list(lista[j])
        if not validar_cifra((lista_posicoes[0]), (lista_posicoes[1])):
            lista_errados += [lista[j]]
        else:
            lista_errados = lista_errados
    return lista_errados

# Parte4:Decifrar a BDB

def obter_num_seguranca(numeros):
    """
    4.2-Obter o número de segurança: tuplo --> inteiro. Esta função recebe um tuplo de inteiros e devolve a menor
    subtração feita entre essas numeros.
    """
    if type(numeros) != tuple or len(numeros) == 0 or len(numeros) == 1:
        return None
    numeros_lista = list(numeros)
    t = len(numeros_lista)
    lista_subtracoes =[]
    for e in range(t):
        for i in range(t):
            subtracao = numeros_lista[e]-numeros_lista[i]
            lista_subtracoes += [subtracao]
    lista_subtracoes.sort()
    for n in range(len(lista_subtracoes)):
        if lista_subtracoes[n] <= 0:
            lista_subtracoes = lista_subtracoes
        else:
            return lista_subtracoes[n]

def decifrar_texto(texto, num_seguranca):
    """
    4.3-Decifrar o texto: string, inteiro --> string. Esta função recebe uma cadeia de caracteres(a cifra) e o inteiro
    (numero de segurança que foi descoberto na função anterior) e devolve a cifra decifrada.
    """
    texto_lista = list(texto)
    for i in range(0, len(texto_lista)):
        if texto_lista[i] == '-':
            texto_lista[i] = chr(32)
        elif i % 2 == 1:
            num_seguranca_calculo = num_seguranca - 1
            while num_seguranca_calculo != 0:
                if texto_lista[i] == 'z':
                    texto_lista[i] = 'a'
                    num_seguranca_calculo -= 1
                else:
                    texto_lista[i] = chr(ord(texto_lista[i])+1)
                    num_seguranca_calculo -= 1
        else:
            num_seguranca_calculo = num_seguranca + 1
            while num_seguranca_calculo != 0:
                if texto_lista[i] == 'z':
                    texto_lista[i] = 'a'
                    num_seguranca_calculo -= 1
                else:
                    texto_lista[i] = chr(ord(texto_lista[i])+1)
                    num_seguranca_calculo -= 1
    texto_corrigido = ''.join(texto_lista)
    return texto_corrigido

def decifrar_bdb(lista):
    """
    4.4-Decifrar a bdb: lista --> lista. Esta função recebe uma lista com entradas da BDB e devolve uma lista com as
    cifras decifradas, levantando erro se houver alguma onformação incorreta.
    """
    lista_decifrada = []
    if not isinstance(lista, list):
        raise ValueError('decifrar_bdb: argumento invalido')
    for e in range(len(lista)):
        if not eh_entrada(lista[e]):
            raise ValueError('decifrar_bdb: argumento invalido')
        n = obter_num_seguranca(lista[e][2])
        d = decifrar_texto(lista[e][0], n)
        lista_decifrada += [d]
    return lista_decifrada

# Parte5:Filtar os utilizadores errados

def eh_utilizador(utilizador):
    """
    5.1-Verificar se é utilizador: universal --> booleano. Esta função recebe um argumento de qualquer tipo e devolve
    True se o argumento for um dicionário contendo a informção do utilizador.
    """
    if type(utilizador) != dict or len(utilizador) != 3:
        return False
    if ('name' or 'pass' or 'rule') not in utilizador.keys():
        return False
    if ('vals' or 'char') not in utilizador['rule'].keys():
        return False
    if type(utilizador['name']) != str or type(utilizador['pass']) != str:
        return False
    lista_name = list(utilizador['name'])
    lista_pass = list(utilizador['pass'])
    if len(lista_name) == 0 or len(lista_pass) == 0:
        return False
    if type(utilizador['rule']) != dict:
        return False
    if type(utilizador['rule']['vals']) != tuple or type(utilizador['rule']['char']) != str:
        return False
    if len(utilizador['rule']['vals']) != 2:
        return False
    if type(utilizador['rule']['vals'][0]) != int or type(utilizador['rule']['vals'][1]) != int:
        return False
    if utilizador['rule']['vals'][0] < 0 or utilizador['rule']['vals'][1] < 0:
        return False
    if utilizador['rule']['vals'][0] > utilizador['rule']['vals'][1]:
        return False
    if len(utilizador['rule']['char']) != 1:
        return False
    if ord(utilizador['rule']['char']) < 97 or ord(utilizador['rule']['char']) > 122:
        return False
    return True

def eh_senha_valida(passe,rule):
    """
    5.2-Verificar se a senha é válida: string, dicionario --> booleano. Esta função recebe uma cadeia de caracteres
    (passe) e um dicionario (contendo o a regra individual de criacão da senha) e devolve True apenas se seguir as
    regras conforme descritas.
    """
    lista_passe = list(passe)
    lista_vogais = []
    contador = 0
    numero_letra = 0
    for e in range(len(lista_passe)):
        if lista_passe[e] == 'a':
            lista_vogais += [lista_passe[e]]
        elif lista_passe[e] == 'e':
            lista_vogais += [lista_passe[e]]
        elif lista_passe[e] == 'i':
            lista_vogais += [lista_passe[e]]
        elif lista_passe[e] == 'o':
            lista_vogais += [lista_passe[e]]
        elif lista_passe[e] == 'u':
            lista_vogais += [lista_passe[e]]
    if len(lista_vogais) < 3:
        return False
    for i in range(0, len(lista_passe) - 1):
        if lista_passe[i] == lista_passe[i + 1]:
            contador += 1
    if contador < 1:
        return False
    for l in range(len(lista_passe)):
        if lista_passe[l] == rule['char']:
            numero_letra += 1
        else:
            numero_letra = numero_letra
    if rule['vals'][0] <= numero_letra <= rule['vals'][1]:
        return True
    return False

def filtrar_senhas(lista_de_senhas):
    """
    5.3-Filtrar as senhas: lista --> lista. Esta função recebe uma lista de senhas e devolve os nomes das senhas que
    estão inválidas, levantando erro se existir algum argumento incorreto.
    """
    lista_errados = []
    if type(lista_de_senhas) != list or len(lista_de_senhas) < 1:
        raise ValueError('filtrar_senhas: argumento invalido')
    for i in range(len(lista_de_senhas)):
        if not eh_utilizador(lista_de_senhas[i]):
            raise ValueError('filtrar_senhas: argumento invalido')
        if not eh_senha_valida(lista_de_senhas[i]['pass'],lista_de_senhas[i]['rule']):
            lista_errados += [lista_de_senhas[i]['name']]
    lista_errados.sort()
    return lista_errados

# Fim,peço desculpa se não der para compreender muito bem o código, mas pelo menos tentei :)
