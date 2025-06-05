from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    f = open("data_bite.json", "r")
    data = json.load(f)
    f.close()

    years = sorted([int(y) for y in data["Bronx"].keys()])

    return render_template("about.html", years=years)
@app.route('/macro')
def macro():
    f = open("data_bite.json", "r")
    data = json.load(f)
    f.close()
    bronx_endpoints = []
    brooklyn_endpoints = []
    manhattan_endpoints = []
    queens_endpoints = []
    staten_island_endpoints = []
    universal_endpoints = []

    years = sorted([int(y) for y in data["Bronx"].keys()])

    for i in range(len(years) - 1):
        year1 = str(years[i])
        year2 = str(years[i + 1])

        bx_y1 = float(data["Bronx"][year1])
        bx_y2 = float(data["Bronx"][year2])
        bronx_endpoints.append([bx_y1, bx_y2])

        bk_y1 = float(data["Brooklyn"][year1])
        bk_y2 = float(data["Brooklyn"][year2])
        brooklyn_endpoints.append([bk_y1, bk_y2])

        m_y1 = float(data["Manhattan"][year1])
        m_y2 = float(data["Manhattan"][year2])
        manhattan_endpoints.append([m_y1, m_y2])

        q_y1 = float(data["Queens"][year1])
        q_y2 = float(data["Queens"][year2])
        queens_endpoints.append([q_y1, q_y2])

        si_y1 = float(data["Staten Island"][year1])
        si_y2 = float(data["Staten Island"][year2])
        staten_island_endpoints.append([si_y1, si_y2])
        
        universal_y1 = (bx_y1+ bk_y1 + m_y1 + q_y1 + si_y1)/5
        universal_y2 = (bx_y2+ bk_y2 + m_y2 + q_y2 + si_y2)/5
        universal_endpoints.append([universal_y1,universal_y2])


    return render_template(
    "macro.html",
    bronx_endpoints=bronx_endpoints,
    brooklyn_endpoints=brooklyn_endpoints,
    manhattan_endpoints=manhattan_endpoints,
    queens_endpoints = queens_endpoints,
    staten_island_endpoints = staten_island_endpoints,
    universal_endpoints = universal_endpoints,
    years=years
    )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/micro')
def year():
    f = open("data_bite.json", "r")
    data = json.load(f)
    f.close()

    year = request.args.get("year")

    bx_value = float(data["Bronx"][str(year)])
    bk_value = float(data["Brooklyn"][str(year)])
    m_value = float(data["Manhattan"][str(year)])
    q_value = float(data["Queens"][str(year)])
    si_value = float(data["Staten Island"][str(year)])

    universal_value = (bx_value + bk_value + m_value + q_value + si_value) / 5

    # Calculate distance from average
    delta_bx = round(bx_value - universal_value, 2)
    delta_bk = round(bk_value - universal_value, 2)
    delta_m = round(m_value - universal_value, 2)
    delta_q = round(q_value - universal_value, 2)
    delta_si = round(si_value - universal_value, 2)
    return render_template("micro.html",
        year=year,
        bk_value=bk_value,
        bx_value=bx_value,
        m_value=m_value,
        q_value=q_value,
        si_value=si_value,
        universal_value=round(universal_value, 2),
        delta_bx=delta_bx,
        delta_bk=delta_bk,
        delta_m=delta_m,
        delta_q=delta_q,
        delta_si=delta_si)
        
        
    

if __name__ == "__main__":
    app.run(debug=True)
