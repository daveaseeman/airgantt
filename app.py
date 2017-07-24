import os
from flask import Flask, render_template, request
from airgantt import get_filtered_records, get_projects  # get_base_records
from airgantt import get_gantt_tasks  # get_gantt_url
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

base_id = os.environ['BASE_ID']
airtable_key = os.environ['AIRTABLE_API_KEY']

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    # records = None
    # tasks = None
    # gantt_url = None
    # Set Filter Params
    # filter_key = request.values.get('filter-key')
    # filter_table = request.values.get('filter-table')
    # Set Record Params
    # record_table = request.values.get('record-table')
    # if filter_table and filter_key:
        # records = get_filtered_records(filter_key,
        #                                filter_table,
        #                                record_table,
        #                                base_id,
        #                                airtable_key)
        # tasks = get_gantt_tasks(records)
        # gantt_url = get_gantt_url(tasks, filter_key)
        # gantt_url=gantt_url, filter_key=filter_key
    return render_template('index.html')


@app.route("/new")
def new():
    record_table = 'Projects'
    project_list = get_projects(record_table, base_id, airtable_key)
    return render_template('new.html', project_list=project_list)


@app.route("/gantt", methods=['POST'])
def gantt():
    filter_key = request.form.get('project_select')
    project = filter_key
    record_table = 'Tasks'
    filter_table = 'Projects'
    records = get_filtered_records(filter_key,
                                   filter_table,
                                   record_table,
                                   base_id,
                                   airtable_key)
    tasks = get_gantt_tasks(records)
    return render_template('gantt.html', tasks=tasks, project=project)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
