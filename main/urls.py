# from django.urls import path
# from django.views.generic import TemplateView
# urlpatterns = [
#     path(
#         "about-us/",
#         TemplateView.as_view(template_name="about_us.html")),
#     path(
#         "",
#         TemplateView.as_view(template_name="home.html")),
#     path(
#         "",
#         TemplateView.as_view(template_name="base.html")),

# ]

from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path(
        "contact-form/",
        views.ContactUsView.as_view(),
        name="contact_form",
    ),
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name="about_us",
    ),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",
    ),
    # path(
    #     "contact-form/",
    #     TemplateView.as_view(template_name="contact_form.html"),
    #     name="contact_form",
    # ),
]