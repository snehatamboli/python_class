import pandas as pd 
a = {'a':100, 'b':200, 'c':300, 'd':400, 'e':800}
print("Original dictionary: ")
print(a)
new_series = pd.series(a)
print("converted series: ")
print(new_series) 