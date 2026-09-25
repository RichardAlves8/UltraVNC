## UltraVNC — Padrões de configurações e melhor uso

O UltraVNC é um software de acesso remoto, muito utilizado por ser open source e atender muito bem seus usuários. Achei interessante compartilhar como ele funciona em seu padrão de instalação, e como configurá-lo da melhor forma.

### O arquivo `ultravnc.ini`

Este armazena como suas configurações foram feitas, para que não seja preciso repeti-las toda vez, mas também sua chave de acesso. <br>
Para isso, é usado um dos algoritmos de criptografia disponíveis para salvá-la, mas, por padrão de instalação, é utilizado o DES <i>(Data Encryption Standard)</i> no modo ECB <i>(Electronic Codebook)</i>.<br>
Por via de regra, esse algoritmo atende bem à maioria dos casos, mas, quando falamos de open source, é oportuno salientar que em seu repositório há informações sobre como ele é utilizado.
<br>
### Sabemos que a chave:
 - É predefinida. 
 - Não utiliza um gerador aleatório.
 - Não tem prazo de vencimento.


### E Então podemos:

- Alterar o método de autenticação.
- Utilizar outros algoritmos de criptografia em suas configurações.

Neste repositório há um script que mostra um exemplo de uso, invertendo o processo com a chave mencionada. 
