from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "webcam/",
        views.webcam_page,
        name="webcam"
    ),

    path(
        "mark/",
        views.mark_attendance,
        name="mark"
    ),

    path(
        "export/",
        views.export_csv,
        name="export"
    ),
]