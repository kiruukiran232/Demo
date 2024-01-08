!pip install transformers
from transformers import pipeline,AutoModelForSequenceClassification,AutoTokenizer
model_name="nlptown/bert-base-multilingual-uncased-sentiment"
model=AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer=AutoTokenizer.from_pretrained(model_name)
pipe=pipeline('sentiment-analysis')
text="Chari ist ein gutes Mädchen"
out=pipe(text)
result=out[0] #Assuming you want the first result if multiple are returned
sentiment=result["label"]
score=round(result["score"],2)
print(f"Sentiment: {sentiment}")
print(score)
