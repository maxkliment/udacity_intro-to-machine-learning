#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
def nan_str(a):
    if a == 'NaN':
        return None
    else:
        return a

import pickle
import pandas as pd
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
enron_df = pd.DataFrame.from_dict(enron_data, orient='index').applymap(nan_str)
print enron_df
print enron_df.axes
print enron_df.shape
print enron_df['poi'].sum()
print enron_df['total_stock_value']['PRENTICE JAMES']
print enron_df['from_this_person_to_poi']['COLWELL WESLEY']
print enron_df['exercised_stock_options']['SKILLING JEFFREY K']
print enron_df['total_payments'].drop('TOTAL').idxmax(), enron_df['total_payments'].drop('TOTAL').max()
print enron_df['salary'].count(), enron_df['email_address'].count()
print enron_df['total_payments'].count(), 1.0 * enron_df['total_payments'].count() / enron_df.shape[0]
print enron_df[enron_df['poi'] == True]['total_payments'].count(), \
      1.0 * enron_df[enron_df['poi'] == True]['total_payments'].count() / enron_df['poi'].sum()

#enron_arr = enron_df.fillna(0).as_matrix()
