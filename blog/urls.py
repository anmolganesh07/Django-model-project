from django.urls import path
from . import views
urlpatterns = [
    path("",views.starting_pageView.as_view(),name="starting-page"),
    path("posts/",views.postsView.as_view(),name="posts-page"),
    path("posts/<slug:slug>/",views.post_detailView.as_view(),name="post-detail-page")
]