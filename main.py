from flask import Flask, render_template, request, redirect, send_file
from extractors.rmo import extract_jobs_remoteok
from extractors.wwr import extract_jobs_weworkremotely
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html", name="segene") #templates 폴더안의 파일을 출력. 폴더이름은 무조건 templates여야 함
    #name은 변수를 보내서 html에 {{name}}에 segene이 들어감

@app.route("/search") #경로 설정 http://localhost:3090/search
def search():
    keyword = request.args.get("keyword") #get방식으로 keyword라는 key값 파라미터 받음
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
            rmo = extract_jobs_remoteok(keyword)
            wwr = extract_jobs_weworkremotely(keyword)
            if rmo is None:
                rmo = []  # Assign an empty list if rmo is None
            if wwr is None:
                wwr = []  # Assign an empty list if wwr is None
            jobs = rmo + wwr
            db[keyword] = jobs
    
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
     keyword = request.args.get("keyword") #get방식으로 keyword라는 key값 파라미터 받음
     if keyword == None:
        return redirect("/")
     if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
     
     save_to_file(keyword, db[keyword])
     return send_file(f"{keyword}.csv", as_attachment=True)

app.run(host="0.0.0.0", port=3090)