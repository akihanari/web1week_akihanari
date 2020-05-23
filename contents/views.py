from django.shortcuts import render

# Create your views here.
from requests_oauthlib import OAuth1Session
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
import tweepy


def login_func(request):
    return render(request, "index.html")


def logout_func(request):
    return render(request, "logout.html")

@login_required
def top_page(request):

    social_account = UserSocialAuth.objects.get(user_id=request.user)
    # social_account_name = UserSocialAuth.objects.get(user_id=request.user.name)
    user_oauth_token = social_account.extra_data['access_token']['oauth_token']
    user_oauth_token_secret = social_account.extra_data['access_token']['oauth_token_secret']
    # screen_name = social_account['screen_name']

    # url = 'https://api.twitter.com/1.1/users/show.json' + '?user_id=' + request.user.id + '&include_entities=true'
    #
    # params = {}

    # url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

    # OAuth で GET
    # twitter = OAuth1Session(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, user_oauth_token, user_oauth_token_secret)
    #
    # req = twitter.get(url, params = params)
    #
    # if req.status_code == 200:
    #     # レスポンスはJSON形式なので parse する
    #     timeline = json.loads(req.text)
        # 各ツイートの本文を表示
        # for tweet in timeline:
        #     # print(tweet["text"])
        #     pass
    # else:
        # エラーの場合
        # print ("Error: %d" % req.status_code)


    # # OAuth認証
    # auth = tweepy.OAuthHandler(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET)
    # auth.set_access_token(user_oauth_token, user_oauth_token_secret)
    # api = tweepy.API(auth)
    #
    # # Timelineメソッド、stringで返却される
    # timeline = api.home_timeline
    # tw = OAuth1Session(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, user_oauth_token, user_oauth_token_secret)

    # url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    # params = {'count': 1}
    # req = UserSocialAuth.objects.get(url, count=request.user.id)
    #
    # if req.status_code == 200:
    #     timeline = json.loads(req.text)

    social_dic = {'social_account': social_account ,'user_oauth_token': user_oauth_token, 'user_oauth_token_sercret': user_oauth_token_sercret}

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
