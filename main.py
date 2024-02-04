def validar_primeiro_digito(cpf):
    """
    Valida o primeiro dígito verificador de um CPF.

    Args:
    - cpf (str): O CPF a ser validado, no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX'.

    Returns:
    - int: O primeiro dígito verificador do CPF, caso seja válido, ou None caso ocorra algum erro.
    """

    # Lista de multiplicadores para o cálculo do primeiro dígito verificador
    multiplicadores_primeiro_digito = list(range(10, 1, -1))

    try:
        # Convertendo o CPF para uma lista de caracteres
        cpf_lista = list(cpf)

        # Removendo os caracteres '.' e '-' do CPF
        for indice, caractere in enumerate(cpf_lista):
            if caractere == '.' or caractere == '-':
                del cpf_lista[indice]

        # Unindo os caracteres do CPF para formar uma string
        cpf_unificado = ''.join(cpf_lista)

        # Verificando se o CPF é sequencial
        cpf_sequencial = cpf_unificado == cpf_unificado[0] * len(cpf_unificado)
        if cpf_sequencial:
            print('Dados sequenciais, por favor insira um CPF válido')
            return None

        # Verificando se o CPF informado tem 11 dígitos
        if cpf_unificado.isdigit() and len(cpf_unificado) == 11:

            # Obtendo apenas os primeiros nove dígitos do CPF
            nove_primeiros_digitos = cpf_unificado[:9]

            # Variável para armazenar a soma total da multiplicação
            soma_total = 0

            # Calculando a soma ponderada dos nove primeiros dígitos do CPF
            for valor, multiplicador in zip(nove_primeiros_digitos, multiplicadores_primeiro_digito):
                resultado = int(valor) * multiplicador
                soma_total += resultado

            # Calculando o primeiro dígito verificador
            resultado_primeiro_digito = (soma_total * 10) % 11

            # Verificando se o primeiro dígito é maior que 9
            digito_1 = resultado_primeiro_digito if resultado_primeiro_digito <= 9 else 0

            return digito_1

        else:
            print('Por favor, insira um CPF válido. Exemplo: xxx.xxx.xxx-xx')
            return None

    except Exception as e:
        print(f'Erro ao validar o primeiro dígito do CPF: {e}')
        return None


def validar_segundo_digito(cpf):
    """
    Valida o segundo dígito verificador de um CPF.

    Args:
    - cpf (str): O CPF a ser validado, no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX'.

    Returns:
    - int: O segundo dígito verificador do CPF, caso seja válido, ou None caso ocorra algum erro.
    """

    # Lista de multiplicadores para o cálculo do segundo dígito verificador
    multiplicadores_segundo_digito = list(range(11, 1, -1))

    try:
        # Convertendo o CPF para uma lista de caracteres
        cpf_lista = list(cpf)

        # Removendo os caracteres '.' e '-' do CPF
        for indice, caractere in enumerate(cpf_lista):
            if caractere == '.' or caractere == '-':
                del cpf_lista[indice]

        # Unindo os caracteres do CPF para formar uma string
        cpf_unificado = ''.join(cpf_lista)

        # Verificando se o CPF é sequencial
        cpf_sequencial = cpf_unificado == cpf_unificado[0] * len(cpf_unificado)
        if cpf_sequencial:
            print('Dados sequenciais, por favor insira um CPF válido')
            return None

        # Verificando se o CPF informado tem 11 dígitos
        if cpf_unificado.isdigit() and len(cpf_unificado) == 11:

            # Obtendo apenas os primeiros nove dígitos do CPF
            nove_primeiros_digitos = cpf_unificado[:9]

            # Adicionando o primeiro dígito verificador aos nove primeiros dígitos do CPF
            dez_digitos = nove_primeiros_digitos + str(validar_primeiro_digito(cpf_unificado))

            # Variável para armazenar a soma total da multiplicação
            soma_total = 0

            # Calculando a soma ponderada dos dez dígitos do CPF
            for valor, multiplicador in zip(dez_digitos, multiplicadores_segundo_digito):
                resultado = int(valor) * multiplicador
                soma_total += resultado

            # Calculando o segundo dígito verificador
            resultado_segundo_digito = (soma_total * 10) % 11

            # Verificando se o segundo dígito é maior que 9
            digito_2 = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0

            return digito_2

    except Exception as e:
        print(f'Erro ao validar o segundo dígito do CPF: {e}')
        return None


def validar_cpf(cpf):
    """
    Valida um CPF verificando seus dígitos verificadores.

    Args:
    - cpf (str): O CPF a ser validado, no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX'.

    Returns:
    - bool: True se o CPF for válido, False caso contrário.
    """

    # Validando o primeiro dígito do CPF
    primeiro_digito = validar_primeiro_digito(cpf)

    if primeiro_digito is None:
        return False

    # Validando o segundo dígito do CPF
    segundo_digito = validar_segundo_digito(cpf)

    if segundo_digito is None:
        return False

    # Verificando se os dígitos validados correspondem aos dígitos do CPF informado
    cpf_valido = cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)

    return cpf_valido


# Exemplo de uso
cpf = '000.000.000-00'
if validar_cpf(cpf):
    print(f'O CPF {cpf} é válido!')
else:
    print(f'O CPF {cpf} é inválido!')
