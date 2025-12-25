import pandas as pd
import spacy


class SentenceUnitizer:
    """
    Sentence-level unitization of review text.
    """

    def __init__(
        self,
        text_col: str = "review_text",
        id_col: str = "review_id",
    ):
        self.text_col = text_col
        self.id_col = id_col
        self._nlp = spacy.load("en_core_web_sm", disable=["ner", "tagger"])

    def transform(self, reviews: pd.DataFrame) -> pd.DataFrame:
        records = []

        if self.text_col not in reviews or self.id_col not in reviews:
            raise ValueError("Required columns missing")

        for _, row in reviews.iterrows():
            review_id = row[self.id_col]
            text = row[self.text_col]

            doc = self._nlp(text)

            for i, sent in enumerate(doc.sents):
                sent_text = sent.text.strip()
                if sent_text:
                    records.append(
                        {
                            "review_id": review_id,
                            "sentence_id": f"{review_id}_{i}",
                            "sentence_text": sent_text,
                        }
                    )

        return pd.DataFrame(records)
