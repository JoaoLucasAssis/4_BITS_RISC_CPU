# CPU RISC de 4 bits e Tradutor de Instruções

Esta documentação descreve uma CPU de 4 bits implementada na arquitetura RISC (Reduced Instruction Set Computing).

O projeto inclui uma tabela de instruções e um programa Python para traduzir instruções baseadas nessa tabela em instruções hexadecimais para serem inseridas na memória do programa(ROM).

### Tabela de Instruções

A tabela de instruções define o conjunto de operações suportadas pela CPU de 4 bits e os códigos de operação associados a cada uma delas.

Ela é fundamental para escrever programas que serão executados pela CPU. 

Consulte a tabela de instruções para obter informações sobre como escrever programas compatíveis.

| hexa | abreviação | binário | registrador |
|:---:|:---:|:---:|:---:|
| 0 | mov | 000 0 | AC <= X |
| 1 | mov | 000 1 | AC <= M(X) |
| 2 | add | 001 0 | AC <= AC + X |
| 3 | add | 001 1 | AC <= AC + M(X) |
| 4 | sub | 010 0 | AC <= AC - X |
| 5 | sub | 010 1 | AC <= AC - M(X) |
| 6 | or | 011 0 | AC <= AC OR X |
| 7 | or | 011 1 | AC <= AC OR M(X) |
| 8 | not | 100 0 | AC <= NOT X |
| 9 | not | 100 1 | AC <= NOT M(X) |
| a | shf | 101 0 | AC <= AC << Q |
| b | shf | 101 1 | AC <= AC >> Q |
| c | jpz | 110 0 | PC <= X SE FLAG ZERO |
| d | jpo | 110 1 | PC <= X SE FLAG OVERFLOW |
| e | go | 111 0 | PC <= X |
| f | str | 111 1 | M(X) <= AC |