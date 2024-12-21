# Air Quality Monitoring

Este é um sistema de monitoramento da qualidade do ar que utiliza React com TypeScript no Frontend e Python (FastAPI) no Backend. O sistema coleta e exibe dados simulados de qualidade do ar, gerando alertas quando os níveis de poluentes atingem limites críticos.

---

## Estrutura do Projeto

```
air_quality_monitoring/
|
├── backend/         # Backend desenvolvido em Python com FastAPI
│   ├── app/
│   │   ├── main.py         # Inicialização da aplicação FastAPI
│   │   ├── data_simulator.py  # Simulador de dados de qualidade do ar
│   │   └── models.py       # Modelos para dados da API
│   └── requirements.txt    # Dependências do Backend
│
├── frontend/        # Frontend desenvolvido com React e TypeScript
│   ├── src/
│   │   ├── App.tsx          # Componente principal da aplicação
│   │   ├── index.tsx        # Ponto de entrada do React
│   │   ├── components/      # Componentes reutilizáveis
│   │   └── styles/          # Estilos da aplicação
│   ├── package.json        # Dependências do Frontend
│   └── tsconfig.json       # Configuração do TypeScript
│
├── README.md        # Documentação do projeto
└── .gitignore       # Arquivos ignorados pelo Git
```

---

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
- [Node.js](https://nodejs.org/) (v16 ou superior)
- [Python](https://www.python.org/) (v3.10 ou superior)
- [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/)

---

## Configuração do Backend

1. Navegue até a pasta `backend`:

   ```bash
   cd backend
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor FastAPI:

   ```bash
   uvicorn app.main:app --reload
   ```

## Configuração do Frontend

1. Navegue até a pasta `frontend`:

   ```bash
   cd frontend
   ```

2. Instale as dependências:

   ```bash
   npm install
   ```

3. Inicie o servidor de desenvolvimento:

   ```bash
   npm start
   ```

4. Acesse a aplicação em: [http://localhost:3000](http://localhost:3000)

---

## Funcionalidades

- **Simulação de dados**: Os dados de qualidade do ar, como níveis de CO2 e PM2.5, são simulados no Backend.
- **Exibição de dados**: Visualize os dados em gráficos e tabelas no painel do Frontend.
- **Alertas**: Receba notificações quando os níveis de poluentes atingirem limites críticos.

---

## Tecnologias Utilizadas

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

### Frontend
- [React](https://reactjs.org/)
- [TypeScript](https://www.typescriptlang.org/)

---

## Melhorias Futuras

- Implementação de integração com sensores reais.
- Armazenamento de dados em um banco de dados.
- Visualizações adicionais para dados históricos.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---
