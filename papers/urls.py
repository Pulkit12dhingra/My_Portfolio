from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from papers.models import Post

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all()[:25],
                                    template_name="papers/blog.html")),

                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="papers/post.html")),
      
            ]