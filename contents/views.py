from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


def login_func(request):
    return render(request, "index.html")


def logout_func(request):
    return render(request, "logout.html")

# def index_func(request):
#     return render(request, "contents/top.html")


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    
    return render(request,'top.html',{'user': user})

    # form = TweetForm

# user_oauth_token = social_account.extra_data['access_token']['oauth_token']
# user_oauth_token_sercret = social_account.extra_data['access_token']['oauth_token_secret']
# UserId:{{ user.access_token.user_id }}</p>
# <p>OAuthTokenSecret:{{ user.access_token.oauth_token_secret }}</p>
# <p>OAuthToken:{{ user.access_token.oauth_token }}</p>
# <p>スクリーンネーム:{{ user.access_token.screen_name }}</p>
# <p>ツイートの合計数:{{ user.access_token.statuses_count }}</p>
# <p>ウェブサイト:{{ user.access_token.url }}</p>
# <p>フォロワー数:{{ user.access_token.followers_count }}</p>
# <p>最新ツイート:{{ user.access_token.status{text} }}</p>
