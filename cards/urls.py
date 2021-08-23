from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cards'

urlpatterns = [
    path('',views.homePage,name='homePage'),

    path('all',views.allCards,name='allCards'),

    # every language has his own url
    path('python',views.pythonList,name='pythonList'),
    path('django',views.djangoList,name='djangoList'),
    path('jscript',views.jscriptList,name='jscriptList'),
    path('html',views.htmlList,name='htmlList'),
    path('css',views.cssList,name='cssList'),
    
    path('addCode',views.addNewCode,name='addCode'),
    
    path('your-add',views.userCard,name='userCards'),
    path('<str:slug>',views.singelCard,name='cardDetail'),
    path('edit-card/<str:slug>',views.editCard,name='editCard'),
    path('search-result/',views.search,name='search'),
]

