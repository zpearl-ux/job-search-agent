from rich import print
from agents.search_agent import SearchAgent


def main():

    print("[bold green]🤖 Job Search Agent[/bold green]")

    agent = SearchAgent()

    jobs = agent.search(
        keyword="Business Analyst",
        location="Sydney"
    )

    print(jobs)


if __name__ == "__main__":
    main()