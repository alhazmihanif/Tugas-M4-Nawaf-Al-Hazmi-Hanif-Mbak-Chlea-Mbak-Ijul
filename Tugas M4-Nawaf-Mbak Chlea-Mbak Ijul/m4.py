#no 1
print('soal no 1')
geprek=['geprek gepruk', 10000, 10.15, True]
print(geprek)
bakso=['arsi', 15000, 15.25, True]
print(bakso)
nasgor=['cak bowo', 27000, 20.35, False]
print(nasgor)
esteh=['poci', 5000, 5.25, False]
print(esteh)
#no 2
print('soal no 2')
huruf=['A', 'B', 'C', 'D', 'E']
print(huruf[2])
print(huruf[1:4])
#no 3
print('soal no 3')
warna=['merah','hijau','biru']
warna[1]='kuning'
print(warna)
#no 4
print('soal no 4')
mata_kuliah = []
mata_kuliah.append('maen maen')
mata_kuliah.append('maen aja')
mata_kuliah.append('bukan maen')
print(mata_kuliah)
#no 5
print('soal no 5')
tugas = ['Matematika', 'Fisika Terapan', 'Peluang Terapan', 'Kimia Terapan']
tugas.remove('Fisika Terapan')
tugas.pop()
print(tugas)
#no 6
print('soal no 6')
angka_acak = [3, 1, 4, 1, 5, 9, 2, 6, 5]
angka_acak.sort(reverse=True)
print(angka_acak)
print('Jumlah kemunculan angka 5:', angka_acak.count(5))
print('Jumlah semua angka:', sum(angka_acak))
#no 7
print('soal no 7')
data_antrean = ['Najwa', 'Budi', 'Tsalits', 'Ibnu', 'Jojo', 'Chlea']
data_antrean.append('Fikri')
data_antrean.remove('Najwa')
data_antrean.remove('Budi')
data_antrean.insert(0, 'Budi')
print(data_antrean)
print(len(data_antrean))
#no 8
print('soal no 8')
nilai_pelter = [75, 80, 60, 95, 80, 85, 65, 100, 80]
print('Jumlah kemunculan nilai 80:', nilai_pelter.count(80))
nilai_pelter.sort(reverse=True)
print('Nilai setelah diurutkan:', nilai_pelter)
print('Tiga nilai tertinggi:', nilai_pelter[:3])