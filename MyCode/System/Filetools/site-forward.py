"""
################################################################################
Создает страницы со ссылками параедресации на перемещенный веб сайт.
Генерирует по 1 странице для каждого существующего на сайте файла html;
сгенерированный файлы нужно выгрузить на ваш старый веб-сайт. Смотрите описание
ftplib далее в книге, где представлены приемы реализации выгрузки файлов
в сценариях после или в процессе создания файлов страниц.
################################################################################
"""
import os
servername = 'learning-python.com'      # новый адрес сайта
homedir = 'books'                       # корневой каталог сайта
sitefilesdir = r'C:\temp\public_html'   # локальный каталог с файлами сайта
uploaddir = r'C:\temp\isp-firward'      # где сохранять сгенерированные файлы
templatename = 'template.html'          # шаблон для генерируемых страниц

try:
    os.mkdir(uploaddir)     # при необходимости создать каталог для
except OSError: pass        # выгружаемых страниц

template = open(templatename).read()    # загружать и импортировать шаблон
sitefiles = os.listdir(sitefilesdir)    # имена файлов без пути к ним

count = 0
for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = os.path.join(uploaddir, filename)
        print('creating', filename, 'as', fwdname)
        
        filetext = template.replace('$server$', servername)     # вставить текст
        filetext = filetext.replace('$home$', homedir)          # и записать
        filetext = filetext.replace('$file$', filename)         # измененный файл
        open(fwdname, 'w').write(filetext)
        count += 1

print('Last file =>\n', filetext, sep='')
print('Done:', count, 'forward files created.')

