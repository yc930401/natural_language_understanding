# spoken_language_understanding
Spoken Language Understanding with Bidirectional LSTM

## Introduction

My firends doing NLP in China told me that analysing chinese text is a little bit different from analysing sentences in English, because word segmentation is needed. Then I began to think about how to do word segmentation in Chinese, adn I found that Chinese word segmentaion is very similar to POS tag in English and IOB labels (Sopken Language Understanding). So today, I use ATIS dataset to build a model to understand english. There are also some other models, like statistical model, dictionary based model and models that combine the two. Please read the references for more information.

## Methodology

1. Prepare training and testing data (The shape of data to input to the model). 
2. Build a Bidirectional LSTM model
3. Train the model on one of the sentences at a time because they are of different length.
4. Evaluate model and show sample output.

## Result

#### Accuracy and F1 score
Test Accuracy: 0.9789094863627057
Test F1: 0.9778037223501733


#### Smaple output
Sentence: ['i', 'need', 'to', 'take', 'a', 'united', 'airlines', 'flight', 'on', 'june', 'eighth', 'from', 'westchester', 'county', 'to', 'cincinnati', 'after', 'DIGIT', 'pm'] 
 Real: ['O', 'O', 'O', 'O', 'O', 'B-airline_name', 'I-airline_name', 'O', 'O', 'B-depart_date.month_name', 'B-depart_date.day_number', 'O', 'B-fromloc.city_name', 'I-fromloc.city_name', 'O', 'B-toloc.city_name', 'B-depart_time.time_relative', 'B-depart_time.time', 'I-depart_time.time'] 
 Predict: ['O', 'O', 'O', 'O', 'O', 'B-airline_name', 'I-airline_name', 'O', 'O', 'B-depart_date.month_name', 'B-depart_date.day_number', 'O', 'B-fromloc.city_name', 'I-fromloc.city_name', 'O', 'B-toloc.city_name', 'B-depart_time.time_relative', 'B-depart_time.time', 'I-depart_time.time'] 

Sentence: ['list', 'flights', 'from', 'memphis', 'to', 'miami', 'on', 'wednesday'] 
 Real: ['O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name'] 
 Predict: ['O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name'] 

Sentence: ['which', 'flights', 'leave', 'on', 'monday', 'from', 'montreal', 'and', 'arrive', 'in', 'chicago', 'in', 'the', 'morning'] 
 Real: ['O', 'O', 'O', 'O', 'B-depart_date.day_name', 'O', 'B-fromloc.city_name', 'O', 'O', 'O', 'B-toloc.city_name', 'O', 'O', 'B-arrive_time.period_of_day'] 
 Predict: ['O', 'O', 'O', 'O', 'B-depart_date.day_name', 'O', 'B-fromloc.city_name', 'O', 'O', 'O', 'B-toloc.city_name', 'O', 'O', 'B-arrive_time.period_of_day'] 

Sentence: ['i', 'need', 'a', 'flight', 'that', 'goes', 'from', 'boston', 'to', 'orlando'] 
 Real: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name'] 
 Predict: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name'] 

Sentence: ['show', 'me', 'one', 'way', 'flights', 'from', 'milwaukee', 'to', 'orlando', 'on', 'wednesday'] 
 Real: ['O', 'O', 'B-round_trip', 'I-round_trip', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name'] 
 Predict: ['O', 'O', 'B-round_trip', 'I-round_trip', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name'] 

Sentence: ['cleveland', 'to', 'miami', 'on', 'wednesday', 'arriving', 'before', 'DIGIT', 'pm'] 
 Real: ['B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name', 'O', 'B-arrive_time.time_relative', 'B-arrive_time.time', 'I-arrive_time.time'] 
 Predict: ['B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name', 'O', 'B-arrive_time.time_relative', 'B-arrive_time.time', 'I-arrive_time.time'] 

Sentence: ['is', 'there', 'ground', 'transportation', 'available', 'at', 'the', 'denver', 'airport'] 
 Real: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-airport_name', 'I-airport_name'] 
 Predict: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-airport_name', 'I-airport_name'] 

Sentence: ['list', 'flights', 'from', 'pittsburgh', 'to', 'newark', 'on', 'monday', 'morning'] 
 Real: ['O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name', 'B-depart_time.period_of_day'] 
 Predict: ['O', 'O', 'O', 'B-fromloc.city_name', 'O', 'B-toloc.city_name', 'O', 'B-depart_date.day_name', 'B-depart_time.period_of_day'] 

Sentence: ['please', 'list', 'flights', 'from', 'st.', 'louis', 'to', 'st.', 'paul', 'which', 'depart', 'after', 'DIGITDIGIT', 'am', 'thursday', 'morning'] 
 Real: ['O', 'O', 'O', 'O', 'B-fromloc.city_name', 'I-fromloc.city_name', 'O', 'B-toloc.city_name', 'I-toloc.city_name', 'O', 'O', 'B-depart_time.time_relative', 'B-depart_time.time', 'I-depart_time.time', 'B-depart_date.day_name', 'B-depart_time.period_of_day'] 
 Predict: ['O', 'O', 'O', 'O', 'B-fromloc.city_name', 'I-fromloc.city_name', 'O', 'B-toloc.city_name', 'I-toloc.city_name', 'O', 'O', 'B-depart_time.time_relative', 'B-depart_time.time', 'I-depart_time.time', 'B-depart_date.day_name', 'B-depart_time.period_of_day'] 

Sentence: ['what', 'is', 'the', 'lowest', 'fare', 'from', 'washington', 'dc', 'to', 'montreal'] 
 Real: ['O', 'O', 'O', 'B-cost_relative', 'O', 'O', 'B-fromloc.city_name', 'B-fromloc.state_code', 'O', 'B-toloc.city_name'] 
 Predict: ['O', 'O', 'O', 'B-cost_relative', 'O', 'O', 'B-fromloc.city_name', 'B-fromloc.state_code', 'O', 'B-toloc.city_name'] 

## References
https://chsasank.github.io/spoken-language-understanding.html </br>
https://machinelearningmastery.com/develop-bidirectional-lstm-sequence-classification-python-keras/ </br>
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.95.4582&rep=rep1&type=pdf </br>
http://aclweb.org/anthology/D15-1141
