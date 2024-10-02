from sklearn.ensemble import RandomForestClassifier
import pickle
import regex as re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from django.shortcuts import render
from .forms import TextInputForm
from .models import TextInput


def index(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = get_model_prediction(text)
            return render(request, 'main/index.html', {'form': form, 'result': result})
    else:
        form = TextInputForm()
    return render(request, 'main/index.html', {'form': form})

# Функция предобработки пользовательского текста
def preprocess(text):
  nlp = spacy.load('en_core_web_sm')
  text = re.sub('[^a-zA-Z0-9]', ' ', text.lower())
  doc = nlp(text)
  lemmatized_tokens = [token.lemma_ for token in doc]
  lemmatized_text = ' '.join(lemmatized_tokens)
  tfidf = pickle.load(open('TfidfWeights.sav' , 'rb'))
  return tfidf.transform([lemmatized_text])


# Функция получения предсказаний наилучшей модели
def get_model_prediction(text):
  model = pickle.load(open('classifier.sav', 'rb'))
  return model.predict(preprocess(text)).item()