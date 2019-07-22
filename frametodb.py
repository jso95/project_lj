#将输入的dataframe转成dic存到MongoDB
#key为dataframe的col，value为每一行对应值，将dataframe每一行输入到同一行
import pymongo
from pandas import Series
def todb(frame,num):
    data=frame.ix[num,:]
    keys=list(frame.columns)
    dic={}
    for i in keys:
        dic[i]=data[i]
    return dic
def frametodb(frame,database,collection):
    client=pymongo.MongoClient('mongodb://localhost:27017')
    db=client[database]
    col=db[collection]
    allnumlist=Series(range(frame.shape[0]))
    alldata=list(allnumlist.apply(lambda x:todb(frame,x)).values)
    col.insert_many(alldata)
