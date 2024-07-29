from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
import os
import shutil

try:
    spark = SparkSession.builder \
        .appName("WineQualityPrediction") \
        .config("spark.driver.memory", "4g") \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:/home/ec2-user/log4j.properties") \
        .getOrCreate()

    # Load the training data with correct delimiter and schema
    train_data = spark.read.csv("TrainingDataset.csv", header=True, inferSchema=True, sep=';')

    # Display schema to verify data loading
    print("Schema of training data:")
    train_data.printSchema()
    
    # Print column names
    print("Column names of training data:")
    print(train_data.columns)

    # Clean column names
    train_data = train_data.toDF(*(c.replace('"', '') for c in train_data.columns))
    
    # Verify the 'quality' column exists
    if 'quality' not in train_data.columns:
        raise ValueError("Column 'quality' not found in the dataset.")

    train_data.show(5)

    # Assemble features
    assembler = VectorAssembler(inputCols=train_data.columns[:-1], outputCol="features")
    train_data = assembler.transform(train_data).select("features", "quality")

    # Show the transformed data
    print("Transformed training data:")
    train_data.show(5)

    # Train the model
    lr = LogisticRegression(labelCol="quality", featuresCol="features", maxIter=10)
    model = lr.fit(train_data)

    # Verify the model has been trained
    print("Model training completed successfully.")
    
    # Define model path
    model_path = "/home/ec2-user/wine_quality_model"

    # Check if the directory exists and handle it
    if os.path.exists(model_path):
        print(f"Directory {model_path} already exists. Removing directory.")
        shutil.rmtree(model_path)

    # Save the model
    model.write().overwrite().save(model_path)
    print("Model saved successfully.")

    # Stop the Spark session
    spark.stop()
except Exception as e:
    print("Error during SparkSession creation or job execution:", e)