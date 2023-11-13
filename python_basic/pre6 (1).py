# -*- coding: utf-8 -*-
"""pre6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v2X-4P7kYVMu68HtjtAHgSeqqms0I57h

# 第6回予習課題

[English version](https://colab.research.google.com/drive/10qXpx0c0rcYZmZ-iT-qsfNfMf45zDj0o)

## Pre6-1. 行列の最大要素とそのインデックス

数のリストのリスト `M` が与えられたとき、`M` の要素の要素 `M[i][j]` のうちの最大要素 `m` と、
そのインデックス `i`, `j` を、
```Python
(i, (j, m))
```
という形のタプルにして返す関数 `find_max_indices(M)` を定義してください。
for文やwhile文や再帰を使わずに、
内包表記や関数 `max` などを使って定義することを試みてください。
（内包表記の中では `for` を使っても構いません。）

`M` は空リストではなく、`M` の要素であるリストも空でないと仮定して構いません。
また、`M` の最大要素は `M` に1回のみ出現すると仮定して構いません。
"""

##########################################################
##  <[ pre6-1-find_max_indices ]> 解答セル (Answer cell)
##  このセルの複製・削除を禁ず (Neither copy nor delete this cell)
##########################################################

QUESTION_EXISTS = False # 質問がある場合は True に変えて，このセル内のコメントとして質問を記述してください
                        # Change to True if you have questions, and describe them as comments in this cell

def find_max_indices(M):
  elements = [(i, (j, elem)) for i, row in enumerate(M) for j, elem in enumerate(row)]
  return max(elements, key=lambda x: x[1][1])

"""提出前に以下のテストセルを実行し、エラーがでないことを確認してください。"""

print(find_max_indices([[1,2,3],[9,8,7,6],[4,5]]) == (1, (0, 9)))
print(find_max_indices([[1,2,3],[0,9,8,7,6],[4,5]]) == (1, (1, 9)))

"""## Pre6-2. 最初の要素を除いたイテラブル

`__init__` メソッドと `__iter__` メソッドのみを持つ次のようなクラス `drop_first` を定義してください。
`drop_first` のコンストラクタは引数 `iterable` を持ちます。
`iterable` にはイテラブルを与えます。

`__init__`　メソッドは、`iterable` に関数 `iter` を適用して得られたイテレータを適当な属性に記録し、
さらに、そのイテレータに対して関数 `next` を1回呼び出します。

`__iter__` メソッドはその属性に記録したイテレータをそのまま返します。

たとえば、`drop_first([1,2,3])` として `drop_first` のインスタンスを作ると、
以下のように、最初の要素 `1` を飛ばした繰り返しが行われます。
```Python
for x in drop_first([1,2,3]):
    print(x)
```
`2` と `3` が印字されます。
"""

##########################################################
##  <[ pre6-2-drop_first ]> 解答セル (Answer cell)
##  このセルの複製・削除を禁ず (Neither copy nor delete this cell)
##########################################################

QUESTION_EXISTS = False # 質問がある場合は True に変えて，このセル内のコメントとして質問を記述してください
                        # Change to True if you have questions, and describe them as comments in this cell

class drop_first:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        next(self.iterator, None)
    def __iter__(self):
        return self.iterator

"""提出前に以下のテストセルを実行し、エラーがでないことを確認してください。"""

assert list(drop_first([1,2,3])) == [2,3]