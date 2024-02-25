class Iterable:
    def create_Iterator(self):
        pass
class Iterator:
    def next(self):
        pass
    def hasNext(self):
        pass
class MyIterable(Iterable):
    def __init__(self) -> None:
        self.collection=[]
    def add(self,item):
        self.collection.append(item)
    def create_Iterator(self):
        return MyIterator(self)

class MyIterator(Iterator):
    def __init__(self,iterable) -> None:
        self.iterable=iterable
        self.index=0
    def hasNext(self):
        return self.index<len(self.iterable.collection)
    def next(self):
        if self.hasNext():
            item=self.iterable.collection[self.index]
            self.index+=1
            return item

if __name__=="__main__":
    it=MyIterable()
    for num in range(1000):
        it.add(num)
    _Iterator=it.create_Iterator()
    while _Iterator.hasNext():
        i=_Iterator.next()
        print(i)

#-------------------------------Sample Without OOP/Pattern------------------------------
#import itertools
#numbers=[200,100,4,2,5,6,70,60,40,10]
#for item in itertools.islice(iter(numbers),None):
#    print(item)
