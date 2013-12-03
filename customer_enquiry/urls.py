from django.conf.urls import patterns

urlpatterns = patterns ('customer_enquiry.views',
    (r'^new/', 'new'),
)
