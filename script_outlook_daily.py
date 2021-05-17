#outlookの日報のテンプレを開く
#バッチファイルでこのプログラムを実行すると楽

import win32com.client as win                  #outlookやexcelの操作を可能にするモジュール #pip install pywin32でインストール

#outlookオブジェクト(COMオブジェクト)の設定
outlook = win.Dispatch('Outlook.Application') #これ以後、outlookオブジェクトでVBAコマンドを使うことでOutlookの操作が可能になる
mail = outlook.CreateItem(0)                  #outlookアイテムを作成 #引数が0だとメールのオブジェクトを作れる

#メールの内容
#sign =                                        #署名

mail.BodyFormat = 1                            #メールフォーマット: 1 テキスト, 2 HTML, 3 リッチテキスト
to_list = ['yuki.yoshida@fuji.co.jp']
mail.To =  ';'.join(to_list)
#mail.cc = 
# mail.Bcc = 
mail.Subject = ''                              #件名
mail.Body = '''


'''

# path = r'C:\\'                               #添付ファイルは絶対パスで指定
# mail.Attachments.Add(path)

#出来上がったメールを確認
mail.Display(True)