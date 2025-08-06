# Manipulador de Listas em Python
![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Status](https://img.shields.io/badge/Status-Concluído-brightgreen) ![License](https://img.shields.io/badge/License-MIT-yellow)

Sistema interativo desenvolvido em Python para manipulação de listas de números inteiros, demonstrando conceitos fundamentais de Programação Orientada a Objetos e tratamento robusto de erros.

## Descrição do Projeto

Este projeto foi desenvolvido como exercício de Programação Orientada a Objetos em Python. O sistema oferece uma interface completa para manipulação de listas numéricas, permitindo adicionar elementos, remover elementos, calcular estatísticas e visualizar dados em tempo real.

### Problema Resolvido
- **Cenário**: Necessidade de manipular listas de números com interface amigável
- **Solução**: Sistema orientado a objetos com validações e interface interativa
- **Resultado**: Controle eficiente de dados numéricos com feedback visual

## Funcionalidades

### Gerenciamento de Lista
- **Adição de Elementos**: Permite adicionar números inteiros ao final da lista
- **Remoção de Elementos**: Remove a primeira ocorrência de um elemento específico
- **Validação Automática**: Impede operações inválidas com feedback claro

### Análise Estatística
- **Maior Valor**: Identifica e exibe o maior número da lista
- **Menor Valor**: Identifica e exibe o menor número da lista
- **Média Aritmética**: Calcula e exibe a média dos elementos com 3 casas decimais

### Interface e Controles
- **Menu Interativo**: 7 opções principais numeradas
- **Validação Robusta**: Trata entradas inválidas e não numéricas
- **Feedback Visual**: Títulos formatados e separadores visuais
- **Navegação Intuitiva**: Loop contínuo até escolha de saída

## Tecnologias Utilizadas

- **Python 3.6+**
- **Programação Orientada a Objetos**: Classes, métodos, encapsulamento
- **Estruturas de Controle**: while, if/elif/else
- **Tratamento de Exceções**: try/except ValueError
- **Métodos Built-in**: max(), min(), sum(), len()
- **Validação de Entrada**: Loops de verificação com lambda

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado no sistema

### Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/manipulador-listas.git
cd manipulador-listas
```

2. **Execute o programa:**
```bash
python manipulador_listas.py
```

3. **Siga as instruções:**
   - Navegue pelo menu principal
   - Realize operações de manipulação
   - Visualize resultados em tempo real

## Demonstração do Sistema

### Menu Principal
```
────────────────────────────────────────────────────────────────────────────────────────────────────
                                                 MENU
────────────────────────────────────────────────────────────────────────────────────────────────────

Opções:
     1. Adicionar um elemento no final da lista;
     2. Remover a primeira ocorrência do elemento na lista;
     3. Exibir o maior valor da lista;
     4. Exibir o menor valor da lista;
     5. Calcular média dos elementos da lista;
     6. Exibir lista;
     7. Sair.
────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Processo de Adição
```
────────────────────────────────────────────────────────────────────────────────────────────────────
                              ADICIONAR UM ELEMENTO NO FINAL DA LISTA
────────────────────────────────────────────────────────────────────────────────────────────────────

Insira o valor a ser adicionado à lista: 25
O valor foi adicionado com sucesso!
────────────────────────────────────────────────────────────────────────────────────────────────────

Deseja inserir novos números à lista?
     1. Sim
     2. Não
```

### Visualização de Estatísticas
```
────────────────────────────────────────────────────────────────────────────────────────────────────
                                    EXIBIR A MÉDIA DA LISTA
────────────────────────────────────────────────────────────────────────────────────────────────────

A média da lista é: 32.750
────────────────────────────────────────────────────────────────────────────────────────────────────
```

## Estrutura do Código

### Arquivo Principal
`manipulador_listas.py` - Implementação completa do sistema

### Classe Principal
```python
class ManipuladorDeLista:
    def __init__(self)                    # Construtor da classe
    def adicionar_elemento(elemento)      # Adiciona elemento à lista
    def remover_elemento(elemento)        # Remove elemento da lista
    def encontrar_maior()                 # Retorna maior valor
    def encontrar_menor()                 # Retorna menor valor
    def calcular_media()                  # Calcula média aritmética
    def mostrar_lista()                   # Retorna cópia da lista
```

### Funções Auxiliares
```python
def configura_titulo(titulo)             # Formatação de títulos
def delimitador_visual()                 # Separadores visuais
def ler_numero(pergunta, condicao...)    # Validação de entrada
def menu()                               # Interface principal
def main()                               # Programa principal
```

### Fluxo de Funcionamento

```
Início → Menu Principal → Escolha da Opção → Validação → Execução → Resultado → Loop
```

## Casos de Teste

| Cenário | Entrada | Resultado Esperado |
|---------|---------|-------------------|
| Lista Vazia | Opção 3 (Maior) | "A lista está vazia!" |
| Adicionar Número | 42 | "O valor foi adicionado com sucesso!" |
| Remover Existente | 42 | "O valor foi removido com sucesso!" |
| Remover Inexistente | 99 | "O valor inserido não está na lista" |
| Calcular Média | [10,20,30] | "A média da lista é: 20.000" |

## Validações Implementadas

- **Entrada Numérica**: Aceita apenas números inteiros
- **Opções de Menu**: Valida escolhas de 1 a 7
- **Existência de Elementos**: Verifica se elemento existe antes de remover
- **Lista Vazia**: Impede operações estatísticas em listas vazias
- **Continuação**: Valida opções de repetição (1 ou 2)

## Conceitos Demonstrados

### Programação Orientada a Objetos
- **Encapsulamento**: Dados e comportamentos organizados em classe
- **Métodos de Instância**: Operações que modificam estado do objeto
- **Construtor**: Inicialização controlada de objetos

### Validação e Controle de Fluxo
- **Loops de Validação**: Repetição até entrada válida
- **Estruturas Condicionais**: Tomada de decisões baseada em entrada
- **Tratamento de Exceções**: Captura de erros de entrada

### Interface de Usuario
- **Menu Interativo**: Navegação numerada intuitiva
- **Feedback Visual**: Confirmações e mensagens informativas
- **Formatação Consistente**: Títulos e separadores padronizados

## Aprendizados Aplicados

Este projeto consolidou conhecimentos em:

- **Classes e Objetos**: Modelagem de estruturas de dados
- **Métodos e Atributos**: Encapsulamento de funcionalidades
- **Validação de Entrada**: Técnicas para entrada robusta de dados
- **Estruturas de Controle**: Loops e condicionais para fluxo de programa
- **Interface de Terminal**: Criação de menus interativos funcionais
- **Tratamento de Erros**: Prevenção de crashes por entrada inválida

## Melhorias Futuras

- [ ] Persistência de dados em arquivo
- [ ] Importação/exportação de listas
- [ ] Operações matemáticas avançadas (mediana, moda)
- [ ] Interface gráfica com Tkinter
- [ ] Suporte a números decimais
- [ ] Histórico de operações
- [ ] Múltiplas listas simultâneas
- [ ] Ordenação personalizada

## Estrutura de Arquivos

```
manipulador-listas/
│
├── manipulador_listas.py    # Código principal
├── README.md               # Documentação
└── LICENSE                 # Licença MIT
```

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

**Natan Mauricio Santos**
- Email: natanmauriciosantos@hotmail.com
- LinkedIn: [linkedin.com/in/natan-mauricio-santos](https://linkedin.com/in/natan-mauricio-santos)
- GitHub: [github.com/NatanMauricio1995](https://github.com/NatanMauricio1995)

---
*Desenvolvido como exercício de Programação Orientada a Objetos em Python*
