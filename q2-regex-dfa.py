"""
A figura q2.svg mostra uma máquina de estados (ou autômato finito
determinístico, DFA) que reconhece a linguagem formadas por 0's e 1's. Uma
string é aceita se começando no estado "start" e fazendo apenas as transições
definidas na figura, a string termina no estado "accept".

Dê alguns exemplos de strings que são aceitas e outras que são recusadas nessa
linguagem preenchendo as variáveis abaixo.

Depois crie uma expressão regular que reconheça a mesma linguagem.
"""

# Menor string possível nessa linguagem (0.5pt)
menor = "100"

# Uma string válida com exatamente 5 caracteres  (0.5pt)
string_5 = "11100"

# Menor string que o número de 0's é igual ao número de 1's (0.5pt)
menor_ab = "1010"

# 3 exemplos de strings válidas diferentes (exceto as anteriores) (1.0pt)
accept_3 = [
    "1100",
    "10100",
    "111100"
]


# Para cada exemplo acima, gere uma string inválida somente rearranjando os
# caracteres da string válida na mesma posição que em accept_3  (1.0pt)
reject_3 = [
    "01",        
    "0011",      
    "011110"     
]

# Regex que descreve a linguagem (1.5pt)
# Dica tente simplifiar o grafo tirando transições desnecessárias
regex = r"1(01*0)*1*0"