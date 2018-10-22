# AssociationRule of Frequent itemsets
BruteForce/Apriori/FPgrowth

## 編譯環境:Anacoda2_spyder(python 2.7)

### AR.data
* 使用IBM-Quest-Data-Generator.exe產生DataSet
* 參數設定
  * Number of transactions in database = 1000
  * Average transaction length = 1
  * Number of items = 10
  * Large Itemsets:
    * Number of patterns = 10000
    *	Average length of pattern = 3
    *	Correlation between consecutive patterns = 0.25
    *	Average confidence in a rule = 0.75
    *	Variation in the confidence = 0.1

### BruteForce.py
* 使用暴力法取得Frequent itemsets
* 使用AR.data輸出結果
 * ![](https://i.imgur.com/XDLDDG9.png)

### Apriori.py
* 使用剪枝方法加快取得Frequent itemsets
* 使用AR.data輸出結果
 * ![](https://i.imgur.com/BvVUPGt.png)

### FPgrowth.py
* 使用FPtree來計算Frequent itemsets
* 使用AR.data輸出結果
 * ![](https://i.imgur.com/7F8V4dW.png)
