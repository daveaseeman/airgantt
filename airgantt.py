from airtable import airtable
import os
from datetime import timedelta as td
from datetime import datetime as dt
from plotly import plotly, figure_factory
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_URL = 'https://api.airtable.com/v%s/'
API_VERSION = '0'


def set_credentials():
    username = os.environ['USERNAME']
    potly_key = os.environ['PLOTLY_API_KEY']
    plotly.tools.set_credentials_file(username=username,
                                      api_key=potly_key)
    return "credentials set"


def get_base_records(record_table, base_id, airtable_key):
    at = airtable.Airtable(base_id, airtable_key)
    table = at.get(record_table)
    records = table['records']
    return records


def get_projects(record_table, base_id, airtable_key):
    filter_table = 'Projects'
    records = get_base_records(filter_table, base_id, airtable_key)
    projects = []
    for record in records:
        record_name = record['fields']['Name']
        projects.append(record_name)
    return projects


def get_filter_value(filter_key, filter_table, base_id, airtable_key):
    records = get_base_records(filter_table, base_id, airtable_key)
    filter_value = None
    for record in records:
        record_name = record['fields']['Name']
        if record_name == filter_key:
            filter_value = record['id']
    return filter_value


def get_filtered_records(filter_key,
                         filter_table,
                         record_table,
                         base_id,
                         airtable_key):
    filter_value = get_filter_value(filter_key,
                                    filter_table,
                                    base_id,
                                    airtable_key)
    records = get_base_records(record_table, base_id, airtable_key)
    i = 0
    del_records = []
    for record in records:
        fields = record['fields']
        field_filter = fields['Project'][0]
        if field_filter != filter_value:
            del_records.append(i)
            i += 1
            for item in del_records:
                del records[i]
    return records


def get_gantt_tasks(records):
    # Range
    starts = []
    finishes = []
    for record in records:
        if 'Start' in record['fields']:
            start = record['fields']['Start']
            starts.append(dt.strptime(start, "%Y-%m-%d"))
        if 'Finish' in record['fields']:
            finish = record['fields']['Start']
            finishes.append(dt.strptime(finish, "%Y-%m-%d"))
    min_start = min(starts)
    max_finish = max(finishes)
    # Tasks
    tasks = []
    for record in records:
        task = {}
        fields = record['fields']
        task_name = fields['Task Name']
        if 'Start' in fields:
            start = fields['Start']
        else:
            start = min_start.strftime("%Y-%m-%d")
        if 'Finish' in fields:
            finish = fields['Finish']
        else:
            finish = max_finish.strftime("%Y-%m-%d")
        duration = (dt.strptime(finish, "%Y-%m-%d") - dt.strptime(start, "%Y-%m-%d")).days
        assignee = fields['Assignee']['name']
        task['Task'] = task_name
        task['Start'] = start
        task['Finish'] = finish
        task['Index'] = assignee
        task['Duration'] = duration
        tasks.append(task)
    tasks = sorted(tasks, key=lambda k: k['Start'])
    return tasks


def get_index_colors(tasks):
    # http://htmlcolorcodes.com/color-chart/flat-design-color-chart/
    colors = {}
    palatte = [  # 'rgb(235, 237, 239)',
        # 'rgb(214, 219, 223)',
        'rgb(174, 182, 191)',
        # 'rgb(133, 146, 158)',
        # 'rgb(93, 109, 126)',
        'rgb(52, 73, 94)',
        # 'rgb(46, 64, 83)',
        # 'rgb(40, 55, 71)',
        'rgb(33, 47, 60)',
        # 'rgb(27, 38, 49)'
    ]
    index = []
    for task in tasks:
        index_value = task['Index']
        index.append(index_value)
    index = set(index)
    i = 0
    for item in index:
        colors[item] = palatte[i]
        i += 1
    return colors


def get_gantt_url(tasks, filter_key):
    colors = get_index_colors(tasks)
    filename = str(filter_key)
    fig = figure_factory.create_gantt(tasks,
                                      colors=colors,
                                      index_col='Index',
                                      show_colorbar=True,
                                      group_tasks=True)
    plot_url = plotly.plot(fig,
                           filename=filename,
                           auto_open=False)
    return plot_url
