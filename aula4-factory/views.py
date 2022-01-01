"""Extensão Flask"""

def init_app(app):
    """Inicialização de extensões"""

    @app.route("/")
    def index():
        return "Hello Eduardo"

    @app.route("/contato")
    def contato():
        return "Página de contato"