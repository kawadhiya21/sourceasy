from django.conf.urls import patterns

urlpatterns = patterns ('product.views',
    (r'^add/', 'add'),
    (r'^add_sizes/(?P<product_id>\w{0,50})/$', 'add_sizes'),
    (r'^add_size_details/(?P<product_id>\w{0,50})/$', 'add_size_details'),
    (r'^add_fabric/(?P<product_id>\w{0,50})/$', 'add_fabric'),
    (r'^test/', 'test'),
)
