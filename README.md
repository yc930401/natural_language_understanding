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
![SLU](/scores.png) </br>

#### Smaple output
![SLU](/outputs.png) </br>

## References
https://chsasank.github.io/spoken-language-understanding.html </br>
https://machinelearningmastery.com/develop-bidirectional-lstm-sequence-classification-python-keras/ </br>
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.95.4582&rep=rep1&type=pdf </br>
http://aclweb.org/anthology/D15-1141
