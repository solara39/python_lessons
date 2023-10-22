#!/usr/bin/env python
# coding: utf-8

# In[2]:


#第8章：大規模データの検索


# In[3]:


#８−１線形探索と二分探索


# In[11]:


def find_linear(data, name): #計算量はdataの長さに比例する→O(n)
    for i in range(len(data)):
        if data[i] == name:
            return True
    return False


# In[12]:


find_linear(['Tom', 'Alice', 'Ken', 'John'], 'Ken')


# In[17]:


def find_bisection(data, name): #2**k = nより計算量はO(logn)
    start = 0
    end = len(data)
    while start != end:
        center = (start + end) // 2
        if data[center] == name:
            return True
        if name < data[center]:
            end = center
        else:
            start = center + 1
    return False


# In[22]:


data = [ 'Alice', 'David', 'John', 'Ken', 'Tom']
print(find_bisection(data, 'Sora'))
print(find_bisection(data, 'Tom'))


# In[25]:


# ８−２ヒストグラムの計算


# In[40]:


def histogram(data): #商品数：n、カテゴリ数：mとすると、計算量はO(nm)
    result = []
    for i in range(len(data)):
        put_item(result, data[i])
    return result

def put_item(res, item):
    for i in range(0, len(res)):
        if res[i][0] == item:
            res[i][1] += 1
            return
    res.append([item, 1])
    
def histogram_sorted(data): #計算量はO(n)
    result = []
    item = data[0]
    c = 1
    for i in range(1, len(data)):
        if item == data[i]:
            c += 1
        else:
            result.append([item, c])
            item = data[i]
            c = 1
    result.append([item, c] )
    return result


# In[41]:


print(histogram(['A', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A']))
print(histogram_sorted(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C']))


# In[43]:


#８−３併合整列法


# In[48]:


def mergesort(data): #計算量はT(n) = 2T(n/2) + O(n)より　O(nlogn)
    n = len(data)
    if n <= 1:
        return data
    else:
        data1 = mergesort(data[0 : n // 2])
        data2 = mergesort(data[n // 2 : n])
        return merge(data1, data2)
    
import ita
def merge(data1, data2):
    result = ita.array.make1d(len(data1) + len(data2))
    i1 = 0
    i2 = 0
    for i in range(0, len(result)):
        if (i2 >= len(data2) or (i1 < len(data1) and data1[i1] <= data2[i2])):
            result[i] = data1[i1]
            i1 += 1
        else:
            result[i] = data2[i2]
            i2 += 1
    return result


# In[49]:


merge([2, 5, 7, 10], [1, 3, 4, 8])


# In[50]:


# ８−４【発展】整列のアルゴリズムと空間計算量


# In[52]:


def simplesort(data): #要素数をnとすると計算量はO(n**2)
    for i in range(0, len(data)):
        j = min_index(data, i)
        swap(data, i, j)
        
def min_index(data, i):
    m = i
    for j in range(i + 1, len(data)):
        if data[j] < data[m]:
            m = j
    return m

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[i] = tmp


# In[53]:


#８−５様々なデータ構造


# In[56]:


def histogram_dict(data):
    result = {}
    for i in range(0, len(data)):
        item = data[i]
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


# In[57]:


print(histogram_dict(['A', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A']))


# In[59]:


def ngram(s, n):
    l = len(s)
    result = {}
    s = s + '$' * n
    for i in range(0, l):
        result[s[i : i + n]] = i
    return result


# In[67]:


print(ngram('検索アルゴリズムの改善',3))


# In[68]:


def ng_search(s, ngram, n, query):
    nq = (query + '$' * n)[0 : n]
    if nq in ngram:
        idx = ngram[nq]
        if s[idx : idx + len(query)] == query:
            return idx
    return -1


# In[75]:


s = '検索アルゴリズムの改善'
ng = ngram(s, 3)
print(ng)


# In[76]:


ng_search(s, ng, 3, 'アルゴリズム')


# In[ ]:




