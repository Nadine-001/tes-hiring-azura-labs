import re
from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors, os

app = Flask(__name__)

conn = cursor = None

#fungsi koneksi database
def openDb() :
   global conn, cursor
   conn = pymysql.connect(db='db_produk', user='root', passwd='', host='localhost', port=3306, autocommit=True)
   cursor = conn.cursor()
   
#fungsi untuk menutup koneksi
def closeDb() :
   global conn, cursor
   cursor.close()
   conn.close()

#fungsi untuk menampilkan data di halaman awal
@app.route('/')
def index() :   
   openDb()
   container = []
   sql = "SELECT * FROM produk"
   cursor.execute(sql)
   results = cursor.fetchall()
   for data in results:
      container.append(data)
   closeDb()
   return render_template('index.html', container=container)

#fungsi untuk menambahkan data
@app.route('/tambah', methods=['GET','POST'])
def tambah() :
   if request.method == 'POST':
      nama = request.form['nama']
      keterangan = request.form['keterangan']
      harga = request.form['harga']
      stok = request.form['stok']
      openDb()
      sql = "INSERT INTO produk (nama_produk, keterangan, harga, stok) VALUES (%s, %s, %s, %s)"
      val = (nama, keterangan, harga, stok)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      return render_template('tambah.html')

#fungsi untuk mengedit data
@app.route('/edit/<id_produk>', methods=['GET','POST'])
def edit(id_produk) :
   openDb()
   cursor.execute('SELECT * FROM produk WHERE id_produk=%s', (id_produk))
   data = cursor.fetchone()
   if request.method == 'POST':
      id_produk = request.form['id_produk']
      nama = request.form['nama']
      keterangan = request.form['keterangan']
      harga = request.form['harga']
      stok = request.form['stok']
      sql = "UPDATE produk SET nama_produk=%s, keterangan=%s, harga=%s, stok=%s WHERE id_produk=%s"
      val = (nama, keterangan, harga, stok, id_produk)
      cursor.execute(sql, val)
      conn.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      closeDb()
      return render_template('edit.html', data=data)

#fungsi untuk melihat detail data
@app.route('/detail/<id_produk>', methods=['GET','POST'])
def detail(id_produk) :
   openDb()
   cursor.execute('SELECT * FROM produk WHERE id_produk=%s', (id_produk))
   data = cursor.fetchone()
   if request.method == 'POST':
      closeDb()
      return redirect(url_for('index'))
   else:
      closeDb()
      return render_template('detail.html', data=data)

#fungsi untuk menghapus data
@app.route('/hapus/<id_produk>', methods=['GET','POST'])
def hapus(id_produk) :
   openDb()
   cursor.execute('DELETE FROM produk WHERE id_produk=%s', (id_produk))
   conn.commit()
   closeDb()
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True)
