from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)
from models.page import Page
from models.category import Category
from utils import log

main = Blueprint('index', __name__)


@main.route("/")
def index():
    # form = {'title':'素颜韵脚'}
    # Category.new(form)
    ps = Page.all(page = 1)
    cs = Category.all()
    return render_template("index.html",pageData = ps,categorys = cs)


@main.route("/list", methods=['POST'])
def more():
    page = int(request.values['page'])
    size = int(request.values['size'])
    res = Page.all(page,size)
    return render_template("page-item.html", pageData=res)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    m = Page.new(form)
    return redirect(url_for('page.detail',id=m.id))


@main.route("/new")
def new():
    cs = Category.all()
    return render_template("new.html",cs = cs)


