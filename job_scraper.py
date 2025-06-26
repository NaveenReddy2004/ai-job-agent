import os
import requests

def scrape_jobs(query, num_results=5):
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        print("❌ SERPAPI_KEY not found in environment.")
        return []

    params = {
        "engine": "google_jobs",
        "q": query,
        "api_key": api_key,
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    results = data.get("jobs_results", [])

    jobs = []
    for result in results[:num_results]:
        jobs.append({
            "Job Title": result.get("title"),
            "Company": result.get("company_name"),
            "Job Link": result.get("related_links", [{}])[0].get("link", "#"),
        })

    return jobs
