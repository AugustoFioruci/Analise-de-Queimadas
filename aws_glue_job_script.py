import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("job_glue_curriculo", {})

# Lê dados do Glue Data Catalog (crawler)
df = spark.read \
    .option("header", "true") \
    .option("sep", ",") \
    .option("quote", "\"") \
    .option("escape", "\"") \
    .option("multiLine", "true") \
    .csv("s3://augustofioruci-incendios/raw/")


# Transformações (importante pro currículo)
df = df.dropDuplicates()
df = df.na.drop()

# Salva em Parquet no S3 (camada processed)
df.write.mode("overwrite").parquet(
    "s3://augustofioruci-incendios/processed/"
)

job.commit()
