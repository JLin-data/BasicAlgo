```Python

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        num_len = len (num)
        num_value = 0
        for i, j in enumerate(num):
            num_value += j * (10 ** (num_len-i-1))
            
        num_value = num_value + k
        
        newNum_list = []
        for k in range(len(str(num_value))):
            new_num = num_value % 10 
            num_value = num_value // 10
            newNum_list.append(new_num)
        
        newNum_list.reverse()
        return newNum_list
        
```

