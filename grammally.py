from textblob import TextBlob
# a = TextBlob("Mye namee is Pranav , Heello Evryon")
a = TextBlob("Campk12 is a good compny and alays valule ttheir employeees.")
a = a.correct()

print(a)