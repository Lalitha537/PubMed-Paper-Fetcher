
# 🧪 PubMed Paper Fetcher

A Python command-line tool to fetch research papers from PubMed based on a query, and identify authors affiliated with pharmaceutical or biotech companies. Results are saved to a CSV file with detailed metadata.

---

## 📦 Features

- Search PubMed using flexible query syntax
- Detect non-academic authors (pharma/biotech companies)
- Save results to a CSV with rich metadata:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email
- Command-line interface with options for help, debug mode, and custom output file

---

## 🧪 Example

```bash
poetry run python -m pubmed_paper_fetcher.cli "machine learning cancer" --file resul.csv --debug
```

---

## 🖥 Output Format

The generated CSV file will contain the following columns:

| PubMed ID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|-------|------------------|-------------------------|-------------------------|-----------------------------|

---

## 🧰 Tools & Dependencies

| Tool | Purpose |
|------|---------|
| [Poetry](https://python-poetry.org/) | Dependency management & packaging |
| [Requests](https://docs.python-requests.org/en/latest/) | HTTP client for PubMed API |
| [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) | XML parsing |
| [PubMed API (Entrez)](https://www.ncbi.nlm.nih.gov/books/NBK25501/) | Data source for research papers |

---

## 🚀 Installation Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher

# Install dependencies
poetry install
```

---

## 🏃‍♂️ How to Run

```bash
# Basic command (prints to console)
poetry run get-papers-list "cancer biomarkers"

# Save to file
poetry run get-papers-list "machine learning cancer" --file results.csv

# Enable debug logs
poetry run get-papers-list "genomics AI" --file output.csv --debug
```

---

## ⚙️ CLI Options

| Flag | Description |
|------|-------------|
| `-h`, `--help` | Show help message and usage |
| `-f`, `--file` | Output file name (CSV) |
| `-d`, `--debug` | Enable debug logging |

---

## 🧩 Project Structure

```
pubmed-paper-fetcher/
├── src/
│   └── pubmed_paper_fetcher/
│       ├── __init__.py
│       ├── core.py        # Contains core logic to fetch and parse results
│       ├── utils.py       # Utility functions like email extraction, filtering
│       └── cli.py         # CLI entry point using argparse
├── tests/
│   └── test_core.py       # Unit tests
├── pyproject.toml         # Poetry project config
└── README.md              # Project documentation
```

---

## ✅ Functional Requirements (Covered)

- ✅ Fetch papers from PubMed using user-specified query
- ✅ Support full query syntax
- ✅ Identify and list non-academic authors
- ✅ Save all required metadata to CSV
- ✅ Works via command-line with options
- ✅ Uses typed Python (`mypy` compatible)

---

## 💡 Heuristics to Identify Non-Academic Authors

- Company-like keywords in affiliation (e.g., "Pharma", "Biotech", "Inc.", "Ltd.", "Corporation")
- Excludes academic keywords like "University", "Institute", "College", "School"
- Optionally checks emails for company domains (e.g., `@pfizer.com`)

---

## 📦 Publishing (Bonus Points)

If you'd like to publish to **TestPyPI**, follow these steps:

```bash
# Build the package
poetry build

# Publish to TestPyPI
poetry publish --repository testpypi
```

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 📣 Author

Developed by Sri Lalitha  
GitHub: https://github.com/Lalitha537/fetch-research-papers-using-user-specified-query.git

---

## 🧠 Acknowledgements

- NCBI PubMed API (Entrez)
- Poetry Python packaging
- Large Language Model tools for assistance
