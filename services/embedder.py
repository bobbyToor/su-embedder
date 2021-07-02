from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("paraphrase-distilroberta-base-v1")
# model = SentenceTransformer("paraphrase-TinyBERT-L6-v2")
# model = SentenceTransformer("bert-base-nli-mean-tokens")
model = SentenceTransformer("paraphrase-mpnet-base-v2")


def embedder(input: str):
    return model.encode(input)
