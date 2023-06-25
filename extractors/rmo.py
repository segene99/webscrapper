from bs4 import BeautifulSoup
import requests


def extract_jobs_remoteok(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "genie"})
    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")

        job_post = soup.find_all("tr")
        for job_info in job_post:
            info = job_info.find_all(
                "td", class_="company position company_and_position"
            )

            for job in info:
                anchor = job.find("a")
                if anchor:
                    link = anchor["href"]
                    position = anchor.find("h2").string
                    position = position.string.strip()

                else:
                    link = ""
                    position = ""

                comp = job.find("span", class_="companyLink")
                if comp:
                    company = comp.find("h3").string
                    company = company.string.strip()
                else:
                    company = ""

                location = job.find("div", class_="location")
                if location:
                    location = location.string
                else:
                    location = ""

                salary = job.find_all("div", class_="location")
                if salary and len(salary) > 1:
                    salary = salary[-1].string.strip()
                else:
                    salary = ""

                time_element = job_info.find("td", class_="time")
                if time_element:
                    time = time_element.find("time")
                    if time:
                        datetime_value = time["datetime"]
                        time = datetime_value
                    else:
                        datetime_value = None
                else:
                    datetime_value = None

                job_data = {
                    "link": f"https://remoteok.com{link}",
                    "position": position,
                    "company": company,
                    "location": location,
                    "salary": salary,
                    "time": time,
                }

                results.append(job_data)

        return results

    else:
        print("Can't get jobs.")


job_results = extract_jobs_remoteok("python")
for job in job_results:
    print(job)
    print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")
