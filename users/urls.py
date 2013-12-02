from django.conf.urls import patterns

urlpatterns = patterns ('users.views',
    (r'^$', 'index'),
    (r'^login', 'login'),
    (r'^logged_in', 'logged_in'),
    (r'^logout', 'logout'),
    (r'^customer_demo', 'stub')
)
