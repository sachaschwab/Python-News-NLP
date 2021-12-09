import pandas as pd
import nltk

def __init__(self):
    self.top_n = 10 # Default

def preprocess(csv_file):
    ''' Input: Tab delimited text file with named columns
            'title' (str, required) | 'content' (str, required) | 'date' (str, optional)
        Output: Dataframe with preprocessed text
        Remarks: For demo, use the sample file provided in /data
    '''
    # Check columns
    df = pd.DataFrame(csv_file)
    
    # Preprocess using NLTK
    # Output

