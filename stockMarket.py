#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Kütüphaneler
import matplotlib.pyplot as plt
import urllib2
import json
import numpy

# Verileri Çekiyoruz
contents = urllib2.urlopen("https://www.doviz.com/api/v1/stocks/all/latest").read()
data = json.loads(contents)

# İslem Seçiyoruz
islem = input("Yapmak İstediğiniz İşlemi Seçiniz (1)Grafik çizer (2)Gün içi verilerini görüntüler: ")

# Veri Alıyoruz
hisse = raw_input("Hisse Adı Giriniz: ")

if islem == 1:
    for i in range(len(data)):
        if hisse.upper() == data[i]["ticker"]:
            plt.plot([data[i]["latest"],data[i]["lowest"],data[i]["highest"]])
            plt.show()

elif islem == 2:
    for i in range(len(data)):
        if hisse.upper() == data[i]["ticker"]:
            print data[i]["full_name"]
            print "Günsonu: ",data[i]["latest"]
            print "Gün İçi En Yüksek: ",data[i]["highest"]
            print "Gün İçi En Düşük: ",data[i]["lowest"]
