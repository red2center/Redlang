import sys
import os
import re
import requests
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
    
    transformed_code = ""
    # Komut satırı argümanlarını al
    args = sys.argv[1:]

    # Eğer argüman yoksa dosya ismi sor
    if not args:
        
        args.append(datta)
        
    else:
        file_name = args[0]

    # Dosyanın varlığını kontrol et
        if os.path.isfile(file_name) and args[0] == 0 :
            
            

            # Dosyayı utf-8 kodlamasıyla oku ve ilk satırını kontrol et
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # İlk satırda <redlang> olup olmadığını kontrol et
            if lines[0].strip() != "<redlang>":
                print("Hata: Dosya uyumsuz, ilk satırda '<redlang>' bulunmadı.")
                return

            # İlk satır hariç dosyanın geri kalanını işle ve gerekli değişiklikleri yap
            
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
    if args[0] != 0:
        if args[0].strip() == "<redlang>":
            transformed_code = datta
    # Dönüştürülmüş kodu çalıştır
    exec(transformed_code)  # Python kodunu çalıştırır

if __name__ == "__main__":
    main(0)
