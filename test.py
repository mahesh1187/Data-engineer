import pandas as pd

url ="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

df = pd.read_parquet(url,iterator=True, chunksize=100000)


print (df.head(100))