from flask_restful import Resource
from flask_jwt_extended import jwt_required
from resources import api
import os

from .rbac import access_for

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from datetime import datetime
import numpy as np

class librarianAnalytics(Resource):
    @jwt_required()
    @access_for(['librarian'])
    def get(self):
        newUsersTimeLine(new_registration_data)
        pie_chart(sections_data)
        section_issud_vs_requ(data1, data2)
        return {'first':'http://127.0.0.1:5000/static/admin_graphs/1.png',
                'second':'http://127.0.0.1:5000/static/admin_graphs/2.png',
                'third':'http://127.0.0.1:5000/static/admin_graphs/3.png'
                }
api.add_resource(librarianAnalytics,'/api/librarian/analytics')

cwd = os.getcwd()

## new registrations vs timeline

def newUsersTimeLine(data_list):
    dates = [datetime.strptime(entry['date'], '%Y-%m-%d') for entry in data_list]
    values = [entry['value'] for entry in data_list]
    plt.figure(figsize=(10, 6))
    plt.plot_date(dates, values, linestyle='-')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xlabel('Date')
    plt.ylabel('No of users')
    plt.title('Time Series Plot')
    plt.gcf().autofmt_xdate()    
    plt.tight_layout()
    img_dest = os.path.join(cwd, 'static','admin_graphs','1.png')
    plt.savefig(img_dest)

new_registration_data = [ # date vs no of new registrations
    {"date": "2024-01-01", "value": 10},
    {"date": "2024-01-02", "value": 15},
    {"date": "2024-01-03", "value": 20},
    {"date": "2024-01-04", "value": 18},
    {"date": "2024-01-05", "value": 25}
    ]

## pie charts of sections as boock count as weight

sections_data = {
    'Art': 25,
    'Programming': 30,
    'AI': 20,
    'Anime': 25
}

def pie_chart(data):
    labels = list(data.keys())
    sizes = list(data.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes,  autopct='%1.1f%%', startangle=90)
    plt.legend(labels, loc="best")
    plt.axis('equal')
    plt.title('Section Distribution')
    img_dest = os.path.join(cwd, 'static','admin_graphs','2.png')
    plt.savefig(img_dest)


data1 = {
    "Art": 10,
    "Programming": 20,
    "AI": 15,
    "Anime": 25
}
data2 = {
    "Art": 15,
    "Programming": 18,
    "AI": 20,
    "Anime": 22
}

def section_issud_vs_requ(data1, data2):
    keys = list(data1.keys())
    values1 = list(data1.values())
    values2 = list(data2.values())
    bar_width = 0.35
    r1 = np.arange(len(values1))
    r2 = [x + bar_width for x in r1]
    plt.figure(figsize=(10, 6))
    plt.bar(r1, values1, color='b', width=bar_width, edgecolor='grey', label='Issue Requests')
    plt.bar(r2, values2, color='r', width=bar_width, edgecolor='grey', label='Book counts')
    plt.xlabel('Keys', fontweight='bold')
    plt.ylabel('Book counts', fontweight='bold')
    plt.xticks([r + bar_width / 2 for r in range(len(values1))], keys)
    plt.title('Comparison of Two Datasets')
    plt.legend()
    img_dest = os.path.join(cwd, 'static','admin_graphs','3.png')
    plt.savefig(img_dest)