# Brute-forcer de Login

Ferramenta em Python que testa senhas contra um formulário de login e detecta o acesso bem-sucedido pela resposta do servidor. Meu terceiro projeto de segurança (Red Team / ataque de senha).

Foi construído para atacar o **meu próprio honeypot**, fechando o ciclo Red Team × Blue Team: o honeypot finge um login, e este brute-forcer tenta quebrá-lo.

## O que faz
- Envia tentativas de login automaticamente (requisições HTTP POST)
- Percorre uma lista de senhas (**ataque de dicionário**)
- Detecta o acerto pelo **conteúdo** da resposta, não pelo status (o status é sempre 200)
- Para assim que encontra e informa em quantas tentativas

## Como usar
Com o honeypot rodando em `http://localhost:8000`:
```bash
pip install requests
python bruteforce.py
```

## Como funciona
- Usa a biblioteca `requests` para enviar um POST com usuário e senha, como se fosse o navegador clicando em "Entrar".
- Compara a resposta: a senha **errada** devolve a tela de login; a senha **certa** devolve uma página diferente (com "Bem-vindo"). O programa procura esse texto.
- Usa uma "bandeira" (`encontrou`) para saber, no fim, se alguma senha funcionou.

## O que eu aprendi
- A diferença entre **ataque de dicionário** (testar senhas prováveis) e **força bruta pura** (testar todas as combinações), e por que o dicionário é muito mais eficiente.
- Que o **status HTTP 200 não significa sucesso**: ele é devolvido tanto para senha certa quanto errada. O sucesso se detecta pelo conteúdo da resposta.
- A matemática do custo de um ataque: `combinações = (tamanho do alfabeto) ^ (comprimento)`. Cada caractere a mais multiplica o tempo.
- Por que as defesas funcionam: senha longa e aleatória, **rate limiting** (resposta lenta), bloqueio após X tentativas e **2FA**.

## Aviso ético e legal
Ferramenta de estudo. Use **apenas** contra sistemas seus ou com autorização explícita (aqui, o meu próprio honeypot). Ataque de força bruta contra sistemas de terceiros sem permissão é crime (no Brasil, Lei 12.737/2012).

---
Feito por **Caio Santhiago Reis da Conceição** — estudante de Ciência da Computação (PUC Minas)
