### Validador de CPF

Este é um código Python que implementa funções para validar os dígitos verificadores de um CPF.

#### Função `validar_primeiro_digito`

A função `validar_primeiro_digito(cpf)` valida o primeiro dígito verificador de um CPF. Ela recebe um CPF no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX' e retorna o primeiro dígito verificador se for válido, ou None caso ocorra algum erro.

#### Função `validar_segundo_digito`

A função `validar_segundo_digito(cpf)` valida o segundo dígito verificador de um CPF. Ela recebe um CPF no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX' e retorna o segundo dígito verificador se for válido, ou None caso ocorra algum erro.

#### Função `validar_cpf`

A função `validar_cpf(cpf)` valida um CPF verificando seus dígitos verificadores. Ela recebe um CPF no formato 'XXX.XXX.XXX-XX' ou 'XXXXXXXXXXX' e retorna True se o CPF for válido e False caso contrário.

### Exemplo de Uso

```python
cpf = '610.074.213-63'
if validar_cpf(cpf):
    print(f'O CPF {cpf} é válido!')
else:
    print(f'O CPF {cpf} é inválido!')
```

Esse exemplo demonstra como usar a função `validar_cpf` para verificar se um CPF é válido ou não.