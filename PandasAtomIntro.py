# first install pandas with pip
#pip install pandas
# or install this too
# pip install ipython
# pip install numpy / pip install numpy==1.19.3
import pandas

#make first dataframe
df = pandas.DataFrame([1,2,3],[1,2,3])
print(df)

# add column names
df1 = pandas.DataFrame([[1,2,3],[1,2,3]],columns = ["price","age","value"])
print(df1)

# add custom name for index or each row and here we have 2 row so we use 2 special indexes
df2 = pandas.DataFrame([[1,2,3],[1,2,3]],columns = ["price","age","value"], index =["first","second"])
print(df2)

# dictionary list
df3 = pandas.DataFrame([{"Name": "John"},{"Name":"Jack"}])
print(df3)

# dictionary list
df4 = pandas.DataFrame([{"Name": "John","surname":"jake"},{"Name":"Jack","surname":"blake"}])
print(df4)

#type(df1); dir(df1) # gives you all the methods you can use on this

# show mean of df which is ne columns
print(df.mean())

# print column 1 of dataframe 1
print(df1.price)
