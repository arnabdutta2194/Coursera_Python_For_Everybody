import sqlite3
import xml.etree.ElementTree as ET

conn=sqlite3.Connection("sqlex.py")
curr=conn.cursor