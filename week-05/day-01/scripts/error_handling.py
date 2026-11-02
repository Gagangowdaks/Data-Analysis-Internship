from pathlib import Path
from datetime import datetime

ERROR_LOG = Path("week-05/day-01/evidence/failed_queries.log")

def log_failed_query(query, error):
    ERROR_LOG.parent.mkdir(parents=True, exist_ok=True)
    with ERROR_LOG.open("a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now().isoformat(timespec='seconds')}] "
            f"Query: {query}\nError: {error}\n\n"
        )

def run_query(query, operation):
    try:
        result = operation()
        print(f"Query: {query}\nResult: {result}\n")
        return result
    except Exception as error:
        log_failed_query(query, error)
        print(f"Query failed: {query}")
        print(f"Error recorded in: {ERROR_LOG}")
        return None

if __name__ == "__main__":
    run_query(
        "Demonstrate error logging",
        lambda: 10 / 0
    )
