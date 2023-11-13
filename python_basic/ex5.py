# -*- coding: utf-8 -*-
"""ex5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3qYeggXJ6JW6-yhPS4uQIe8Je29daj-

# 第5回本課題

[English version](https://colab.research.google.com/drive/15MupnChkl2u1TxplWNRgHGg6njVCNtJM)

## Ex5-1. 圧縮行格納方式の変種

疎行列（$0$ を多く含む行列）を、非零要素のリストと非零要素の列インデックスのリストの組で表現する方法があります。

たとえば、
$$
A = \left(
\begin{array}{cccc} 1 & 2 & 3 & 0 \\ 0 & 0 & 0 & 1 \\ 2 & 0 & 0 & 2 \\ 0 & 0 & 0 & 1 \end{array}
\right)
$$
という行列$A$は、
非零要素のリスト `[1,2,3,1,2,2,1]` と、
行毎の非零要素のインデックス `[0,1,2]` `[3]` `[0,3]` `[3]` から成る非零要素の列インデックスのリスト`[[0,1,2],[3],[0,3],[3]]` で表現できます。
これは、圧縮行格納（compressed row storage, CRS）方式と呼ばれる形式に近いものです。

このような零要素をデータとしてそのまま保持しない行列表現を、疎表現と呼びます。
一方、全ての零要素をデータとしてそのまま保持する行列表現を、密表現と呼びます。
たとえば、リストのリストの形での行列$A$の密表現は `[[1,2,3,0],[0,0,0,1],[2,0,0,2],[0,0,0,1]]` です。

以上を踏まえ、非零要素のリスト `elems` と非零要素の列インデックスのリスト `colss` による疎表現を受け取り、**リストのリストの形**での密表現を返す関数 `crs2matrix(elems, colss)` を定義せよ。
ただし、入力は**正方行列**であると仮定してよく、`elems` には数値に限らず**任意の型のオブジェクト**が入り得るとする。

**注**：NumPyの配列を使って題意を満たすように `crs2matrix` を定義するのは間違えやすいので、その利用は推奨していない。どうしても使いたい場合、`dtype` 引数に `object` を指定する点に注意せよ。
"""

##########################################################
##  <[ ex5-1-crs2matrix ]> 解答セル (Answer cell)
##  このセルの複製・削除を禁ず (Neither copy nor delete this cell)
##########################################################

QUESTION_EXISTS = False # 質問がある場合は True に変えて，このセル内のコメントとして質問を記述してください
                        # Change to True if you have questions, and describe them as comments in this cell

def crs2matrix(elems, colss):
    n_rows = len(colss)
    result = []
    for i in range(n_rows):
      result.append([])
      for _ in range(n_rows):
        result[-1].append(0)

    index = 0
    for i, x in enumerate(colss):
      for _ in x:
        result[i][_] = elems[index]
        index += 1
    return result

"""提出前に以下のテストセルを実行し、エラーがでないことを確認してください。"""

assert crs2matrix([1,2,3,1,2,2,1], [[0,1,2],[3],[0,3],[3]]) == [[1,2,3,0],[0,0,0,1],[2,0,0,2],[0,0,0,1]]
assert crs2matrix([], [[],[],[],[]]) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
assert crs2matrix(['1','2'], [[0],[1]]) == [['1',0],[0,'2']]
