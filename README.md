# Teste-estagio-back: Ominisaude

# Como funciona:

  ###  Ao rodar o programa abrirá a interface gráfica onde você tera algumas opções:
  - Pesquisar um filme.
  - Listar um filme.
    
    
  #### Pesquisar:
  - Abrirá uma janela com as informações básicas do filme que foram buscadas na API OMDB, além de uma nova opção: Favoritar/Remover Favorito.
  - ##### Favoritar/ Remover Favorito:
    - Favoritar um filme adicionará este na sua lista de favoritos que está sendo salva em um arquivo JSON
    - Remover um filme removerá este da sua lista de favoritos.
  
  #### Listar:
  - Abrirá uma janela com uma lista dos títulos de filmes favoritados que estão salvos no arquivo JSON.


  #### Observações:
  - Apesar de ser simples o programa não permitirá que você adicione o mesmo filme mais de uma vez na lista de favoritos.
  - Assim como não permitirá remover um filme que não esteja na lista.

# Documentação:

#### Bibliotecas usadas:
- request.
- json.
- tkinter.

#### Classes criadas:
- Movie.
  
### Explicação do código:
- Usando a biblioteca request e com o método get tive acesso a API OMDB e pude pegar os dados dos filmes e atribuí-los a classe criada Movie.
- Usando a biblioteca tkinter criei uma interface gráfica para facilitar o uso do programa.
- Usando a biblioteca json pude transformar a resposta da API em um dict além de poder escrever e ler o arquivo que guarda a lista de filmes favoritos.
 
### Verificações:

##### Para salvar como favorito:
  - Caso a lista possua conteúdo, verifica se o filme já está nela, se não estiver salva.
    
##### Para remover da lista de favoritos:
- Verifica se o filme está na lista, se estiver remove.

##### Para pesquisar filme:
- Verifica se a caixa de pesquisa possui algum texto nela, se não impede a busca.