from pyspark.sql import functions as F



 incoming = spark.table("silver.dim_staff_updates")



 current = (spark.table("silver.dim_staff_updates_lineage"))



 key_col = "employee_nbr"



 ignore = {

     "employee_nbr",

     "published_date_time_utc",

     "extract_date_time_utc",

     "rn",

     "time_in_level",

     "staff_level_current_date"

 }



 compare_cols = [c for c in incoming.columns if c not in ignore]



 def row_hash(df):

     return F.sha2(

         F.concat_ws("||", *[

             F.coalesce(F.col(c).cast("string"), F.lit("0")) for c in compare_cols

         ]),

         256

     )



 incoming_h = incoming.withColumn("data_hash", row_hash(incoming))

 current_h = current.withColumn("data_hash", row_hash(current))





 cmp = (incoming_h.alias("n")

        .join(current_h.select(key_col, "data_hash").alias("c"), on=key_col, how="left")

        .withColumn("is_changed",

                    F.col("c.data_hash").isNull() | (F.col("n.data_hash") != F.col("c.data_hash")))

       )





 changed = cmp.filter(F.col("is_changed"))



 # display(changed.select(key_col, "is_changed", "published_date_time_utc"))

 result_df = cmp.select(

     F.col(key_col),

     F.col("published_date_time_utc").alias("event_ts"),

     F.col("published_date_time_utc"),

     F.col("is_changed"),

     F.current_timestamp().alias("load_ts")

 )



 result_df.write \

     .format("delta") \

         .mode("append") \

             .saveAsTable("silver.staff_change_events")





 latest_all_df = spark.table("silver.staff_change_events") \

     .groupBy(key_col) \

     .agg(

         F.max("published_date_time_utc").alias("latest_source_ts")

     )



 # display(latest_all_df)



 latest_change_df = spark.table("silver.staff_change_events") \

     .filter(F.col("is_changed") == True) \

     .groupBy(key_col) \

     .agg(

         F.max("published_date_time_utc").alias("latest_change_source_ts"),

         F.max("event_ts").alias("last_event_ts")

     )

 final_df = latest_all_df.alias("a") \

     .join(latest_change_df.alias("c"), key_col, "left")



 # display(final_df)



 final_df.write \

     .format("delta") \

         .mode("overwrite") \

             .saveAsTable("silver.staff_latest_published")

 

 

 

 



 