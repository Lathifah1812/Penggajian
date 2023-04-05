Ini adalah program Python yang menghitung gaji karyawan berdasarkan faktor-faktor seperti gaji dasar, grade, jumlah anak, dan status pernikahan. 

## Cara Menggunakan Program

1. Jalankan program pada komputer dengan Python terinstal.
2. Masukkan nama karyawan, gaji, grade, jumlah anak, dan status pernikahan saat diminta oleh program.
3. Program akan menghitung total gaji karyawan dengan faktor allowance grade, allowance children, allowance spouse, dan potongan pajak. Total gaji yang dihitung juga dapat disesuaikan dengan bonus khusus untuk grade dan jumlah anak tertentu.
4. Total gaji karyawan akan dicetak pada layar.

Catatan: Informasi masukan harus sesuai dengan kriteria data yang diminta.

## Dokumentasi Kode

``` python
class Employee:
    def __init__(self, name: str, salary: int, grade: int, num_children: int, married: bool):
        self.name = name
        self.salary = salary
        self.grade = grade
        self.num_children = num_children
        self.married = married
    
    def get_grade_allowance(self, grade: int) -> float:
        # mendapatkan allowance berdasarkan grade karyawan
        ...
    
    def get_children_allowance(self, num_children: int) -> float:
        # mendapatkan allowance berdasarkan jumlah anak karyawan
        ...
        
    def get_spouse_allowance(self, married: bool) -> float:
        # mendapatkan allowance berdasarkan status pernikahan karyawan
        ...
        
    def get_salary(self) -> float:
        # menghitung gaji karyawan
        ...
        
# meminta masukan dari pengguna
name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))
grade = int(input("Enter employee grade (1-4): "))
num_children = int(input("Enter number of employee's children: "))
married = input("Is employee married (yes/no): ").lower() == "yes"

# inisialisasi objek karyawan dan perhitungan gaji
emp = Employee(name, salary, grade, num_children, married)
salary = emp.get_salary()

# menampilkan hasil gaji karyawan
print(f"{emp.name} has a salary of {salary}")
```
