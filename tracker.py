import requests
import pandas as pd

URL = "https://remotive.com/api/remote-jobs?search=java"

response = requests.get(URL)
data = response.json()

jobs = data.get("jobs", [])

filtered = []

for job in jobs:
    title = job.get("title", "")
    company = job.get("company_name", "")
    location = job.get("candidate_required_location", "")
    url = job.get("url", "")

    keywords = [
        "sdet",
        "java",
        "selenium",
        "api testing",
        "rest assured",
        "testng",
        "automation engineer",
        "qa engineer",
        "quality engineer",
        "cucumber",
        "postman"
    ]

    text = (title + company).lower()

    if any(k in text for k in keywords):
        filtered.append({
            "title": title,
            "company": company,
            "location": location,
            "link": url
        })
df = pd.DataFrame(filtered)

print("\n=== SDET JOBS FOUND ===\n")
print(df)

df.to_csv("jobs.csv", index=False)
print("\nSaved to jobs.csv")