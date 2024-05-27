# 技術課題1

公開URL: https://naokey.pythonanywhere.com/fib?n=10

ソースコードの構成
```
.
├── src
│   └── fib.py     (フィボナッチ数列の計算)
├── test
│   └── test.py    (ユニットテストの実装)
├── app.py         (ルーティング処理)
├── .gitignore
├── requirements.txt
└── README.md
```

## ルーティング
### 実装したエラーコード
#### 400 (Bad request.)
- パラメータ $n$ が見つからない
- $n$ が数字じゃない
- $n$ が負
- $n$ が200以上
  
> [!NOTE]
> $n = 200$ のとき $Fib(n) = 280571172992510140037611932413038677189525$ となる
> 値が大きくメモリが圧迫されてしまうため，これ以上大きいクエリを無効にする

#### 404 (Page not found.)
- 指定されたパスが見当たらない


## フィボナッチ数列の計算
[ソースコード](https://github.com/naokeyn/fib_api/blob/main/src/fib.py)

### 概要

フィボナッチ数列を数式で表すと次のようになる．

$Fib(0) = 1, Fib(1) = 1 $

$Fib(n) = Fib(n-1) + Fib(n-2) $ &nbsp; $ (n \geq 2)$

要素数 $n$ の配列を用意し， $Fib(0), Fib(1), Fib(2), ... Fib(n-2), Fib(n-1), Fib(n)$ を順に計算して配列に代入．
その際，直前に計算した値を配列から参照することで計算量を減らすことができる．



## ユニットテスト

[ソースコード](https://github.com/naokeyn/fib_api/blob/main/test/test.py)

### 正常に値を返しているか確認 (`test_valid_query`)
以下の3つの場合で検証を行い，正しく機能することを確認した
- $n=0$ で $Fib(n) = 1$
- $n=10$ で $Fib(n) = 55$
- $n=99$ で $Fib(n) = 218922995834555169026$

### 想定されるエラー (`test_invalid_query`)
- $n \geq 200$
- $n < 0$
- $n$ が数字以外
- クエリパラメータに $n$ が存在しない

これらのケースでステータスコードが`400`になることを確認した
