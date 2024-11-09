import subprocess
import sys
import os
import urllib.request
import shutil

def install_python():
    python_installer_url = "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe"
    installer_path = os.path.join(os.getcwd(), "python_installer.exe")
    
    print("Python yükleyici indiriliyor...")
    urllib.request.urlretrieve(python_installer_url, installer_path)
    
    print("Python arka planda yükleniyor...")
    subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], shell=True)
    
    os.remove(installer_path)
    print("Python kuruldu ve yükleyici kaldırıldı.")

def install_pyinstaller():
    print("PyInstaller yükleniyor...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], shell=True)
    print("PyInstaller yüklendi.")

def main():
    # Python yüklü mü kontrol et
    try:
        python_version = subprocess.check_output(["python", "--version"], shell=True).decode()
        print(f"Python zaten yüklü: {python_version}")
    except subprocess.CalledProcessError:
        print("Python yüklü değil, yükleniyor...")
        install_python()

    # PyInstaller yüklü mü kontrol et
    try:
        subprocess.check_output([sys.executable, "-m", "pyinstaller", "--version"], shell=True)
        print("PyInstaller zaten yüklü.")
    except subprocess.CalledProcessError:
        print("PyInstaller yüklü değil, yükleniyor...")
        install_pyinstaller()

    # İlk komut satırı argümanını al ve dosya adına ata
    if len(sys.argv) > 1:
        dosya_adi = sys.argv[1]
        if os.path.isfile(dosya_adi):
            # PyInstaller ile onefile parametresini kullanarak exe oluştur
            print(f"{dosya_adi} dosyası için pyinstaller çalıştırılıyor...")
            subprocess.run([sys.executable, "-m", "pyinstaller", "--onefile", dosya_adi], shell=True)
            print("Çalıştırılabilir dosya oluşturuldu.")
        else:
            print(f"Hata: '{dosya_adi}' dosyası bulunamadı.")
    else:
        print("Hata: Lütfen bir dosya adı belirtin.")

if __name__ == "__main__":
    main()
