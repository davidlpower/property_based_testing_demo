# eFFN Testing Tip: Property-based tests

# Library
In this demo the property-based testing library used was [Hypothesis](http://hypothesis.works/)

# Structure
* application - a basic run length encoder to test
* slides - demo slides
* tests - parametrised tests and property-based tests

# Getting Started
First, you'll need to make sure you have a few Python modules installed
```pip install parameterized hypothesis```

Next, make sure your ```$PYTHONPATH``` is pointed to the root directory of this project

# Run The Tests
From the root directory, run 
```pytest ./tests/test_run_length_encoding.py``` 
or
```pytest ./tests/test_run_length_encoding_property_based.py```

