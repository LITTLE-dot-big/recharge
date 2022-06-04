This is a simple program which predicts the price of the recharge based on the inputs given, i.e. 'amount of data' and 'validity'.
It uses machine learning concepts to train a model to do the job.
It is written in Python 3.7

Modules required: 
    1. pandas
    2. numpy
    3. sklearn
    4. matplotlib

The data is stored in a csv file. This data is extracted into a numpy 'ndarray'. The data can also be extracted into a pandas 'dataframe', and then converted into 'ndarray'. The steps to do the above are commented out.
Then the data is sliced into training and test sets. 
There are two models used in the program, the less accurate is commented out.
The program uses 'mean squared error' parameter to determine its accuracy, and the same is plotted using the 'matplotlib' module.
