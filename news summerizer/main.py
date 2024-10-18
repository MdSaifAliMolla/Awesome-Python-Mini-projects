import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt_tab')

def summarize():
    url = utext.get("1.0","end").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publish.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0","end")
    author.delete("1.0","end")
    publish.delete("1.0","end")
    summary.delete("1.0","end")

    title.insert("1.0",article.title)
    author.insert("1.0",article.authors)
    publish.insert("1.0",article.publish_date)
    summary.insert("1.0",article.summary)

    title.config(state="disabled")
    author.config(state="disabled")
    publish.config(state="disabled")
    summary.config(state="disabled")

    text = article.text
    analysis = TextBlob(text)
    sen=(f"Sentiment : {'positive'if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'} with confidence of {analysis.sentiment.polarity}")
    sentiment.delete("1.0","end")
    sentiment.insert("1.0",sen)
    sentiment.config(state="disabled")


root = tk.Tk()
root.title("News Summarizer")
root.geometry("900x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()
title=tk.Text(root, height=1, width=100)
title.config(state="disabled",bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()
author=tk.Text(root, height=1, width=100)
author.config(state="disabled",bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication date")
plabel.pack()    
publish=tk.Text(root, height=1, width=100)
publish.config(state="disabled",bg="#dddddd")
publish.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()
summary=tk.Text(root, height=17, width=100)
summary.config(state="disabled",bg="#dddddd")
summary.pack()

snlabel = tk.Label(root, text="Sentiment Analysis")
snlabel.pack()
sentiment=tk.Text(root, height=1, width=100)
sentiment.config(state="disabled",bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()
utext=tk.Text(root, height=1, width=100)
utext.pack()

button=tk.Button(root, text="Summarize", command=summarize)
button.pack()    

root.mainloop()