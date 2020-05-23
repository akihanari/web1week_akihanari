from django.shortcuts import render

# Create your views here.
from requests_oauthlib import OAuth1Session
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth



def login_func(request):
    return render(request, "index.html")


def logout_func(request):
    return render(request, "logout.html")

@login_required
def top_page(request):

    social_account = UserSocialAuth.objects.get(user_id=request.user.id)
    user_oauth_token = social_account.extra_data['access_token']['oauth_token']
    user_oauth_token_sercret = social_account.extra_data['access_token']['oauth_token_secret']
    # screen_name = social_account['screen_name']

    social_dic = {'social_account': social_account ,'user_oauth_token': user_oauth_token, 'user_oauth_token_sercret': user_oauth_token_sercret}

    url = 'https://api.twitter.com/1.1/users/show.json' + '?user_id=' + request.user.id + '&include_entities=true'

    oath_key_dict = {
        "consumer_key": SOCIAL_AUTH_TWITTER_KEY,
        "consumer_secret": SOCIAL_AUTH_TWITTER_SECRET,
        "access_token": user_oauth_token,
        "access_token_secret": "user_oauth_token_sercret
    }

    params = {}

    # OAuth で GET
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        timeline = json.loads(req.text)
        # 各ツイートの本文を表示
        for tweet in timeline:
            print(tweet["text"])

    else:
        # エラーの場合
        print ("Error: %d" % req.status_code)

    return render(request,'top.html', social_dic)

    # form = TweetForm


# UserId:{{ user.access_token.user_id }}</p>
# <p>OAuthTokenSecret:{{ user.access_token.oauth_token_secret }}</p>
# <p>OAuthToken:{{ user.access_token.oauth_token }}</p>
# <p>スクリーンネーム:{{ user.access_token.screen_name }}</p>
# <p>ツイートの合計数:{{ user.access_token.statuses_count }}</p>
# <p>ウェブサイト:{{ user.access_token.url }}</p>
# <p>フォロワー数:{{ user.access_token.followers_count }}</p>
# <p>最新ツイート:{{ user.access_token.status{text} }}</p>
