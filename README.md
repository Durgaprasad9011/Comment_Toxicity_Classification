
## Detecting Toxic Comments for Better Online Conversations

It classifies comments into various categories such as toxicity, severe toxicity, obscenity, threats, insults, and identity hate based on their respective levels.

It's application is identifying and filtering toxic content in online discussions to promote a safer and more respectful digital environment.

### Dataset Used: 
jigsaw-toxic-comment-classification-challenge

**Link:** https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/overview

### Utilized technologies: 
- *Pandas, Numpy, Tensorflow, Tokenization, Embedding, and employed Deep Learning Models including Bi LSTM and BERT, along with Gradio.*

- *I've shared two Jupyter Notebooks, '**LSTM.ipynb**' and '**BERT.ipynb**', for a detailed exploration of the implementation workflow.*

### My Results:
#### *Bidirectional LSTM Model:*

|   Accuracy  |   Recall   | Precision  |  F1 Score  |
|:-----------:|:----------:|:----------:|:----------:|
|     99.38%     |     92.03%    |     91.00%    |    91.52%   |


#### *BERT Model:*

|   Accuracy  |   Recall   | Precision  |  F1 Score  |
|:-----------:|:----------:|:----------:|:----------:|
|     94.34%     |     95.17%    |     93.49%    |    94.32%   |


### How to Run:

- *I have saved my best model i.e; '**toxicity.h5**' along with the gradio application code '**app.py**'. [ Ensure to update the model path in the '**app.py**' file if the models are located in different directories ].*  
- *Ensure that you have both files available on your system.*
- *Install Gradio and Jinja2 in your terminal using the following commands:*
  
        pip install Jinja2
  
        pip install gradio
- *Make sure to execute these commands to fulfill the necessary dependencies for the application.*
- *After a successful installation, execute the Python code using the following command:*

            python app.py  # If working in the same directory

                                or

            python "the file path of app.py"  # If working in a different directory

- *You can also use python3 based on your terminal's conventions. Ensure to run this command to initiate the application.*
- *which will direct you to open the following interface:*

![Alt Text](https://drive.google.com/uc?id=1wpBcUWJuR8UHNWmG0t11_uopfCoedAzy)

- *Now, you can type a comment and click on "Submit." The output will classify the comment into categories, including toxicity, severe toxicity, obscenity, threats, insults, and identity hate.*



     
