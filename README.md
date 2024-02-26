
# Cadastro automatizado de Usuários no SEI
## Considerações
- O script é sensível a latência de internet.
- O script utiliza os dados em arquivos CSV derivados de Excel, no formato: nome,email,sigla,cpf.
- Esses dados devem estar no diretório do projeto, com o nome `dados.csv`.
- Após rodar o comando que inicia o script, você terá 10 segundos para mudar para a janela do SIP.
- É importante a janela do SIP estar nesse [estado](https://imgur.com/a/8aAUqmG) e em tela cheia.
- Para parar o script, basta jogar o mouse em um dos cantos da tela (tem que ser bem no canto).
- É de suma importância seguir essas orientações para o funcionamento correto do script.
# Uso
Requisitos:
- Python3
	- abra a prompt de comando -> digite `python3` -> caso esteja instalado na máquina entrará no console do python, caso contrário abrirá a loja da Microsoft para instalação.
- [Git](https://git-scm.com/downloads)
	- Em caso de servidores proxy é necessário configurar o proxy para executar o git clone
	- `git config --global http.proxy http://user:password@proxyserver:port` 
- Pip
	- Na prompt de comando digite `pip --version` para checar se está instalado
	- Em caso de servidores proxy é necessário usar a flag `--proxy http://user:password@proxyserver:port` para instalação de pacotes com o Pip.
## Instruções

1. Crie uma pasta no local em que deseja armazenar o projeto e depois copie o caminho absoluto da pasta ([Imagem](https://imgur.com/a/l3pBhbd)).
2. Abra a prompt de comando e digite `cd <endereço que você copiou>`
3. Digite: `git clone https://github.com/bernardotonin/sei-cadastro-de-usuarios.git`
4. Digite: `cd sei-cadastro-de-usuarios`
5. Agora, vamos instalar as dependências do projeto, digite: `pip install -r requirements.txt`
6. Pronto, agora basta rodar o script com o comando `python3 main.py`

# Próximos passos
- Implementação do cadastro de unidades, permissões e hierarquias
- Implementação de uma interface gráfica