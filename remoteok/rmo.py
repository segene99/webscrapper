# from bs4 import BeautifulSoup
# import requests


# def extract_jobs_remoteok(term):
#     url = f"https://remoteok.com/remote-{term}-jobs"
#     request = requests.get(url, headers={"User-Agent": "Kimchi"})
#     if request.status_code == 200:
#         results = []
#         soup = BeautifulSoup(request.text, "html.parser")

#         job_post = soup.find_all("tr")
#         for job_info in job_post:
#             info = job_info.find_all(
#                 "td", class_="company position company_and_position"
#             )

#             for job in info:
#                 anchor = job.find("a")
#                 if anchor:
#                     link = anchor["href"]
#                     title = anchor.find("h2").string
#                 else:
#                     link = ""
#                     title = ""

#                 comp = job.find("span", class_="companyLink")
#                 if comp:
#                     company_name = comp.find("h3").string
#                 else:
#                     company_name = ""

#                 location = job.find("div", class_="location")
#                 if location:
#                     location = location.string
#                 else:
#                     location = ""

#                 salary = job.find_all("div", class_="location")
#                 if (
#                     salary and len(salary) > 1
#                 ):  # Check if salary data exists and has multiple elements
#                     salary = salary[
#                         -1
#                     ].string.strip()  # Get the last element (salary) and strip any whitespace
#                 else:
#                     salary = ""

#                 job_data = {
#                     "link": f"https://remoteok.com{link}",
#                     "title": title,
#                     "company_name": company_name,
#                     "location": location,
#                     "salary": salary,
#                 }

#                 results.append(job_data)

#         return results

#     else:
#         print("Can't get jobs.")


# job_results = extract_jobs_remoteok("python")
# for job in job_results:
#     print(job)
#     print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")

from bs4 import BeautifulSoup
import requests


def extract_jobs_remoteok(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
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
                    title = anchor.find("h2").string
                    title = title.string.strip()

                else:
                    link = ""
                    title = ""

                comp = job.find("span", class_="companyLink")
                if comp:
                    company_name = comp.find("h3").string
                    company_name = company_name.string.strip()
                else:
                    company_name = ""

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
                    else:
                        datetime_value = None
                else:
                    datetime_value = None

                job_data = {
                    "link": f"https://remoteok.com{link}",
                    "title": title,
                    "company_name": company_name,
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
