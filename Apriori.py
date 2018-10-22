import pandas as pd
import time
import itertools

def findsubsets(fSet,nElement):
        return set(itertools.combinations(fSet,nElement))

def GetSupport(item,TransactionDF):
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


def Apriori(TransactionDF, Itemset, minsup):
        Freq_itemsets = []
        for nE in range(1,len(Itemset)+1):
                newItemset = set()
                for item_X in findsubsets(Itemset,nE):
                        item_X = set(item_X)
                        sup = GetSupport(item_X,TransactionDF)
                        if sup >= minsup:
                                newItemset.update(item_X)
                                Freq_itemsets.append(item_X)
                                print item_X,sup
                Itemset = newItemset
        return Freq_itemsets

def DataInput():
        df = pd.read_table("AR.data",delim_whitespace=True,header=None)  
        df = df.drop(labels=1, axis=1)
        df.set_index(0,inplace=True)
        Itemset = set()
        for item in df[2]:
                Itemset.add(item)
        return df,Itemset        
        
if __name__ == "__main__":
        tStart = time.time()
        
        df,Itemset = DataInput()
        FI = Apriori(df,Itemset,0.15)
        
        tEnd = time.time()
        print "It cost %f sec" % (tEnd - tStart)
