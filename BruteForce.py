import pandas as pd

import itertools

def findsubsets(fSet,nElement):
        return set(itertools.combinations(fSet,nElement))

def SetSupport(item,TransactionDF):
        Support = 0
        for idx in range(1,TransactionDF.index.max()):
                if str(type(TransactionDF[2][idx])) != "<type 'numpy.int64'>":
                        TransactionSet = set(TransactionDF[2][idx])
                else:
                        TransactionSet = set()
                        TransactionSet.add(TransactionDF[2][idx])
                if item.issubset(TransactionSet):
                        Support = Support + 1
        return float(Support)/TransactionDF.index.max()


def BruteForce(TransactionDF, Itemset, minsup):
        Freq_itemsets = []
        for nE in range(1,len(Itemset)+1):
                for item_X in findsubsets(Itemset,nE):
                        item_X = set(item_X)
                        sup = SetSupport(item_X,TransactionDF)
                        if sup >= minsup:
                                Freq_itemsets.append(item_X)
                                print item_X,sup
        return Freq_itemsets

if __name__ == "__main__":
        df = pd.read_table("AR.data",delim_whitespace=True,header=None)  
        df = df.drop(labels=1, axis=1)
        df.set_index(0,inplace=True)
        Itemset = set()
        for item in df[2]:
                Itemset.add(item)
        FI = BruteForce(df,Itemset,0.15)
