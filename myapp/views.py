from django.shortcuts import render,redirect
from .models import Tweets
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def homepage(request):

    tweet_data = Tweets.objects.all().order_by("-pub_date")
    context = {"view_tweets":tweet_data,"page":"home","username":request.user.username}
    
    return render(request,"index.html",context=context)

def add_tweet(request):

    if request.method == "POST":
        topic = request.POST.get("topic")
        tweet = request.POST.get("tweet_content")
        pub_date = timezone.now()

        Tweets.objects.create(
            topic = topic,
            tweet = tweet,
            pub_date = pub_date
        )

        messages.success(request,"Tweet Added Successfully...")

        return redirect("/add-tweet/")

    return render(request,"add_tweet.html",{"page":"addtweet"})

def delete_tweet(request,tweet_id):
    
    tweet = Tweets.objects.get(id=tweet_id)
    tweet.delete()

    return redirect("/")

def update_tweet(request,tweet_id):

    queryset = Tweets.objects.get(id=tweet_id)
    
    if request.method == "POST":

        data = request.POST

        utopic = data.get("topic")
        utweet = data.get("tweet_content")
        upub_date = timezone.now()

        queryset.topic = utopic
        queryset.tweet = utweet
        queryset.pub_date = upub_date

        queryset.save()

        return redirect('/')
    context = {'retrotweets':queryset,"page":"updatetweet"}

    return render(request,"update_tweet.html",context=context)
def logout_page(request):
    logout(request)
    return redirect("/login/")
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("a_user_name")
        password = request.POST.get("a_user_password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username!")
            return redirect("/login/")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password!")
            return redirect("/login/")
        else:

            login(request,user)

            return redirect("/")

    return render(request,"login.html",{"page":"login"})

def register_page(request):

    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"UserName Already Exists...")
            return redirect("/register/")

        new_user = User.objects.create(
            username = username
        )

        new_user.set_password(password)
        new_user.save()
        messages.info(request,"Registration Successful...")
        return redirect("/register/")

    return render(request,"register.html")

