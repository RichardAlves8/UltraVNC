# UltraVNC — Segurança em redes privadas 

O UltraVNC é um software de acesso remoto que armazena a senha de conexão criptografada no arquivo `ultravnc.ini`. Essa criptografia, no entanto,  utiliza o algoritmo DES <i>(Data Encryption Standard)</i> operando no modo ECB <i>(Electronic Codebook)</i>. Qualquer senha armazenada pode ser recuperada caso o arquivo na pasta do programa seja aberto.

## Por que isso é perigoso?
O UltraVNC é OpenSource oque significa que qualquer pessoa pode ter acesso ao seu código fonte, e dito isso, é exposto o uso de uma chave estática em Hexdecimal, que é sempre a mesma em todas as instalações.
<p align="center"><code>E8 4A D6 60 C4 72 1A E0</code></p>

 
No script deste respositório está um exemplo do nível da fragilidade do arquivo em que sua senha fica armazenada.


## Recomendações 

- Evitar o uso do método de autenticação padrão.
- Utilizar um plugin de criptografia mais robusto.
- Restringir o acesso à porta.
- Proteger o arquivo `ultravnc.ini`.
- Monitorar logs de acesso.
