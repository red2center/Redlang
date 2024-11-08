import sys
import os
import re
import requests
import pyinstaller
import requests

def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Herhangi bir hata varsa tetikler
        return response.text
    except requests.exceptions.RequestException as e:
        print("URL'den veri alınırken bir hata oluştu:", e)
        return None

# GitHub'daki raw URL'sini buraya girin










def main(datta):
    
        
    # Komut satırı argümanlarını al
    args = sys.argv[1:]

    # Eğer argüman yoksa dosya ismi sor
##    if not args:
##        file_name = input("Lütfen bir dosya ismi girin: ")
##        args.append(file_name)
##        pyfile = ""
##        redfile = ""
##        url = "https://raw.githubusercontent.com/red2center/redlang/main/comp.py"
##        metin = fetch_text_from_url(url)
##
##        if metin:
##            pyfile = a
##        with open(file_name,"r",encoding='utf-8')as f:
##            a = f.read()
##            redfile = a
##        if len(datta)>1:
##            with open(file_name.replace(".red",".py"),"w",encoding='utf-8')as f:
##                f.write(datta)
##            subprocess.run([sys.executable, "-m", "pyinstaller", "--onefile", file_name.replace(".red",".py")], check=True)
##            os.remove(file_name.replace(".red",".py"))
##        olddata = """
##if __name__ == "__main__":
##    main()
##"""
##        newdata = """
##if __name__ == "__main__":
##    main("""+'"""'+redfile+'"""'+")"
##        
##            
##
##    else:
##        file_name = args[0]

    # Dosyanın varlığını kontrol et
    if not os.path.isfile(file_name):
        print(f"Hata: '{file_name}' dosyası bulunamadı.")
        return

    # Dosyayı utf-8 kodlamasıyla oku ve ilk satırını kontrol et
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # İlk satırda <redlang> olup olmadığını kontrol et
    if lines[0].strip() != "<redlang>":
        print("Hata: Dosya uyumsuz, ilk satırda '<redlang>' bulunmadı.")
        return

    # İlk satır hariç dosyanın geri kalanını işle ve gerekli değişiklikleri yap
    transformed_code = ""
    for line in lines[1:]:  # İlk satırı atla
        # 'eger' ifadesini 'if' ile değiştir
        if line.lstrip().startswith("eger"):
            line = line.replace("eger", "if", 1)

        # 'yaz' ifadesini çift tırnak içinde değilse 'print' ile değiştir
        line = re.sub(r'\byaz\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "print", line)

        # 'gir' ifadesini çift tırnak içinde değilse 'input' ile değiştir
        line = re.sub(r'\bgir\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "input", line)

        # 'degilse' ifadesini çift tırnak içinde değilse 'else' ile değiştir
        line = re.sub(r'\bdegilse\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "else", line)
        line = re.sub(r'\buzunluk\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "len", line)
        line = re.sub(r'\bdongu\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "while", line)
        line = re.sub(r'\bdogru\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "True", line)
        line = re.sub(r'\byanlis\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "False", line)
        line = re.sub(r'\btur \b(?=(?:[^"]*"[^"]*")*[^"]*$)', "for ", line)
        line = re.sub(r'\b içinde \b(?=(?:[^"]*"[^"]*")*[^"]*$)', " in ", line)
        line = re.sub(r'\b say\b(?=(?:[^"]*"[^"]*")*[^"]*$)', " range", line)
        line = re.sub(r'\b ve \b(?=(?:[^"]*"[^"]*")*[^"]*$)', " and ", line)
        line = re.sub(r'\bdurdur\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "break", line)
        line = re.sub(r'\bfonk \b(?=(?:[^"]*"[^"]*")*[^"]*$)', "def ", line)
        line = re.sub(r'\bfonksiyon \b(?=(?:[^"]*"[^"]*")*[^"]*$)', "def ", line)
        line = re.sub(r'\b veya \b(?=(?:[^"]*"[^"]*")*[^"]*$)', " or ", line)
        line = re.sub(r'\bdöndür \b(?=(?:[^"]*"[^"]*")*[^"]*$)', "return ", line)
        line = re.sub(r'\bdene:\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "try:", line)
        line = re.sub(r'\bhata:\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "except:", line)
        line = re.sub(r'\bdevamet\b(?=(?:[^"]*"[^"]*")*[^"]*$)', "continue", line)
        
            # İşlenmiş satırı dönüştürülmüş koda ekle
        transformed_code += line
        

    # Dönüştürülmüş kodu çalıştır
    exec(transformed_code)  # Python kodunu çalıştırır

if __name__ == "__main__":
    main()
