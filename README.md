 brain-test
A way to solve 2 different coding tasks the way i see.
 Install dependencies:

```
 virtualenv -p python3 env
 source env/bin/activate
 pip install -r requirements.txt
```
 
 Run tests:

```
pytest tasks.py -s -vv
```


### TASK 1. 

Given a non-empty string s and a list wordList containing a list of non-empty tokens, 
determine if s can be represented as a concatenation of tokens from the list (where each token may be used several times). 
You may assume the dictionary does not contain duplicate tokens.

```
s = "whataniceday";
wordList = [ "a", "what", "an", "nice", "day"];
-> true
 
s = "dawhaty",  
wordList = ["a", "what", "an", "nice", "day"].
-> false

s = "abc",
wordList = ["a", "ab", "bc"].
-> true
```




 ### TASK 2
 Given a collection of intervals, merge all overlapping intervals.
 For example,
 ```
 Given [2,6],[8,10],[1,3],[15,18],[18,21] 
 return [1,6],[8,10], [15, 21]


 Given [2,6],[8,10],[1,3],[15,18],[18,21],[3, 15] ---> [1,21]
 ```

    
   
   
 
  
     