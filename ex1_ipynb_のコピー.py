# -*- coding: utf-8 -*-
"""ex1.ipynb のコピー

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H4k8IwskXNpvIX19J1e411mS35n4WTF3

# 第1回本課題

[English version](https://colab.research.google.com/drive/1wzBj7eKYi5cLEtAvL9W-7FLiwszjuTZi)

## Ex1-1. 三角形の分類

3本の線分の長さを表す非負数 `a`, `b`, `c` を受け取り、その線分が

* 三角形を構成しないならば 0
* 鋭角三角形を構成するならば 1
* 直角三角形を構成するならば 2
* 鈍角三角形を構成するならば 3

を返す関数 `classify_triangle(a, b, c)` を定義してください。
（ヒント：[余弦定理](https://ja.wikipedia.org/wiki/%E4%BD%99%E5%BC%A6%E5%AE%9A%E7%90%86)）
"""

##########################################################
##  <[ ex1-1-classify_triangle ]> 解答セル (Answer cell)
##  このセルの複製・削除を禁ず (Neither copy nor delete this cell)
##########################################################

QUESTION_EXISTS = False # 質問がある場合は True に変えて，このセル内のコメントとして質問を記述してください
                        # Change to True if you have questions, and describe them as comments in this cell

def classify_triangle(a, b, c):
    sides_list = [a, b, c]
    sides_list.sort()
    if sides_list[0] <= 0:
      return 0
    elif sides_list[2] >= sides_list[0] + sides_list[1]:
      return 0
    if sides_list[2] ** 2 < sides_list[1] ** 2 + sides_list[0] ** 2:
      return 1
    elif sides_list[2] ** 2 == sides_list[1] ** 2 + sides_list[0] ** 2:
      return 2
    else:
      return 3

"""提出前に以下のテストセルを実行し、エラーがでないことを確認してください。"""

assert classify_triangle(3,6,5) == 3
assert classify_triangle(3,4,5) == 2
assert classify_triangle(4,3,3) == 1
assert classify_triangle(1,1,3) == 0
assert classify_triangle(1,2,0) == 0

from google.colab import drive
drive.mount('/content/drive')