# PLN API
## Como executar a API?

1. Faça o clone deste repositório para o seu ambiente local.

2. Navegue até o diretório do projeto.

```bash
cd pln-api
```
3. Instale o Docker e o docker-compose.

Siga o tutorial do próprio Docker que está nesse [link](https://docs.docker.com/get-docker/).

4. Copie as variáveis de ambiente e coloque sua key da api do openai.

```bash
cp .env-example .env
```

5. Após instalar o Docker faça o build.

```bash
docker-compose up --build
```

## Endpoints da API

### Status
Endpoint: GET /status/

Esse endpoint retorna o status da api.

Exemplo de resposta:

```json
{
"status": "online",
"timestamp": 1690268056,
"started": 1690268052,
"service": "api",
"version": "1.0"
}
```
### Question
Endpoint: POST /answer/

Exemplo de body:
```json
{
	"question": "Exemplo de pergunta"
}
```

Exemplo de resposta de sucesso:
```json
{
	"answer": "Exemplo de resposta"
}
```

