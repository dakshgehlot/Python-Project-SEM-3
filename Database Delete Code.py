# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 02:15:52 2021

@author: Daksh
"""
import mysql.connector as mcon
mcon1=mcon.connect(host='localhost',user='root',passwd='69420',database='cs_project')
cursor=mcon1.cursor()
cursor.execute("drop database cs_project")
