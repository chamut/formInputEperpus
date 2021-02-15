import os
from datetime import datetime

import mysql.connector
from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="eperpus_db"
    )

COVER_FOLDER = 'C:/Users/Mutia Salsabila/PycharmProjects/formInputEperpus/Cover/'
FILE_FOLDER = 'C:/Users/Mutia Salsabila/PycharmProjects/formInputEperpus/File/'

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
        kategori = bookDetails['kategori']
        now = datetime.now().time()
        foto = request.files['cover']
        filename = secure_filename(str(now)+foto.filename)
        foto.save(os.path.join(COVER_FOLDER, filename))
        foto = COVER_FOLDER + filename
        file = request.files['filebuku']
        filename = secure_filename(str(now)+file.filename)
        file.save(os.path.join(FILE_FOLDER, filename))
        file = FILE_FOLDER + filename

        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO buku (idbuku, judul_buku, isbn, pengarang, penerbit, tahun_terbit, jumlah_halaman, sinopsis, foto_buku, kategori, file_buku, jumlah_copy, total_dipinjam) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (0, judul, isbn, pengarang, penerbit, int(tahun), int(halaman), sinopsis, foto, kategori, file, int(copy), 0))
        mydb.commit()
        cur.close()
    return render_template('cobauploadya.html')

@app.route("/user", methods=['GET', 'POST'])
def userdata():
    if request.method == 'POST':
        userdata = request.form
        username = userdata['username']
        password = userdata['password']
        nama = userdata['nama']
        fakultas = userdata['fakultas']
        jurusan = userdata['jurusan']
        angkatan = userdata['angkatan']
        status = userdata['status']

        cur = mydb.cursor()
        cur.execute(
            "INSERT INTO user (iduser, username, password, nama_lengkap, fakultas, jurusan, angkatan, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (0, username, password, nama, fakultas, jurusan, int(angkatan), status))
        mydb.commit()
        cur.close()
    return render_template('formUser.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1288, debug=True)