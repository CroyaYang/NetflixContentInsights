from flask import Flask, render_template, flash, request
import numpy as np
import pandas as pd
#pd.set_option('display.max_columns', 500) # Maximum display columns setting
#np.set_printoptions(suppress=True) # Enables scientific notation to be used when outputting floating point

import nltk
# Use the code below to download the NLTK package, a straightforward GUI should pop up
#nltk.download()
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import joblib

#stop_words = stopwords.words('english')
# Define our own list of deactivated words
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
# Adds stuff to our stop words list
stop_words.extend(['.',','])

def remove_stopwords(list_of_tokens):
    """
    Removes stopwords
    移除停用词函数
    """
    cleaned_tokens = []

    for token in list_of_tokens:
        if token in stop_words: continue
        cleaned_tokens.append(token)

    return cleaned_tokens

def stemmer(list_of_tokens):
    '''
    Takes in an input which is a list of tokens, and spits out a list of stemmed tokens.
    词干提取函数
    '''
    stemmed_tokens_list = []

    for i in list_of_tokens:

        token = PorterStemmer().stem(i)
        stemmed_tokens_list.append(token)

    return stemmed_tokens_list

def lemmatizer(list_of_tokens):
    '''
    词形还原函数
    '''
    lemmatized_tokens_list = []

    for i in list_of_tokens:
        token = WordNetLemmatizer().lemmatize(i)
        lemmatized_tokens_list.append(token)

    return lemmatized_tokens_list


def the_untokenizer(token_list):
        '''
        Returns all the tokenized words in the list to one string.
        Used after the pre processing, such as removing stopwords, and lemmatizing.
        令牌化的单词重新组合成字符串
        '''
        return " ".join(token_list)

def clean_string(my_string): # Text preprocessing of input strings
    tokenized_list = word_tokenize(my_string)
    removed_stopwords = remove_stopwords(tokenized_list)
    stemmed_words = stemmer(removed_stopwords)
    lemmatized_words = lemmatizer(stemmed_words)
    back_to_string = the_untokenizer(lemmatized_words)
    return back_to_string

# Flask Initialization
app = Flask("genre_prediction", template_folder='templates')
app.secret_key = "super secret key"
# Defining Flask Routes
@app.route('/', methods=["GET","POST"])

def predict():
    #error = 'trying post'
    try:
        # 如果是POST请求，表示用户提交了表单
        if request.method == "POST":
            
            # Get user-entered movie plot summary
            my_string = request.form['plot']
            
            # Load the model and other necessary data
            my_model = joblib.load('../models/netflix_logistic_model.pkl')
            my_scaler = joblib.load('../models/netflix_standard_scaler.pkl')
            my_tfidf = joblib.load('../models/netflix_tfidf_min20.pkl')
            
            # Define the movie type column
            genre_cols = ['g_Independent Movies', 'g_Faith & Spirituality', 'g_Documentaries', 'g_LGBTQ Movies',
              'g_International TV Shows', 'g_TV Thrillers', 'g_TV Dramas', 'g_Stand-Up Comedy & Talk Shows',
              'g_Thrillers', 'g_Anime Features', 'g_Science & Nature TV', 'g_TV Horror', 'g_Movies',
              'g_Korean TV Shows', 'g_Teen TV Shows', 'g_Action & Adventure', 'g_Crime TV Shows',
              'g_Anime Series', 'g_Cult Movies', 'g_Docuseries', 'g_Sci-Fi & Fantasy', 'g_TV Sci-Fi & Fantasy',
              'g_Dramas', 'g_Sports Movies', 'g_TV Comedies', 'g_Horror Movies', 'g_Stand-Up Comedy',
              'g_British TV Shows', 'g_Music & Musicals', 'g_TV Action & Adventure', 'g_Spanish-Language TV Shows',
              'g_TV Mysteries', 'g_Reality TV', 'g_TV Shows', 'g_Comedies', 'g_Romantic TV Shows', 'g_Romantic Movies',
              'g_Kids\' TV', 'g_Classic Movies', 'g_International Movies', 'g_Classic & Cult TV',
              'g_Children & Family Movies']
        
            # Processing inputs with the tfidf model
            input_tfidf = my_tfidf.transform([clean_string(my_string)])
            input_transformed_df = pd.DataFrame(input_tfidf.toarray(), columns=my_tfidf.get_feature_names_out())
            input_final = input_transformed_df

            input_final_df = my_scaler.transform(input_final)
            
            # Genre prediction using machine learning models
            input_pred = my_model.predict_proba(input_final_df)
            # Convert predictions to DataFrame and sort them
            df = pd.DataFrame(input_pred, columns=genre_cols).T.sort_values(0, ascending=False)
            # Extract the types and their probabilities for which the predicted probability is greater than or equal to 0.2 and construct the output list
            output_list = []
            for index, row in df.iterrows():
                # Check if the probability is greater than or equal to 0.2 and the category is not in the specified list
                if row.values[0] >= 0.2 and index.capitalize() not in ["G_Movies", "G_dramas", "G_TV Shows", 'G_tv dramas']:
                    temp_list = [int(round(row.values[0]*100, 0)), index.capitalize()]
                    output_list.append(temp_list)
            # 渲染模板并返回结果到前端页面
            return render_template('predict.html', results=output_list, my_string=my_string)
            '''
            for index, row in df.iterrows():
                if row.values[0] >= 0.2:
                    temp_list = [int(round(row.values[0]*100,0)), index.capitalize()]
                    output_list.append(temp_list)
             # 渲染模板并返回结果到前端页面
            return render_template('predict.html', results=output_list, my_string=my_string)
            '''
        
         # 如果是GET请求，显示表单页面
        else:
            return render_template('predict.html')

    except Exception as e:
        # 捕获异常，将错误信息传递给前端页面
        print(e)
        #return json.dumps({'success':True}, 200, {'ContentType':'application/json'})
        return render_template("predict.html", error = e)

if __name__ == "__main__":
    app.debug = True
    app.run()