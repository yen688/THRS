from django.shortcuts import render
import sqlite3
import json
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'reservation/index.html')

def rule(request):
    return render(request, 'reservation/rule.html')

def inquire(request):
    return render(request, 'reservation/inquireForm.html')
    
def inquireList(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        # 連接資料庫
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # 查詢phpne reserve資料表
        cursor.execute('SELECT * FROM Reserve where phone=?', (phone,))
        # 取得所有資料
        results = cursor.fetchall()  
        cursor.close()
        conn.close()
        return render(request, 'reservation/inquireList.html',{'results': results}) 
      
def cancelSucess(request):
    if request.method == 'POST':
        cancel = request.POST.get('cancel')
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Reserve WHERE ID=?', (cancel,))
        conn.commit()
        cursor.close()
        conn.close()
    return render(request, 'reservation/cancelSucess.html')

def mail(request):
    return render(request, 'reservation/mail.html')

def calendar(request):
    return render(request, 'reservation/calendar.html')

def confirmForm(request,date):
    return render(request, 'reservation/confirmForm.html',{'date':date})

def bookingList(request):
    name = []
    level = []
    time = []
    # 連接資料庫
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # 查詢reserve資料表
    cursor.execute('SELECT * FROM Reserve')
    # 取得所有資料
    data = cursor.fetchall()

    for i in range(0,len(data)):
        name.append(data[i][1])
        level.append(data[i][5])
        time.append(data[i][4])

    # 關閉資料庫連線
    cursor.close()
    conn.close()

    combined = zip(name, level, time)

    # 傳送資料到bookingList.html
    return render(request, 'reservation/bookingList.html',{'context':combined})

def confirm(request):
    if request.method == 'POST':
        name = request.POST.get('customer')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        level = request.POST.get('level')
    
    # 連接資料庫
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # 新增資料到reserve資料表
    cursor.execute('INSERT INTO Reserve(name,phone,date,time,level) VALUES(?,?,?,?,?)',(name,phone,date,time,level))
    conn.commit()

    # 關閉資料庫連線
    cursor.close()
    conn.close()

    return render(request, 'reservation/index.html')
