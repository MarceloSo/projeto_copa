from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sistema.views',
    url(r'^adicionar/$', 'selecaoAdicionar'),
  
    url(r'^salvar/$', 'selecaoSalvar'),
    
    url(r'^$', 'index'),


    #url(r'^admin/', include(admin.site.urls)),
)
