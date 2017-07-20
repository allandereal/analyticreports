from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^home/$', dashboard, name='dashboard'),
    url(r'^project/$', project_groups_detail, name='project-groups'),
    url(r'^report/verison/one/(?P<project_id>[\-\w]+)/$', report_template_one, name='template_one'),
    url(r'^report/csv/(?P<project_id>[\-\w]+)/$', export_to_csv, name='csv')

    # url(r'^$', qc_views.index),
    # url(r'^test_pdf_found/$', qc_views.html_to_pdf_view),
    # url(r'^sms_maama_weekly/$', qc_views.sms_maama_weekly),
    # url(r'^sms_maama_weekly_pdf/$', qc_views.print_report),
    # url(r'^sms_maama_weekly_pdf_2/$', qc_views.generate_pdf),
    # url(r'^sms_maama_weekly_pdf_3/$', qc_views.pdf_view),
    # url(r'^failed_messages/$', qc_views.daily_messages_failed),
    # url(r'^pdf/$', qc_views.MyPDFView.as_view()),
    # url(r'^test_pdf/$', qc_views.TestMyPDFView.as_view()),
    # url(r'^my-pdf/$', PDFView.as_view(template_name='my-pdf.html'), name='my-pdf'),
]
