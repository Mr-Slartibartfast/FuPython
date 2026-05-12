from pyspark.sql import functions as F



 key_col = "employee_nbr"

 first_seen_df = spark.table("gold.dim_staff") \

     .groupBy("employee_nbr") \

     .agg(F.min("published_date_time_utc").alias("first_source_ts"))



 # display(first_seen_df)

 last_change_df = spark.table("silver.staff_change_events") \

     .filter(F.col("is_changed") == True) \

         .groupBy(key_col) \

             .agg(

                 F.max("published_date_time_utc").alias("last_change_ts"),

                 F.max("event_ts").alias("last_event_ts")

             )

 # display(last_change_df)

 final_df = first_seen_df.alias("f") \

     .join(last_change_df.alias("c"), key_col, "left") \

         .select(

             F.col(key_col),

             F.coalesce(

                 F.col("c.last_change_ts"),

                 F.col("f.first_source_ts")

             ).alias("effective_change_ts")

         )

 # display(final_df)

 final_df.write \

     .format("delta") \

         .mode("overwrite") \

             .saveAsTable("silver.staff_latest_published")