A way to solve 2 different coding tasks the way i see.

## Prerequisites:
- python3.7 installed system wide.
- make sure to call either `python tasks.py` if it defaults to python3.7 or `python3 tasks.py` when executing `.py` files. 
Also `py tasks.py` might work on some systems.

## Usage:

- install dependencies and see if it works using tests

or
 
- just type: `python tasks.py` and see output of a simpler test. 

## Step 1. Install dependencies:

Run `pre-setup` only if you don't have pip and virtualenv in your system:

```./pre-setup.sh```

Create env and install requirements:
```
 virtualenv -p python3 env
 source env/bin/activate
 pip install -r requirements.txt
```
 
## Step 2. Run tests:

```
pytest tests.py -s -vv
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

    
   
   
 
  
     
