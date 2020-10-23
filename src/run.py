from model_builder import train_model
from model_builder import predictions_from_model
import pandas as pd
import pickle
import time

input_data_filepath   = '../data/raw/trainSet.csv'
new_data_filepath     = '../data/raw/candidateTestSet.csv'
model_filepath        = '../models/final_model_object.pckl'
preprocessor_filepath = '../models/preprocessor_object.pckl'
output_prediction_filepath = '../output/candidateTestSet_with_categories.csv'


if __name__ == "__main__":
    # fetch training data:
    df_train = pd.read_csv(input_data_filepath, header=None, names=['query', 'category'])
    df_train['category'] = pd.Categorical(df_train['category'].astype(str))

    # train model, return preprocessing steps and model object:
    preprocessor, trained_model = train_model(df_train)
    
    with open(model_filepath, 'wb') as filepath:
        pickle.dump(trained_model, filepath)
    
    with open(preprocessor_filepath, 'wb') as filepath:
        pickle.dump(preprocessor, filepath)
        
    # fetch unlabelled data, add computed predictions, output to file:
    df_new = pd.read_csv(new_data_filepath, header=None, names=['query'])
    df_new['category_predicted'] = predictions_from_model(trained_model, preprocessor, df_new['query'])
    df_new.to_csv(output_prediction_filepath, index=False)
