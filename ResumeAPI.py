from flask import Flask, request, jsonify
import indeedScraper
from pprint import pprint
from time import gmtime, strftime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(indeedScraper.get_num_resumes(24,"Dallas,TX"))

@app.route('/resumes',methods=['GET'])
def numresumes():
    data = request.args
   
    job_type = int(data['job_type'])
    location = data['location']
    num_resumes = indeedScraper.get_num_resumes(job_type,location)
    scrapedate = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    response = {'job_type' : job_type, 'location': location, 'num_resumes': num_resumes, 'scrape_date' : scrapedate }
    return jsonify(location=location,
                   job_type=job_type,
                   num_resumes=num_resumes,
                   scrape_date=scrapedate)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)