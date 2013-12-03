from django.conf.urls import patterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns ('product.views',
    (r'^add/', 'add'),
    (r'^add_sizes/(?P<product_id>\w{0,50})/$', 'add_sizes'),
    (r'^add_size_details/(?P<product_id>\w{0,50})/$', 'add_size_details'),
    (r'^add_fabric/(?P<product_id>\w{0,50})/$', 'add_fabric'),
    (r'^test/', 'test'),
    (r'^product_definition/(?P<product_id>\w{0,50})/$', 'api_product_definition'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
