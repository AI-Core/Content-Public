# %%
import pyspark
from pyspark.sql import SparkSession

import findspark
findspark.init()
# %%

session = SparkSession.builder.config().getOrCreate()
# %%

# %%
