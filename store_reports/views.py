from django.shortcuts import render

# Create your views here.
from store_management_systems.settings import connection


class Report_1:
    conn = connection.cursor()
