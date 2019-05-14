from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)


from models.page import (
    Page,

)


main = Blueprint('page', __name__)


@main.route('/<int:id>')
def detail(id):
    m = Page.get(id)
    return render_template("detail.html", page=m)