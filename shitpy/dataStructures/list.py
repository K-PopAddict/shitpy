from __future__ import print_function
from random import shuffle
import time

def _is_sorted(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            f=1
        else:
            f=0
            break
    return f

class list:
    
    def __init__(self,arr):
        self.arr = arr

    def shitSort(self):
        self.arr = self.arr[:]
        count = 0
        if len(self.arr)>=8:
            print("Please don't! It will take me forever to sort this shit!")
            time.sleep(2)
            print("Fuck it! I am sorting")
            while not _is_sorted(self.arr):
                shuffle(self.arr)
                count+=1
                if count%20000==0:
                    time.sleep(0.5)
                    print(self.arr)
                    print("Shit! This one is wrong, let me check another permutation!")
                if count == 10000000:
                    print("Forget it! I can't do!")
                    return None
            print("Huff! Finally")
            return self.arr
        
        else:
            flag = 0
            while not _is_sorted(self.arr):
                shuffle(self.arr)
                count+=1
                if count%20==0:
                    time.sleep(1)
                    print(self.arr)
                    print("Shit! This one is wrong, let me check another permutation!")
                    flag = 1
            if flag==1:
                print("Huff! Finally")
            else:
                print("This is too easy, even for me!")
            return self.arr
    
    def __repr__(self):
        return str(self.arr)
        
    def __str__(self):
        return str(self.arr)
    