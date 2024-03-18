# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    data, columns = [], []
    columns = get_columns()
    cs_data = get_cs_data(filters)

    if not cs_data:
        frappe.msgprint(_('No records found'))
        return columns, data

    data = []
    for d in cs_data:
        row = frappe._dict({
            'first_name': d.get('first_name'),
            'dob': d.get('dob'),
            'age': d.get('age'),
        })
        data.append(row)
    chart=get_chart_data(data)
    report_summary=get_report_summary(data)
    return columns, data,None,chart,report_summary

def get_columns():
    return [
        {
            "label": _("Name"),
            "fieldtype": "Data",
            "fieldname": "first_name",
            "width": 120,
        },
        {
            "label": _("DOB"),
            "fieldtype": "Date",
            "fieldname": "dob",
            # "hidden": 1,
            "width": 100,
        },
        {
            "label": _("Age"),
            "fieldtype": "Data",
            "fieldname": "age",
            "width": 100,
        },
    ]

def get_conditions(filters):
    conditions = {}

    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value

    return conditions

def get_cs_data(filters):
    conditions = get_conditions(filters)
    data = frappe.get_all(
        doctype='Server Side Scripting',
        fields=['first_name', 'age', 'dob'],
        filters=conditions,
        order_by='first_name desc'
    )

    return data

def get_chart_data(data):
    if not data:
        return None

    labels = ['Age <= 45', 'Age > 45']
    age_data = {'Age>45': 0, 'Age<=45': 0}
    
    for entry in data:
        if entry.age is not None:
            if entry.age <= 45:
                age_data['Age<=45'] += 1  # Corrected key here
            else:
                age_data['Age>45'] += 1

    datasets = [{
        'name': 'Age Status',
        'values': [age_data.get('Age<=45'), age_data.get('Age>45')]  # Corrected key here
    }]

    chart = {
        'data': {
            'labels': labels,
            'datasets': datasets
        },
        # 'type': 'pie',
        # 'type': 'line',
        'type': 'bar',
        'height': 300
    }

    return chart



def get_report_summary(data):
    if not data:
        return None

    age_below_45,age_above_45=0,0
    
    for entry in data:
        if entry.age is not None:
            if entry.age <= 45:
                age_below_45 += 1  
            else:
                age_above_45 += 1

    return  [
        {
        'value':age_below_45,
        'indicator':'Green',
        'label':'Age Below 45',
        'datatype': 'Int',
        },

        {
        'value':age_above_45,
        'indicator':'Red',
        'label':'Age Above 45',
        'datatype': 'Int',
        },

        ]