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

Exemplo de sequência de instruções

```txt
move 0, 0
str 0, 1
move 1, 0
str 1, 1
move 0, 1
add 1, 1
jump 0, 1
str 2, 1
move 1, 1
str 0, 1
move 2, 1
str 1, 1
goto 4, 0
```

### Tradução de Instruções

O programa Python é responsável por traduzir um arquivo de texto contendo instruções acima instruções hexadecimais.

O arquivo de entrada deve seguir um formato específico, com cada instrução em uma linha separada.

Após a execução do programa Python, um arquivo de saída é gerado contendo as instruções traduzidas.

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Logisim](https://img.shields.io/badge/Logisim-004BA8?style=for-the-badge&logo=logisim&logoColor=white)](https://sourceforge.net/projects/circuit/)

## Instalação
<details>
<summary>Clique aqui!</summary>
<p>

### Pré-requisitos para instalação!

![Git](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)
--------------------------------------------------------------------------------------------

Para começar, clone o repositório do projeto em seu ambiente local. Siga a etapa abaixo:

* Abra o terminal na pasta onde deseja clonar o repositório.

* Clone o repositório para o seu ambiente local usando o seguinte comando:

```git
git clone https://github.com/JoaoLucasAssis/4_BITS_RISC_CPU.git
```

> :warning: obs: Certifique-se de ter o git instalado antes de executar o comando no terminal

* Execute o comando a seguir para buscar todas as branches do repositório remoto:

```git
git fetch --all
```

> :bulb: obs: Para listar todas as branches, execute o comando:
>
> git branch -a

* Crie uma branch local baseada na branch remota `develop` com o seguinte comando:

```git
git checkout develop
```

Agora você está pronto para começar a trabalhar em sua nova branch!
</p>
</details>

## Como usar o programa

Para traduzir um arquivo de instruções, siga estas etapas:

* Faça a [Instalação](#instalação) do projeto

* Adicione em `input.txt` a sequência de instruções que deseja traduzir.

* Após a execução do programa, abra o software Logisim.

* Carregue o projeto da CPU de 4 bits.

* Clique para adicionar o arquivo de instruções traduzido à memória de programa (ROM).

* Execute a simulação.

## Colaboradores

<table>
  <tr>
  <!-- João Lucas -->
    <td align="center">
      <a href="https://github.com/JoaoLucasAssis">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwxCRWlkfeigdbif83ap111RPNlGARl02wOF5OvW9zUA&s" width="100px;" height="100px;" alt="Foto do João Lucas"/><br>
        <sub>
          <b>JoaoLucasAssis</b>
        </sub>
      </a>
    </td>
    </td>
  </tr>
</table>