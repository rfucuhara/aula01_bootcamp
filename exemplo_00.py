nome_funcionario = input('Digite o seu nome:')
valor_salario = float(input("Digite o seu salario:"))
bonus_percentual = float(input("Digite o seu bonus em %:"))
salario_final = valor_salario
_CONSTATEBONUS = 1000

valor_do_bonus = _CONSTATEBONUS + valor_salario * bonus_percentual


print(f"Olá {nome_funcionario} possui o valor de bonus {valor_do_bonus}")