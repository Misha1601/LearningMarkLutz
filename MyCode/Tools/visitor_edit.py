"""
################################################################################
Порядок использования: "python ...\Tools\visitor_edit.py string rootdir?".
Добавляет подкласс класса SearchVisitor, который автоматически запускает
текстовый редактор. В процессе обхода автоматичесмки открывает в текстовом
редакторе файлы, содержащие искомую строку; в Windows можно так же использовать
editor='edit' или 'notepad'; чтобы воспользоватьлся текстовым редактором,
реализация которого будет представлена далее в книге, попробуйте r'python Gui\
TextEditor\texteditor.py'; при работе с некоторыми редакторами можно было бы
передать команду перехода к первому совпадению с искомой строкой;
################################################################################
"""

import os, sys
from visitor import SearchVisitor

class EditVisitor(SearchVisitor):
    """
    открывает для редактирования файлы, содержащие искомую строку и
    находящиеся в каталоге startDir и ниже
    """
    editor = r'/usr/bin/nano'
    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))
