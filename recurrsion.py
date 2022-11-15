import sys
def hello():
    print('hello world')
    hello()
sys.setrecursionlimit(111)
hello() 
