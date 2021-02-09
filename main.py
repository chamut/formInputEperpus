import os

import mysql.connector
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="eperpus_db"
    )

@app.route("/", methods=['GET', 'POST'])
def buku():
    if request.method == 'POST':
        bookDetails = request.form
        judul = bookDetails['judul']
        isbn = bookDetails['isbn']
        pengarang = bookDetails['pengarang']
        penerbit = bookDetails['penerbit']
        tahun = bookDetails['tahun']
        halaman = bookDetails['halaman']
        sinopsis = bookDetails['sinopsis']
        copy = bookDetails['jumlahcopy']

        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO buku (idbuku, judul_buku, isbn, pengarang, penerbit, tahun_terbit, jumlah_halaman, sinopsis, foto_buku, kategori, file_buku, jumlah_copy, total_dipinjam) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (0, judul, isbn, pengarang, penerbit, int(tahun), int(halaman), sinopsis, foto, 'gfdhjska', 'hshajhjs', int(copy), 0))
        mydb.commit()
    return render_template('booksform.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1288, debug=True)