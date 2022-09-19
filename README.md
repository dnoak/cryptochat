# CryptoChat: Chat feito em Python com criptografia RSA e servidor socket.

#### Autores: Daniel  Carvalho e Augusto Alves

bibliotecas externas usadas:
PyCryptoDome: pip install pycryptodome
PyQt5: pip install PyQt5


Aplicação para realizar troca de mensagens entre dois Host (que estão em redes diferentes) de forma segura, através de uma comunicação Socket TCP. As mensagens trocadas entres os Hosts atendem os critérios de segurança apresentados: Integridade, confiabilidade, disponibilidade.

Em relação a parte de segurança da informação relacionada à integridade, confiabilidade e disponibilidade, foi usado o algoritmo de criptografia assimétrica RSA, junto com o conceito de tokens temporários que servem para garantir a privacidade da sessão entre dois usuários, junto a isso cada programa executado funciona como servidor e cliente simultaneamente, o que tira a necessidade de sempre haver um caminho fixo predeterminado entre cliente e servidor.

Foi criado um banco de dados descentralizado de usuário, que não depende de um servidor central para salvar o login de usuários. Para isso, foi utilizado o próprio conceito da definição de criptografia assimétrica, com cada usuário tendo a sua chave privada e pública únicas, então ele usa a sua própria chave pública como meio de identificação, e também só ele consegue provar a sua identidade baseada nessa chave pública aplicando sua chave privada quando é aplicado o algoritmo RSA. Logo, cada usuário pode logar e provar sua identidade de qualquer lugar da internet, basta apenas levar a sua chave privada e pública com ele. 
Esta aplicação tem uma interface gráfica feita em PyQt5 para configurar o IP e Porta do Host que receberá a mensagem, um campo para leitura e um campo para escrita de mensagens.


# USO DO CRYPTOCHAT#

1 - campo "Host": inserir o endereço de IP da máquina que deseja entrar em contato

2 - campo "Porta Client": inserir o valor da porta que escutará as mensagens vindas do outro usuário.

3 - campo "Porta Server": inserir o valor da porta que vai hospedar o seu servidor local, por padrão usa o endereço "localhost".

4 - campo "Usuário": inserir o nickname do usuário salvo localmente (a sua chave privada é salva localmente dentro de um arquivo ".pem" no formato "usuário.pem". Logo, a conta desse usuário pode ser acessada de qualquer computador, basta importar a pasta que contém a sua chave privada e salvá-la localmente no outro computador.)

5 - Botão "Criar usuário": cria um usuário novo com o nickname digitado no campo "Usuário" caso ele já não exista e seja um nickname válido, nesse momento é criado uma pasta com esse usuário e nela estará salva a sua chave privada no formato ".pem".

6 - Botão "Login": inicia o servidor/cliente simultaneamente e aguarda o CryptoChat do outro usuário em contato responder para iniciar a conversa.
