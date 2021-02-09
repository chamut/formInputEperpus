from urllib import request

import mysql.connector

class Todatabase:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="eperpus_db"
    )

    def kirimkedb(self, data):
        # INSERT INTO `buku` (`idbuku`, `judul_buku`, `isbn`, `pengarang`, `penerbit`, `tahun_terbit`, `jumlah_halaman`, `sinopsis`, `foto_buku`, `kategori`, `file_buku`, `jumlah_copy`, `total_dipinjam`) VALUES (NULL, 'cacZCX', '1234567', 'df,,mjnhgbfdsa', 'ASDFVGHJFDS', '2111', '300', 'DVVVSDV\r\nF\r\nF\r\n\r\nD\r\nG\r\nF\r\nH\r\nGF\r\nJ\r\nH\r\nJ\r\nHG', 'sdfghjklkjhgfdsa', 'assdhfjdfddh', 'dsdfghjhkjhgfdsdfghjk', '1', '0');
        if request.method == 'POST':
            bookDetails = request.form
            judul = bookDetails['judul']
            isbn = bookDetails['isbn']
            pengarang = bookDetails['pengarang']
            penerbit = bookDetails['penerbit']
            tahun = bookDetails['tahun']
            halaman = bookDetails['halaman']
            copy = bookDetails['jumlahcopy']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (judul_buku, isbn, pengarang, penerbit, tahun_terbit, jumlah_halaman, foto_buku, file_buku, jumlah_copy) VALUES (%s, %s, %s, %s, %d, %d, %s, %s, %d)", (judul, isbn, pengarang, penerbit, int(tahun), int(halaman), 'gfdhjska', 'hshajhjs', int(copy)))
            mysql.connection.commit()
        return render_template('booksform.html')