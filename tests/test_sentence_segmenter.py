import pandas as pd
from segmentation.sentence_segmenter import SentenceUnitizer


def test_basic_sentence_split():
    df = pd.DataFrame(
        {
            "review_id": ["r1"],
            "review_text": ["The oysters were great ! Service was slow."],
        }
    )

    unitizer = SentenceUnitizer()
    out = unitizer.transform(df)

    print(out)

    assert len(out) == 2
    assert out.iloc[0]["sentence_text"] == "The oysters were great !"
    assert out.iloc[1]["sentence_text"] == "Service was slow."


if __name__ == "__main__":
    test_basic_sentence_split()    
    print("All tests passed.")   