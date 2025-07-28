import typer
from .fetcher import search_pubmed, fetch_details
from .exporter import export_to_csv
import rich

app = typer.Typer()


@app.command()
def get(query: str, file: str = None, debug: bool = False):
    if debug:
        rich.print(f"[blue]Searching PubMed for:[/blue] {query}")
    ids = search_pubmed(query)
    if debug:
        rich.print(f"[green]Found {len(ids)} articles[/green]")
    papers = fetch_details(ids)
    if file:
        export_to_csv(papers, file)
        rich.print(f"[bold green]Results saved to {file}[/bold green]")
    else:
        for paper in papers:
            rich.print(paper)


if __name__ == "__main__":
    app()
