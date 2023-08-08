from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from sql_integration.settings import *
import pandas as pd, sqlalchemy as sa
from django.db import connection

engine = sa.create_engine('postgresql://postgres:5773@localhost:5432/chioma')
# from .forms import DatabaseConnectionForm
from .models import DataEntry
# Create your views here.


# def dynamic_data_display(request):
#     query = request.GET.get('query','')
#     data_entries = DataEntry.objects.filter(content__icontains=query)

#     context  = {
#         'query' : query,
#         'entries': data_entries

#     }
#     return render(request,'query_result.html',context)

def execute_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result_df = pd.DataFrame(rows, columns=columns)
        return result_df.to_html()
        # df = pd.read_sql(query, engine)
        # return df.to_html()

def home(request):
    if request.method == "POST":
        sql_statement = request.POST['sql_statement']
        query = DataEntry(sql_statement=sql_statement)
        query.save()
        result_html = execute_query(sql_statement)
        context = {'html': result_html}
        return render(request, "query_result.html", context)
    return render(request,"query_result.html")