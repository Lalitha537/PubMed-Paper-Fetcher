from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from .filters import is_non_academic, extract_email

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, retmax: int = 20) -> List[str]:
    url = f"{BASE_URL}esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data['esearchresult']['idlist']

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    url = f"{BASE_URL}efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(pubmed_ids), "retmode": "xml"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "xml")
    papers = []

    for article in soup.find_all("PubmedArticle"):
        pmid = article.PMID.text
        title = article.Article.ArticleTitle.text
        pub_date = article.Article.Journal.JournalIssue.PubDate
        pub_date_str = " ".join([x.text for x in pub_date.find_all()])

        authors = article.find_all("Author")
        non_acad_authors, companies, email = [], [], None

        for author in authors:
            aff_info = author.find("AffiliationInfo")
            if aff_info and aff_info.Affiliation:
                aff_text = aff_info.Affiliation.text
                if is_non_academic(aff_text):
                    full_name = f"{author.ForeName.text if author.ForeName else ''} {author.LastName.text if author.LastName else ''}".strip()
                    non_acad_authors.append(full_name)
                    companies.append(aff_text)
                    if '@' in aff_text and not email:
                        email = extract_email(aff_text)

        if non_acad_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date_str,
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email or "N/A"
            })

    return papers
