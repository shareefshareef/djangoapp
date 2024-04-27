from django.urls import path
from .views import homepage,add_tweet,delete_tweet,update_tweet
from .views import login_page,register_page,logout_page


app_name = "myapp"

urlpatterns = [
    path("",homepage,name="home"),
    path("add-tweet/",add_tweet,name="add_tweet"),
    path("delete-tweet/<tweet_id>/",delete_tweet,name="delete_tweet"),
    path("update-tweet/<tweet_id>/",update_tweet,name="update_tweet"),
    path("login/",login_page,name="login_page"),
    path("register/",register_page,name="register_page"),
    path("logout/",logout_page,name="logout_page")
]