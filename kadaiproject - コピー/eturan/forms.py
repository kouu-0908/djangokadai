from django import forms 

class MailForm(forms.Form):
    name =forms.CharField(label ='お名前')
    email =forms.EmailField(label='メールアドレス')
    title =forms.CharField(label='お問い合わせタイトル')
    message =forms.CharField(label='メッセージ', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        '''ContactFormのコンストラクター
        
            フィールドの初期化を行う
        '''
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholer'] =\
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] ='form-control'
        
        self.fields['email'].widget.attrs['placeholer'] =\
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] ='form-control'
        
        self.fields['title'].widget.attrs['placeholer'] =\
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] ='form-control'
        
        self.fields['message'].widget.attrs['placeholer'] =\
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] ='form-control'