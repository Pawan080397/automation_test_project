import re

def normalize_location(text: str) -> str:
    """
    Delhi (WTC) -> delhi
    Delhi, NCR  -> delhi
    """
    text = text.lower()
    text = re.sub(r"\(.*?\)", "", text)   # brackets hatao
    text = re.sub(r"[,|-].*", "", text)   # , ya - ke baad hatao
    return text.strip()
