# Time comparison of algorithms that calculate the sum of integers in the interval [a, b]

## System requeriments (recommended)
* Ubuntu 20.04 LTS

## 1. Configure and run the app

1.1 Install the stable/latest version of Python 3 and verify their version.
```
$ sudo apt install python3
```
```
$ python3 --version
```

1.2 Run the app
```
$ python3 app.py
```

## 2. Output
> e.g.
Time comparison of algorithms that calculate the sum of integers in the interval [a, b].
----------------------------------------------------------------------------------------
Ordenered list: [100, 101, ..., 999999, 1000000]
size of list is 999901
----------------------------------------------------------------------------------------
Algorithm       Sum             Lapsed time
Iterative sum   500000495050    0.0463950634s
Standart sum    500000495050    0.0065970421s
Gauss sum       500000495050    0.0000035763s

# Reference Links
[StackExchange Math - Get the sum of numbers from 75 to 995 with interval of 5](https://math.stackexchange.com/questions/1692833/get-the-sum-of-numbers-from-75-to-995-with-interval-of-5)