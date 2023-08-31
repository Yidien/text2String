# coding:utf-8

import os
import PySide2


dir_name = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dir_name, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from guietta import Gui, III, ___, _
from PySide2.QtWidgets import QPlainTextEdit
import re


def transformation_text_to_string(control):
    tmp = control.text_text.toPlainText()
    tmp = re.sub(r'^\s*', ' "', tmp)
    tmp = re.sub(r'\n', r'\\n"\n+"', tmp)
    tmp += '"'
    control.text_string.setPlainText(tmp)
    return


def transformation_string_to_text(control):
    tmp = control.text_string.toPlainText()
    tmp = re.sub(r'(^|\+)\s*"', '', tmp)
    tmp = re.sub(r'(\\n)?\s*"\n', '\n', tmp)
    tmp = re.sub(r'"$', '', tmp)
    control.text_text.setPlainText(tmp)
    return


def event_text2string(gui, *args):
    transformation_text_to_string(gui)
    return


def event_string2text(gui, *args):
    transformation_string_to_text(gui)
    return


def main():
    gui = Gui \
        (
            [(QPlainTextEdit, 'text_text'),  ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, _, (QPlainTextEdit, 'text_string'),  ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,],
            [III, III, III, III, III, III, III, III, III, III, III, (['text2string'], 'bt_text2string'), III, III, III, III, III, III, III, III, III, III, III],
            [III, III, III, III, III, III, III, III, III, III, III, (['string2text'], 'bt_string2text'), III, III, III, III, III, III, III, III, III, III, III],
            [III, III, III, III, III, III, III, III, III, III, III, _, III, III, III, III, III, III, III, III, III, III, III],
        )

    gui.bt_text2string = event_text2string
    gui.bt_string2text = event_string2text

    gui.run()
    return

if __name__ == '__main__':
    main()