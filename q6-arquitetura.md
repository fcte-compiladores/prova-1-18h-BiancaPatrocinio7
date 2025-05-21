De modo abstrato, o compilador é um programa que converte código de uma
linguagem para outra. Como se fosse uma função do tipo `compilador(str) -> str`.
No caso de compiladores que emitem código de máquina ou bytecode, seria mais
preciso dizer `compilador(str) -> bytes`, mas a idéia básica é a mesma.

De forma geral o processo é dividido em etapas como abaixo

```python
def compilador(x1: str) -> str | bytes:
    x2 = lex(x1)        # análise léxica
    x3 = parse(x2)      # análise sintática
    x4 = analysis(x3)   # análise semântica
    x5 = optimize(x4)   # otimização
    x6 = codegen(x5)    # geração de código
    return x6
```

Defina brevemente o que cada uma dessas etapas realizam e marque quais seriam os
tipos de entrada e saída de cada uma dessas funções. Explique de forma clara o
que eles representam. Você pode usar exemplos de linguagens e/ou compiladores
conhecidos para ilustrar sua resposta. Salve sua resposta nesse arquivo.

# lex(?) -> list[Token]
Análise léxica, essa etapa transforma o código-fonte em uma lista de tokens, que são unidades básicas da linguagem, como palavras-chave, identificadores, símbolos, números.
Exemplo de token: Token(tipo='if', valor='if')
Entrada: string com o código-fonte
Saída: lista de tokens
 
# parse(x2: list[Token]) -> AST
Análise sintática, nela os tokens são organizados em uma estrutura hierárquica chamada árvore sintática abstrata (AST - Abstract Syntax Tree), que representa a estrutura gramatical do programa.
Entrada: lista de tokens
Saída: uma AST (estrutura de nós representando comandos, expressões, etc.)

# analysis(x3: AST) -> AST
Análise semântica, essa etapa verifica se a AST está semanticamente correta, como se variáveis foram declaradas antes de serem usadas ou tipos são compatíveis. Pode anotar a AST com informações extras (como tipos).
Entrada: AST
Saída: AST enriquecida com informações semânticas ou com erros detectados

# optimize(x4: AST) -> AST
Otimização, nela o compilador tenta melhorar o desempenho ou reduzir o tamanho do código, mantendo o mesmo comportamento.
Podendo eliminar cálculos redundantes, simplificar expressões, etc.
Entrada: AST
Saída: AST otimizada

# codegen(x5: AST) -> str | bytes
Geração de código, nela transforma a AST final em código executável, pode ser código de máquina, bytecode, ou até mesmo outra linguagem.
Entrada: AST
Saída: código final (string ou bytes), pronto para ser executado