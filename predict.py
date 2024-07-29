from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
import sys

if len(sys.argv) != 2:
    print("Usage: predict.py <test_file>")
    sys.exit(-1)

test_file = sys.argv[1]

spark = SparkSession.builder.appName("WineQualityPrediction").getOrCreate()

# Load the test data
test_data = spark.read.csv(test_file, header=True, inferSchema=True)

# Print schema of the original test data
print("Schema of original test_data:")
test_data.printSchema()

# Show a sample of the original test data
test_data.show()

# Assemble features
assembler = VectorAssembler(inputCols=test_data.columns[:-1], outputCol="features")
transformed_data = assembler.transform(test_data)

# Print schema of the transformed data
print("Schema of transformed_data:")
transformed_data.printSchema()

# Show a sample of the transformed data
transformed_data.show()

# Check if 'quality' column exists in the transformed data
if 'quality' in transformed_data.columns:
    print("Column 'quality' found in transformed_data")
else:
    print("Column 'quality' NOT found in transformed_data")
    sys.exit(-1)

# Select the required columns
try:
    test_data = transformed_data.select("features", "quality")
    print("Schema of test_data after select:")
    test_data.printSchema()
except Exception as e:
    print(f"Error selecting columns: {e}")
    sys.exit(-1)

# Show a sample of the selected data
test_data.show()

# Load the model
try:
    model = LogisticRegressionModel.load("/home/ec2-user/wine_quality_model")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(-1)

# Make predictions
predictions = model.transform(test_data)

# Evaluate the model
evaluator = MulticlassClassificationEvaluator(labelCol="quality", predictionCol="prediction", metricName="f1")
f1_score = evaluator.evaluate(predictions)

print(f"F1 Score: {f1_score}")

spark.stop()