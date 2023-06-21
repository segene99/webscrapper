from requests import get
from bs4 import BeautifulSoup
from weworkremotly.wwr import extractor_job
from remoteok.rmo import extract_jobs_remoteok

jobs_wwr = extractor_job("python")


jobs_rmo = extract_jobs_remoteok("python")
