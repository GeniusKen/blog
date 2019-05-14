from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)


from models.category import (
    Category,
)
from models.page import Page


main = Blueprint('category', __name__)


@main.route("/<string:category>")
def index(category):
    ps = Page.find_all(category = category)
    return render_template('category.html',pageData = ps,categorys = Category.all())