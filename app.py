from flask import Flask

from routes.page import main as page_routes
from routes.index import main as index_routes
from routes.category import main as category_routes

from flask import Markup
import markdown2

app = Flask(__name__)

app.secret_key = 'test for good'


app.register_blueprint(page_routes, url_prefix='/page')
app.register_blueprint(index_routes)
app.register_blueprint(category_routes,url_prefix='/category')

@app.template_filter('neomarkdown')
def neomarkdown(markdown_content):
    content=Markup(markdown2.markdown(markdown_content, extras=["tables"]))
    return content



if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)
