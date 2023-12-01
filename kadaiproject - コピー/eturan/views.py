from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import MailForm

from django.contrib import messages

from django.core.mail import EmailMessage

class IndexView(TemplateView):
    template_name ='index.html'

class DetailView(TemplateView):
    template_name ='detail.html'
    
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
