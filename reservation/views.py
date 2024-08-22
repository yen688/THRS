from django.shortcuts import render
import sqlite3
from .models import Reserve
import datetime


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

def confirmForm(request):
    date = request.GET.get('date')
    level = request.GET.get('level')
    return render(request, 'reservation/confirmForm.html',{'date':date, 'level':level})

def bookingList(request):
    if request.method == 'POST':
        level = request.POST.get('menu')
        date = request.POST.get('date')

        date = date.split('-')
        date = date[2]+'-'+date[1]+'-'+date[0]

        bookinglists = Reserve.objects.filter(level=level, date=date)
    # 傳送資料到bookingList.html
    return render(request, 'reservation/bookingList.html',{'bookinglists': bookinglists, 'date':date, 'level':level})

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
