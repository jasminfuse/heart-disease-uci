import pickle
import numpy as np

with open('models/stdscalar.pkl','rb') as classifier_file:
    stdsclr = pickle.load(classifier_file)  

def standard_classifier(input):
    return stdsclr.transform(np.array(input).reshape(-1,13))

with open('models/model.pkl', 'rb') as model_file:
    loaded_classifier = pickle.load(model_file)

def predict(input):
    return loaded_classifier.predict(input)
