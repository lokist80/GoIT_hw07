# README.md
## GoIT homework 7

У цьому домашньому завданні ми зробимо із скрипта розбору папки Python-пакет та консольний скрипт, який можна викликати у будь-якому місці системи з консолі командою `clean-folder`. Для цього вам треба створити структуру файлів та папок:

```
├── clean_folder
│    ├── clean_folder
│    │   ├── clean.py
│    │   └── __init__.py
│    └── setup.py
```
У `clean_folder/clean_folder/clean.py` треба помістити все, що ми зробили на попередніх домашніх завданнях по розбору папки. Ваше основнє завдання написати `clean_folder/setup.py`, щоб вбудований інструментарій Python міг встановити цей пакет та операційна система могла використати цей пакет як консольну команду.<br>

> ### TREE (необов'язково)<br>
> `tree` - консольна утиліта для деревовидного відображення файлів та каталогів.<br>
> У Windows утиліта працює "з коробки", для Ubuntu/Debian встановлюється командою з терміналу:<br>
> `sudo apt install tree`<br>
> Більше інформації по встановленню та використанню у Linux i Windows --> [тут](https://www.tecmint.com/linux-tree-command-examples/) і [тут](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tree).<br>
> <br>
> __!!! Для повноцінної роботи скрипта, встановлення утиліти НЕ є обов'язковим !!!__

`pip install -i https://test.pypi.org/simple/ Sorting-Files==0.0.2`<br>
[test Pypi link](https://test.pypi.org/project/Sorting-Files/0.0.2/)
