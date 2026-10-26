# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a1978c4a-740d-42e8-a612-a7040561b036",
# META       "default_lakehouse_name": "lh_bronze",
# META       "default_lakehouse_workspace_id": "9a883ddc-b4cf-4456-95ee-b946e4bd0599",
# META       "known_lakehouses": [
# META         {
# META           "id": "a1978c4a-740d-42e8-a612-a7040561b036"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

#Config
BASE_PATH  = 'Files/contratos'
LIST_YEARS = [2022,2023,2024,2025,2026]
TABLE_NAME = 'bronze_contratos'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#let us compare the cols (name and data type) for each year, using 2022 as the ref year
#we will also count the number of rows for each file
dict_year_cols = {}

sum_rows_files = 0

#arranging a dict with the years and its corresponding cols 
for year in LIST_YEARS:
    folder_file_path = f"/{year}/Contratos{year}.json"
    df = (
        spark.read
        .option('multiline', True)
        .json(BASE_PATH + folder_file_path)
    )
    dict_year_cols[year] = set (df.dtypes)
    print (f"{year} file row count : {df.count()}")
    sum_rows_files += df.count()

print ("Comparison below:")
#comparing the difference 
for year in dict_year_cols.keys():
    if year == 2022:
        continue
    
    comparison_2022_year = dict_year_cols[2022].difference(dict_year_cols[year])
    comparison_year_2022 = dict_year_cols[year].difference(dict_year_cols[2022])
    print (f"{year} -> missing: {comparison_2022_year} | extra: {comparison_year_2022}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#let's read the 5 files now and add the load timestamp column aswell as the source file column 

df = (
    spark.read
    .option('multiline', True)
    .json([f"{BASE_PATH}/{year}/Contratos{year}.json" for year in LIST_YEARS])
    .withColumn ("_source_file", F.col("_metadata.file_path"))
    .withColumn ("_load_ts", F.current_timestamp())
)

# Gate: don't overwrite the table unless every source row was read
df_row_count = df.count()

if df_row_count != sum_rows_files:
    raise ValueError(
        f"Row count mismatch: expected {sum_rows_files:,} rows from the source files, "
        f"got {df_row_count:,} in the DataFrame. Table not written."
    )

# Full-snapshot source -> overwrite, so the notebook is rerun-safe (idempotent)
df.write.format("delta").mode("overwrite").saveAsTable(TABLE_NAME)
print(f"{TABLE_NAME} written: {df_row_count:,} rows")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
