from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from owl_survey import settings

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'owl.views.home'),
                       url(r'^/$', 'owl.views.home'),
                       url(r'^accounts/signup/$', 'owl.views.signup'),
                       url(r'^registered_facebook/$', 'owl.views.registered_facebook'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'}),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': '/'}),

                       url(r'^edit/profile/$', 'owl.views.edit_profile'),
                       url(r'^edit/question/(?P<qid>[0-9]+)/$', 'owl.views.edit_question'),
                       url(r'^edit/survey/(?P<sid>[0-9]+)/$', 'owl.views.edit_survey'),

                       url(r'^new/question/(?P<sid>[0-9]+)/$', 'owl.views.new_question'),
                       url(r'^new/survey/$', 'owl.views.new_survey'),

                       url(r'^view/questions/(?P<sid>[0-9]+)/$', 'owl.views.view_question'),
                       url(r'^view/surveys/$', 'owl.views.view_survey'),
                       url(r'^view/my_surveys/$', 'owl.views.view_my_survey'),
                       url(r'^view/for_me_surveys/$', 'owl.views.view_survey_for_audience'),
                       url(r'^view/survey/(?P<sid>[0-9]+)/$', 'owl.views.view_survey_by_id'),


                       url(r'^delete/survey/(?P<sid>[0-9]+)/$', 'owl.views.delete_survey'),
                       url(r'^result/(?P<sid>[0-9]+)/$', 'owl.views.result'),
                       ) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

