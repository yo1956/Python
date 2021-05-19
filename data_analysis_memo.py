import pandas as pd
import numpy as np

#---------------------------------------------データ分析で使う関数のメモ-----------------------------------------------------------#
#pandasやnumpyなどの使い方を例とともに説明する

#**************************データの読み込み********************************#

#pd.read_csv()------------------------------------------------
#csvファイルのデータセットをpandas.DataFrame形式で読み込む。
train = pd.read_csv('../input/titanic/train.csv')
test = pd.read_csv('../input/titanic/test.csv')

#pandas.DataFrame.head()--------------------------------------
#pandas.DataFrameの上から数行の中身を返す
#表示する行数は引数で指定でき、特に指定しない場合は5行になる。
train.head()

#pd.concat()----------------------------------------------------
#pandas.DataFrameを行方向に結合し、新しいpandas.DataFrameを作る
#第1引数に結合したいpandas.DataFrameのリストを渡す
#sort = Falseとすることで、列をソートしないように指定できる
data = pd.concat([train, test], sort=False)

#pandas.DataFrame.isnull()------------------------------------------------
#pandas.DataFrameの全ての要素について、欠損値かどうかの真偽値の表を表示する
#pandas.DataFrame.sum()
#列方向に足し合わせて、数を表示する
data.isnull().sum() #列ごとの欠損値の数が分かる


#**************************特徴量エンジニアリング****************************#

#pandas.Series.replace()------------------------------------------
#値を置換する
#param1: 変換前のリスト
#param2: 変換後のリスト 
#param3: 変換前のリストを変換後のもので置き換えるならTrueを指定
#pandas.Seriesは、pandas.DataFrame内の1つの列を指すデータ型のこと
data['Sex'].replace(['male', 'female'], [0, 1], inplace=True)

#pandas.Series.fillna()-----------------------------------------------------------
#欠損値を補完する
#param1: 欠損値を補完する値
#param2: inplace指定
data['Embarked'].fillna('S', inplace=True)
data['Fare'].fillna(np.mean(data['Fare']), inplace=True) #Fareの平均で欠損値を補完

i#Ageの平均値－標準偏差から平均値＋標準偏差の間の整数値を取る乱数で補完する例
age_avg = data['Age'].mean()
age_std = data['Age'].std()
data['Age'].fillna(np.random.randint(age_avg - age_std, age_avg + age_std), inplace=True)

#pandas.Series.map()----------------------------------------------------------------------------------------------
#値を置換する
#pandas.Series.replace()との違いは、元のデータに変換を支持していない値が存在した場合、np.nan(欠損値)に置き換わること
#pandas.Series.replace()は、指定がない値についてはそのまま保持する
#astype()はdtype(pandas.DataFrameの列ごとのデータ型)に対しキャストができる
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)

#pandas.DataFrame.drop()----------------------------------
#行・列の削除
#param1: 削除する行・列のリスト
#param2: axis=1とすると列の削除、axis=0とすると行の削除
#param3: inplace指定
delete_columns = ['Name', 'PassengerID', 'SibSP', 'Parch', 'Ticket', 'Cabin']
data.drop(delete_columns, axis = 1, inplace=True)

#機械学習アルゴリズムの入力とするため、pandas.DataFrameを特徴量と目的変数に分割する例
y_train = train['Survived']                #trainのSurvivedをy_trainへ
X_train = train.drop('Survived', axis=1)   #trainのSurvived以外をX_trainへ
X_test = test.drop('Survived', axis=1)     #testのSurvived以外をX_testへ

#インデクシング(データの取り出し方の手法)-----------------------------------------------------------------------
#[:len(train)] #[開始位置 : 終了位置]のように指定する
#省略した場合は、開始位置は最初から、終了位置は最後までになる
train = data[:len(train)] #最初からlen(train)番目までを取り出したpandas.DataFrame #len(train)はtrainの行数を表す
test = data[len(train):]



#**************************機械学習アルゴリズムの学習・予測****************************#

from sklearn.linear_model import LogisticRegression

#LogisticRegression()---------------------------------------------------------------
#ロジスティック回帰
#clfはClassifier(分類器)の意味
#param1: 損失(penalty)を指定。l2にすると「L2 正則化」
#param2: 解の探索手法(solver)を指定。sagにすると「sag(Stochastic Average Gradient)」
#param3: 乱数のseed(random_state)を指定。
clf = LogisticRegression(penalty='l2', solver='sag', random_state=0)

#fit()-------------------------------------------------------
#学習
clf.fit(X_train, y_train) #X_trainとy_trainの対応関係を学習

#predict()---------------------------------------------------
#予測
y_pred = clf.predict(X_test) #学習したモデルからX_testに対する予測を行う


#clf.fit()で学習し、clf.predict()で予測するのは、sklearnの機械学習アルゴリズムを使う場合に共通する書き方


#**************************予測結果をCSVファイルにする****************************#
sub = pd.read_csv('../input/titanic/gender_submission.csv') #submit用のcsvファイルのサンプルを読み込み、subに格納
sub['Survived'] = list(map(int, y_pred))                    #subのSurvivedに、y_predを整数にした値を代入
sub.to_csv('submission.csv', index=False)                   
#subをsubmission.csvというcsvファイルに書き出しindex=Falseとすることで、ファイル保存時にpandas.DataFrameの行のindex番号を付与しないようにしている