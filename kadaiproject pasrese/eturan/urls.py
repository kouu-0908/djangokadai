from django.urls import path
from . import views

app_name ='eturan'

urlpatterns = [
     #topページのULR
    path('',views.IndexView.as_view(), name='index'),
    
    #記事ごとに表示させるページのURL
    path('kouryaku-detail/',
         views.DetailView.as_view(),
         name='kouryaku_detail'),
    
    #メールの送受信を行うページURL
    path('kouryaku-mail/',
         views.MailView.as_view(),
         name='kouryaku_mail'),
    
    #選択された記事の内容を表示させるページのURL
    path('detail/<int:pk>',
         views.jyouhou_detail,
         name='detail'),
    
    #選択されたカテゴリの記事を一覧表示させるページのURL
    path('jyouhou/<int:category>',
         views.CatetgoryView.as_view(),
         name='jyouhou_cat'),
    
    #選択されたユーザーの記事を一覧表示させるためのURL
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'),
    
    #ログイン中のユーザーの登録した記事を一覧表示するためのURL
    path('mypage/',views.MypageView.as_view(), name='mypage'),
    
    #検索を行うページのURL
    path('search/',
         views.SearchView.as_view(),
         name='kouryaku_search'),
    
]
