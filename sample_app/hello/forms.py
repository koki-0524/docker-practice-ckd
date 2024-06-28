from django import forms 
from django.contrib.auth import get_user_model
from .models import Book, Publisher, Author



class LoginForm(forms.Form): 
    #ログイン画面用のフォーム
    username = forms.CharField(
        label='ユーザー名',
        max_length=255,
    )
    
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(),
    )
    
    def clean_username(self):
        username = self.cleaned_data['username']
        
        if len(username) < 3:
            #NG
            raise forms.ValidationError(
                '入力されたユーザー名が正しくありません'
            )
            
        return username   
class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        
        #入力させるフィールドをタプル形式で宣言する
        fields = ('username','email','password')
        widget = {
            'password': forms.PasswordInput(attrs={'placeholder':'パスワード'})
        }
        
    #modelない入力項目を追加する場合
    password2 = forms.CharField (
        label='確認用パスワード',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'パスワード'})
    )
    
    #モデルで定義されている項目の設定を変更する場合
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs = {'placeholder':'ユーザー名'}
        self.fields["email"].widget.attrs = {'placeholder':'メールアドレス'}
        self.fields["email"].requtred = True
            
            
class BookForm(forms.ModelForm):
    class Meta:
        #使用するモデル
        model = Book
        #使用するフィールド項目
        fields = ('title','publisher','author','price','description','publish_date')
        #デフォルト設定の変更
        widgets = {
            'author': forms.CheckboxSelectMultiple(),
            'publish_date':forms.DateInput(attrs={"type":'date'})
        }
        
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            
            #各項目の初期化処理
            self.fields['title'].widget.attrs.update({'placeholder': '本のタイトル'})
            self.fields['place'].widget.attrs.update({'placeholder': '価格'})
            self.fields['description'].widget.attrs.update({'placeholder': '詳細'})
            
            #出版社と著者のデータをモデルから取得して設定する
            self.fields['publisher'].queryset = Publisher.objects.all()
            self.fields['author'].queryset = Author.all()
            
            