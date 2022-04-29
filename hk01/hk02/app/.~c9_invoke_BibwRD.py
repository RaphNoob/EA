from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from .models import News, NewsCategory, WorldNews, Business, Travel, Sports
from . import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'
    

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/news1/')
    def news(self):
        param1 = 'news1'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
class a(BaseView):
    default_view = 'a'
    @expose('/')
    def a(self):
        return self.render_template('hknews.html')

db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, '全部', category="港聞")
appbuilder.add_link("社會新聞", href="/newspageview/global_news/", category="港聞")
appbuilder.add_link("突發", href="/newspageview/news1/", category="港聞")
appbuilder.add_view(a, "Big news") 

""" Custom Views """
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")