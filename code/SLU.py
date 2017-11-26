import pickle
import os.path
import numpy as np
from keras.layers.embeddings import Embedding
from keras.models import Sequential, load_model
from sklearn.metrics import f1_score, accuracy_score
from keras.layers import LSTM, Dense, TimeDistributed, Bidirectional, Dropout
import warnings
warnings.filterwarnings('ignore')

epochs = 10

def get_data():
    train_set, valid_set, test_set, dicts = pickle.load(open("atis.pkl", 'rb'), encoding='latin1')
    words2idx, labels2idx = dicts['words2idx'], dicts['labels2idx']

    x_train, _, y_train = train_set
    x_valid, _, y_valid = valid_set
    x_test, _, y_test = test_set

    # Create index to word/label dicts
    idx2words  = {words2idx[k]:k for k in words2idx}
    idx2labels = {labels2idx[k]:k for k in labels2idx}

    n_classes = len(idx2labels)
    n_vocab = len(idx2words)
    return x_train, y_train, x_valid, y_valid, x_test, y_test, n_classes, n_vocab, idx2words, idx2labels


def builg_model(n_vocab, n_classes):
    model = Sequential()
    model.add(Embedding(n_vocab, 100, input_length=None))
    model.add(Dropout(0.25))
    model.add(Bidirectional(LSTM(100, return_sequences=True)))
    model.add(TimeDistributed(Dense(n_classes, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model


if __name__ == '__main__':
    x_train, y_train, x_valid, y_valid, x_test, y_test, n_classes, n_vocab, idx2words, idx2labels = get_data()
    if os.path.exists('SLU.h5'):
        model = load_model('SLU.h5')
    else:
        model = builg_model(n_vocab, n_classes)

    for iteration in range(1, epochs+1):
        print('---------------- Iteration {} ----------------'.format(iteration))
        for i in range(len(x_train)):
            model.train_on_batch(x_train[i][np.newaxis,:], np.eye(n_classes)[y_train[i]][np.newaxis, :])
        model.save('SLU.h5')

        y_pred = []
        for i in range(len(x_test)):
            y_pred.append(np.argmax(model.predict_on_batch(x_test[i][np.newaxis,:]), -1)[0])

        accuracy = np.mean([accuracy_score(y_test[i], y_pred[i]) for i in range(len(y_test))])
        f1 = np.mean([f1_score(y_test[i], y_pred[i], average='weighted') for i in range(len(y_test))])
        print('Test Accuracy: {}\n Test F1: {}'.format(accuracy, f1))

    # show example
    sample_indices = np.random.randint(0, len(x_test), size=10)
    sample_texts = [x_test[i] for i in sample_indices]
    sample_labels = [y_test[i] for i in sample_indices]
    pred_labels = [np.argmax(model.predict(sample_texts[i][np.newaxis, :]), -1)[0] for i in range(len(sample_indices))]
    for i in range(len(sample_indices)):
        sentence = [idx2words[j] for j in sample_texts[i]]
        real_label = [idx2labels[j] for j in sample_labels[i]]
        pred_label = [idx2labels[j] for j in pred_labels[i]]
        print('Sentence: {} \n Real: {} \n Predict: {} \n'.format(sentence, real_label, pred_label))

