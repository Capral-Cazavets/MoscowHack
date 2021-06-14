from django.shortcuts import render
from django.http import *
import sqlite3
import math
import base64

def index(request):
    print(request.META)
    ''' Код для определения минимального расстояния, после преобразований и получения геоданных пользователя
    if ((request.META['QUERY_STRING'])[:4]=='near'):
        def distance(x1, y1, x2, y2):
            c = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            mas.append
            return c
        j = 0
        mas = []
        while j<n_users(количество пользователей):
            c = distance(x1, y1, x2, y2)
            mas.append(c)
            j+=1
        mas.sort()
        mas1 = []
        while i<5:
            mas1.append(i)
            i+=1
        HttpResponse(mas1)
        '''
    #Демо вариант
    if ((request.META['QUERY_STRING'])[:4]=='near'):
        id_u = ['97219257','97213257','97152257']
        sqlite_connection = sqlite3.connect('./Mitings.sqlite3')
        sqlite_connection1 = sqlite3.connect('./images.sqlite3')
        cursor = sqlite_connection.cursor()
        cursor1 = sqlite_connection1.cursor()
        i1 = 0
        slov1 = []
        while i1<3:
            cursor1.execute("select * from Images where id='"+str(id_u[i1])+ "'")
            b = cursor1.fetchall()[0][2]
            print(f"{b}")
            slov1.append(b)
            i1+=1
        return HttpResponse(slov1)
    if ((request.META['QUERY_STRING'])[:4]=='find'):
        id_u = ['97764257']
        sqlite_connection = sqlite3.connect('./Mitings.sqlite3')
        sqlite_connection1 = sqlite3.connect('./images.sqlite3')
        cursor = sqlite_connection.cursor()
        cursor1 = sqlite_connection1.cursor()
        i1 = 0
        slov2 = []
        while i1<1:
            cursor1.execute("select * from Images where id='"+str(id_u[i1])+ "'")
            b = cursor1.fetchall()[0][2]
            print(f"{b}")
            slov2.append(b)
            i1+=1
        return HttpResponse(slov2)
        #Рекомендация по интересам пользователя временно реализуем рандомом так как нет данных и разделов
    if ((request.META['QUERY_STRING'])[:2]=='id'):
        id_u = ['97764257','97938257','93690257']
        sqlite_connection = sqlite3.connect('./Mitings.sqlite3')
        sqlite_connection1 = sqlite3.connect('./images.sqlite3')
        cursor = sqlite_connection.cursor()
        cursor1 = sqlite_connection1.cursor()
        i1 = 0
        slov3 = []
        while i1<3:
            cursor1.execute("select * from Images where id='"+str(id_u[i1])+ "'")
            b = cursor1.fetchall()[0][2]
            print(f"{b}")
            slov3.append(b)
            i1+=1
        return HttpResponse(slov3) 
    if ((request.META['QUERY_STRING'])[:3]=='pop'):
        id_u = ['98016257','98007257','97981257','97975257','97938257','97933257','97764257','97662257','97628257','97623257']
        sqlite_connection = sqlite3.connect('./Mitings.sqlite3')
        sqlite_connection1 = sqlite3.connect('./images.sqlite3')
        cursor = sqlite_connection.cursor()
        cursor1 = sqlite_connection1.cursor()
        i = 0
        slov = []
        while i<9:
            cursor1.execute("select * from Images where id='"+str(id_u[i])+ "'")
            b = cursor1.fetchall()[0][2]
            print(f"{b}")
            slov.append(b)
            i+=1
        return HttpResponse(slov)
    return JsonResponse('aaaaaaaaaaaaa')
