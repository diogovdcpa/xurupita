<div align="center">

# 🧪 Xurupita Labs

**Laboratório digital de experimentação e inovação em desenvolvimento web**

[![Deploy with Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)](https://xurupita.com.br)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

[🌐 Website](https://xurupita.com.br) • [📚 API Docs](https://xurupita.com.br/docs) • [🔗 API](https://xurupita.com.br/api)

</div>

---

## 🚀 Sobre o Projeto

**Xurupita Labs** é um laboratório digital pessoal dedicado a explorar novas tecnologias e criar experiências web inovadoras. Aqui experimentamos, aprendemos e compartilhamos conhecimento.

### ✨ Features

- 🎨 **Landing Page Moderna** - Design dark mode com paleta azul
- 📡 **API REST Gratuita** - Dados sobre linguagens de programacao
- 📖 **Documentacao Completa** - Exemplos em JavaScript e Python
- ⚡ **Deploy na Vercel** - Serverless Functions com Flask

---

## 📡 API de Linguagens de Programacao

Uma API REST gratuita e aberta com informacoes sobre 12 linguagens de programacao. Perfeita para aprender a consumir APIs!

### Endpoints

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| `GET` | `/api` | Informacoes da API |
| `GET` | `/api/languages` | Lista todas as linguagens |
| `GET` | `/api/languages/{id}` | Busca por ID (1-12) |
| `GET` | `/api/languages/search?q=python` | Busca por nome |

### Exemplo de Uso

```javascript
// JavaScript
fetch('https://xurupita.com.br/api/languages')
  .then(res => res.json())
  .then(data => console.log(data));
```

```python
# Python
import requests
response = requests.get('https://xurupita.com.br/api/languages')
data = response.json()
```

### Linguagens Disponiveis

Python, JavaScript, TypeScript, Java, C#, Go, Rust, Swift, Kotlin, PHP, Ruby, C++

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3 (Dark Mode)
- **Deploy**: Vercel Serverless Functions
- **Fonte**: Inter (Google Fonts)

---

## 🏃 Rodando Localmente

```bash
# Clone o repositorio
git clone https://github.com/diogovdcpa/xurupita.git
cd xurupita

# Instale as dependencias
python -m venv .venv
source .venv/bin/activate
pip install flask gunicorn

# Rode o servidor
gunicorn main:app
```

Acesse `http://localhost:8000`

---

## 📁 Estrutura do Projeto

```
xurupita/
├── main.py              # App Flask principal
├── endpoints/
│   └── routes.py        # Rotas da API
├── templates/
│   ├── index.html       # Landing page
│   └── docs.html        # Documentacao da API
├── static/
│   └── css/
│       └── style.css    # Estilos (dark mode)
└── public/
    └── favicon.png      # Favicon
```

---

## 📄 Licenca

Este projeto e open source e disponivel sob a licenca MIT.

---

<div align="center">

**Feito com 💙 por [Xurupita Labs](https://xurupita.com.br)**

*Experimentando o futuro, uma aplicacao por vez.*

</div>
