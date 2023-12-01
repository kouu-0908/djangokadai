from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import MailForm

from django.contrib import messages

from django.core.mail import EmailMessage

from touroku.models import PhotoPost

from django.views.generic import DeleteView

#topページの表示に関係するview
class IndexView(ListView):
    template_name ='index.html'
    model =PhotoPost
    queryset =PhotoPost.objects.order_by('-post_at')
    paginate_by =5

  
#メールの送受信に関係するview
#teamsのファイルの中のやつ
class MailView(FormView):
    '''問い合わせページを表示するビュー
    
    フォームで入力されたデータを取得し、メールの作成と送信を行う
    '''
    # contact.htmlをレンダリングする
    template_name ='mail.html'
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = MailForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('eturan:kouryaku_mail')
      
    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
        メール送信を行う
        
        parameters:
          form(object): ContactFormのオブジェクト
        Return:
          HttpResponseRedirectのオブジェクト
          オブジェクトをインスタンスかするとsuccess_urlで
          設定されているURLにリダイレクトされる
        '''
        # フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        # メールのタイトルの書式を設定
        subject = 'お問い合わせ: {}'.format(title)
        # フォームの入力データの書式を設定
        message = \
          '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
          .format(name, email, title, message)
        # メールの送信元のアドレス(自分のメール)
        from_email = 'mcd2376047@stu.o-hara.ac.jp'
        # 送信先のメールアドレス(自分のメール)
        to_list = ['mcd2376047@stu.o-hara.ac.jp']
        # EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        # EmailMessageクラスのsend()でメールサーバーからメールを送信
        message.send()
        # 送信完了後に表示するメッセージ
        messages.success(
          self.request, 'お問い合わせは正常に送信されました！')
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

#記事の詳細を表示させるためのview
class DetailView(DeleteView):
  template_name ='detail.html'
  model =PhotoPost
  
def jyouhou_detail(request, pk):
  record =PhotoPost.objects.get(id=pk)
  return render(
    request, 'detail.html', {'object': record})

#カテゴリごとの記事を表示させるview
class CatetgoryView(ListView):
    template_name ='index.html'
    paginate_by =4
    
    def get_queryset(self):
        category_id =self.kwargs['category']
        categories =PhotoPost.objects.filter(
            category=category_id).order_by('-post_at')
        return categories

#ユーザーごとの記事を表示させるview
class UserView(ListView):
    template_name ='index.html'
    paginate_by =4
    
    def get_queryset(self):
        user_id =self.kwargs['user']
        user_list =PhotoPost.objects.filter(
            user=user_id).order_by('-post_at')
        return user_list
      
#ログイン中のユーザーのマイページを表示させるview
class MypageView(ListView):
  template_name ='mypage.html'
  paginate_by =4
  
  def get_queryset(self):
    queryset =PhotoPost.objects.filter(
      user=self.request.user).order_by('-post_at')
    return queryset

#参考サイト：https://acordecode.com/%e3%80%90django%e3%80%91%e3%82%a2%e3%83%97%e3%83%aa%e3%81%ab%e6%a4%9c%e7%b4%a2%e6%a9%9f%e8%83%bd%e3%82%92%e5%ae%9f%e8%a3%85%e3%81%99%e3%82%8b%e6%96%b9%e6%b3%95%ef%bc%81/
#検索を行うページを表示させるview
class SearchView(ListView):
    model = PhotoPost
    template_name = 'search.html'
    queryset =PhotoPost.objects.order_by('-post_at')
    paginate_by =4

    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__icontains=title)
        return query
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context
      
