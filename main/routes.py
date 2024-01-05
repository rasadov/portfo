from main import app, db
import os
from flask import (
    send_from_directory,
    render_template,
    request,
    redirect,
    url_for,
)
from main.forms import (
    Message,
    ProjectForm,
    ArticleForm,
    LoginForm,
    RemoveArticleForm,
    RemoveProjectForm,
    CleanMessages
)
from main.models import Projects, Articles, Admin, Contact
from flask_login import login_user, current_user
from sqlalchemy import desc


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


def add_to_database(model):
    db.session.add(model)
    db.session.commit()


@app.route("/thank-you")
def thank_you():
    return render_template("thankyou.html")


@app.route("/", methods=["GET", "POST"])
def my_home():
    form = Message()
    blog = Articles.query.order_by(desc(Articles.id))
    projects = Projects.query.order_by(desc(Projects.id))
    if request.method == "GET":
        return render_template(
            "index.html",
            form=form,
            blog=blog,
            amount_of_articles=blog.count(),
            projects=projects,
            amount_of_projects=projects.count(),
        )

    if form.validate_on_submit():
        message = Contact(
            name=form.name.data,
            surname=form.surname.data,
            email=form.surname.data,
            message=form.message.data,
        )
        add_to_database(message)
        return redirect(url_for("thank_you"))
    return "<h1>Fill the form properly</h1>"


@app.route("/messages-admin", methods=["GET", "POST"])
def messages():
    messages = Contact.query.order_by(desc(Contact.id))
    form = CleanMessages()

    if request.method == 'POST':
        if form.validate_on_submit():
            for i in messages:
                db.session.delete(i)
            db.session.commit()

    return render_template("admin_messages.html", messages=messages, current_user=current_user, form=form)


@app.route("/create-blog", methods=["GET", "POST"])
def create_blog():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Articles(title=form.title.data, text=form.text.data)
        add_to_database(article)
        return redirect(url_for("admin"))
    return render_template("create_blog.html", form=form, current_user=current_user)


@app.route("/edit-project/<id>", methods=["GET", "POST"])
def edit_project(id):
    project = Projects.query.filter_by(id=id).first()
    form = ProjectForm(title=project.title, text=project.text, link=project.link)
    if form.validate_on_submit():
        project.title = form.title.data
        project.text = form.text.data
        project.link = form.link.data
        add_to_database(project)
        return redirect(url_for("admin"))
    return render_template("create_project.html", form=form, current_user=current_user)


@app.route("/edit-blog/<id>", methods=["GET", "POST"])
def edit_blog(id):
    article = Articles.query.filter_by(id=id).first()
    form = ArticleForm(title=article.title, text=article.text)
    if form.validate_on_submit():
        article.title = form.title.data
        article.text = form.text.data
        add_to_database(article)
        return redirect(url_for("admin"))
    return render_template("create_blog.html", form=form, current_user=current_user)


@app.route("/create-project", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Projects(
            title=form.title.data, text=form.text.data, link=form.link.data
        )
        add_to_database(project)
        return redirect(url_for("admin"))
    return render_template("create_project.html", form=form, current_user=current_user)


@app.route("/login", methods=["GET", "POST"])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Admin.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.chech_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            return redirect(url_for("admin"))
    return render_template("login.html", form=form, current_user=current_user)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    remove_project = RemoveProjectForm()
    remove_article = RemoveArticleForm()
    if request.method == "POST":
        if remove_article.validate_on_submit():
            article_to_delete = Articles.query.filter_by(
                id=remove_article.id.data
            ).first()
            if article_to_delete:
                db.session.delete(
                    Articles.query.filter_by(id=remove_article.id.data).first()
                )
                db.session.commit()

        if remove_project.validate_on_submit():
            project_to_delete = Projects.query.filter_by(
                id=remove_project.id.data
            ).first()
            if project_to_delete:
                db.session.delete(project_to_delete)
                db.session.commit()
    blog = Articles.query.order_by(desc(Articles.id))
    projects = Projects.query.order_by(desc(Projects.id))
    return render_template(
        "admin.html",
        blog=blog,
        amount_of_articles=blog.count(),
        projects=projects,
        amount_of_projects=projects.count(),
        remove_project=remove_project,
        remove_article=remove_article,
        current_user=current_user
    )
