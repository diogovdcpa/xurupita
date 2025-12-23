from flask import Blueprint, jsonify, request


api_bp = Blueprint("api", __name__)


@api_bp.get("/api")
def api_index():
    """Página inicial da API com informações dos endpoints"""
    return jsonify({
        "name": "Xurupita Labs API",
        "version": "1.0.0",
        "description": "API gratuita com informações sobre linguagens de programação",
        "documentation": "https://xurupita.com.br/docs",
        "endpoints": {
            "list_all": {
                "method": "GET",
                "url": "/api/languages",
                "description": "Lista todas as linguagens de programação"
            },
            "get_by_id": {
                "method": "GET",
                "url": "/api/languages/{id}",
                "description": "Retorna uma linguagem específica pelo ID (1-12)"
            },
            "search": {
                "method": "GET",
                "url": "/api/languages/search",
                "description": "Busca linguagens por nome (?q=) ou ano (?year=)"
            }
        },
        "total_languages": 12
    })


# Base de dados de linguagens de programação
LANGUAGES = [
    {
        "id": 1,
        "name": "Python",
        "description": "Linguagem de programação de alto nível, interpretada e de propósito geral. Conhecida por sua sintaxe clara e legibilidade.",
        "creator": "Guido van Rossum",
        "year": 1991,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "use_cases": [
            "Inteligência Artificial e Machine Learning",
            "Análise de Dados e Ciência de Dados",
            "Desenvolvimento Web (Django, Flask)",
            "Automação e Scripts",
            "DevOps e Infraestrutura"
        ]
    },
    {
        "id": 2,
        "name": "JavaScript",
        "description": "Linguagem de programação interpretada, multiparadigma e dinâmica. É a linguagem da web, executando em navegadores e servidores.",
        "creator": "Brendan Eich",
        "year": 1995,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
        "use_cases": [
            "Desenvolvimento Frontend (React, Vue, Angular)",
            "Desenvolvimento Backend (Node.js)",
            "Aplicativos Mobile (React Native)",
            "Desenvolvimento de Games",
            "Aplicações Desktop (Electron)"
        ]
    },
    {
        "id": 3,
        "name": "TypeScript",
        "description": "Superset tipado de JavaScript desenvolvido pela Microsoft. Adiciona tipagem estática opcional e recursos avançados de OOP.",
        "creator": "Anders Hejlsberg (Microsoft)",
        "year": 2012,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
        "use_cases": [
            "Aplicações Enterprise Frontend",
            "APIs Backend com Node.js",
            "Grandes projetos JavaScript",
            "Bibliotecas e Frameworks",
            "Full-stack Development"
        ]
    },
    {
        "id": 4,
        "name": "Java",
        "description": "Linguagem orientada a objetos, robusta e multiplataforma. Seu lema é 'Write Once, Run Anywhere'.",
        "creator": "James Gosling (Sun Microsystems)",
        "year": 1995,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg",
        "use_cases": [
            "Aplicações Android",
            "Sistemas Corporativos (Spring Boot)",
            "Microserviços",
            "Big Data (Hadoop, Spark)",
            "Sistemas Bancários e Financeiros"
        ]
    },
    {
        "id": 5,
        "name": "C#",
        "description": "Linguagem moderna, orientada a objetos, desenvolvida pela Microsoft como parte da plataforma .NET.",
        "creator": "Anders Hejlsberg (Microsoft)",
        "year": 2000,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg",
        "use_cases": [
            "Desenvolvimento de Games (Unity)",
            "Aplicações Windows Desktop",
            "APIs Web (.NET Core)",
            "Aplicações Enterprise",
            "Realidade Virtual e Aumentada"
        ]
    },
    {
        "id": 6,
        "name": "Go",
        "description": "Linguagem compilada, estaticamente tipada, criada pelo Google. Focada em simplicidade, eficiência e concorrência.",
        "creator": "Robert Griesemer, Rob Pike, Ken Thompson (Google)",
        "year": 2009,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg",
        "use_cases": [
            "Microserviços e APIs",
            "DevOps e Cloud (Docker, Kubernetes)",
            "Sistemas Distribuídos",
            "CLI Tools",
            "Infraestrutura de Rede"
        ]
    },
    {
        "id": 7,
        "name": "Rust",
        "description": "Linguagem de sistemas focada em segurança, velocidade e concorrência. Previne erros de memória em tempo de compilação.",
        "creator": "Graydon Hoare (Mozilla)",
        "year": 2010,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg",
        "use_cases": [
            "Sistemas Operacionais",
            "WebAssembly",
            "Blockchain e Criptomoedas",
            "Ferramentas de CLI",
            "Sistemas Embarcados"
        ]
    },
    {
        "id": 8,
        "name": "Swift",
        "description": "Linguagem moderna desenvolvida pela Apple para iOS, macOS e todo o ecossistema Apple. Segura e performática.",
        "creator": "Chris Lattner (Apple)",
        "year": 2014,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/swift/swift-original.svg",
        "use_cases": [
            "Aplicativos iOS",
            "Aplicativos macOS",
            "watchOS e tvOS",
            "Desenvolvimento Server-side",
            "Machine Learning (Core ML)"
        ]
    },
    {
        "id": 9,
        "name": "Kotlin",
        "description": "Linguagem moderna que roda na JVM, desenvolvida pela JetBrains. É a linguagem oficial para desenvolvimento Android.",
        "creator": "JetBrains",
        "year": 2011,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg",
        "use_cases": [
            "Desenvolvimento Android",
            "Backend com Spring Boot",
            "Kotlin Multiplatform",
            "Aplicações Desktop",
            "Scripts e Automação"
        ]
    },
    {
        "id": 10,
        "name": "PHP",
        "description": "Linguagem de script server-side amplamente usada para desenvolvimento web. Fácil de aprender e muito popular.",
        "creator": "Rasmus Lerdorf",
        "year": 1994,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg",
        "use_cases": [
            "Desenvolvimento Web (Laravel, Symfony)",
            "WordPress e CMS",
            "E-commerce (Magento, WooCommerce)",
            "APIs RESTful",
            "Sistemas de Gerenciamento de Conteúdo"
        ]
    },
    {
        "id": 11,
        "name": "Ruby",
        "description": "Linguagem dinâmica, orientada a objetos, focada em simplicidade e produtividade. Conhecida pelo framework Rails.",
        "creator": "Yukihiro Matsumoto",
        "year": 1995,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg",
        "use_cases": [
            "Desenvolvimento Web (Ruby on Rails)",
            "Startups e MVPs",
            "Automação e DevOps",
            "Prototipagem Rápida",
            "Scripts e Ferramentas"
        ]
    },
    {
        "id": 12,
        "name": "C++",
        "description": "Extensão da linguagem C com suporte a orientação a objetos. Altamente performática e usada em sistemas críticos.",
        "creator": "Bjarne Stroustrup",
        "year": 1983,
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg",
        "use_cases": [
            "Desenvolvimento de Games (Unreal Engine)",
            "Sistemas Operacionais",
            "Navegadores Web",
            "Sistemas Embarcados",
            "Computação de Alto Desempenho"
        ]
    }
]


@api_bp.get("/api/languages")
def get_all_languages():
    """Retorna todas as linguagens de programação"""
    return jsonify({
        "data": LANGUAGES,
        "total": len(LANGUAGES),
        "message": "Lista de linguagens de programação"
    })


@api_bp.get("/api/languages/<int:language_id>")
def get_language(language_id: int):
    """Retorna uma linguagem específica pelo ID"""
    language = next((lang for lang in LANGUAGES if lang["id"] == language_id), None)
    
    if language:
        return jsonify({
            "data": language,
            "message": "Linguagem encontrada"
        })
    
    return jsonify({
        "error": "Linguagem não encontrada",
        "message": f"Nenhuma linguagem com ID {language_id}"
    }), 404


@api_bp.get("/api/languages/search")
def search_languages():
    """Busca linguagens por nome ou ano"""
    query = request.args.get("q", "").lower()
    year = request.args.get("year", type=int)
    
    results = LANGUAGES
    
    if query:
        results = [lang for lang in results if query in lang["name"].lower()]
    
    if year:
        results = [lang for lang in results if lang["year"] == year]
    
    return jsonify({
        "data": results,
        "total": len(results),
        "query": query or None,
        "year": year
    })
