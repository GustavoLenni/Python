# Estrutura With

# Sem o with 
arquivo = open("meu_arquivo.txt" ,"w")
# Abrindo o arquivo
# o "w" é de write ou seja para escrever no arquivo
# ou "r" que seria read para ler o arquivo
arquivo.write("Hello World")
# escrevendo "Hello World no Arquivo"
arquivo.close()
# Fechando o Arquivo

# com o with
with open("meu_arquivo.txt", 'w') as arquivo:
    # O 'open("meu_arquivo.txt", 'w')' abre o arquivo no modo de escrita ('w' de write).
    # Se o arquivo não existir, ele será criado. Se já existir, o conteúdo será apagado.
    
    # O 'with' garante que o arquivo será fechado automaticamente ao final do bloco.
    
    arquivo.write("Olá Mundo")  # Escreve "Olá Mundo" no arquivo.
    
    # Após sair do bloco 'with', o arquivo será fechado automaticamente.

# Utilizando para ler o arquivo 
with open("meu_arquivo.txt", 'r') as arquivo:
    print(arquivo.read())