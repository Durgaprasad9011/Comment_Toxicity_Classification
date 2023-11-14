import gradio as gr
import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers import TextVectorization
import os

MAX_FEATURES = 200000  # number of words in the vocab
vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')

# Load the pre-trained model
model = tf.keras.models.load_model("C:\\Users\\Sunke Durgaprasad\\Desktop\\ED\\SEM-V\\Machine Learning project\\Deploy\\toxicity.h5")

# Define your DataFrame (df) with appropriate columns
#train_path = os.path.join("/content/drive/MyDrive/jigsaw-toxic-comment-classification-challenge", 'train.csv','train.csv')
df = pd.read_csv("C:\\Users\\Sunke Durgaprasad\\Desktop\\ED\\SEM-V\\Machine Learning project\\jigsaw-toxic-comment-classification-challenge\\train.csv\\train.csv")

# Adapt the TextVectorization layer with training data
train_comments = df['comment_text'].values  # Assuming the comments are in a column named 'comment_text'
vectorizer.adapt(train_comments)

def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)

    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{}: {}\n'.format(col, results[0][idx] > 0.5)

    return text

demo = gr.Interface(
    fn=score_comment,
    inputs=gr.Textbox(lines=2, placeholder='Comment to score'),
    outputs="text"
)
demo.launch(share=True, debug=True)