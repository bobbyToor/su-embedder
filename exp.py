from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer("paraphrase-distilroberta-base-v1")
# model = SentenceTransformer("paraphrase-TinyBERT-L6-v2")
# model = SentenceTransformer("bert-base-nli-mean-tokens")
model = SentenceTransformer("paraphrase-mpnet-base-v2")

em1 = model.encode("India")
em2 = model.encode("hsuwau")

print(util.pytorch_cos_sim(em1, em2))
