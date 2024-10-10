English
-------
Brief description
-------------

  The program simulates the efficiency of a hybrid system (solar panels) and displays the result in the form of plot.
  With the help of the program, you can analyze the modeled efficiency of solar panels at a specific point (by coordinates) and the amount of energy and money saved.
 
  The results are presented in the form of tables, plots and .csv files.
  
Main functions
--------------

  Based on the data entered by the user, the program builds column plots, where each column is a month.
  
  Graphs include:
    
    -Energy use
    
    -Energy generation
    
    -Percentage of generated energy
    
    -Price of energy consumed
    
    -Price of generated energy
    
    -Percentage of money saved

  Also, the program saves the calculated data in the form of .csv files and displays the data in the console in the form of tables. 

Installation instructions
-------------------------

  Download hybrid_system_modulater.exe from “https://github.com/amt0r/hybrid_solar_system/tree/main/dist” and run.

Usage
-----

  The program input:
  
    -Longitude and latitude of the point to place the solar panels
    
    -Annual energy consumption
    
    -Nominal power of solar panels
    
    -Price per kW-hr
    
    -Year for obtaining insolation data

  After entering the data in the appropriate fields, click on the “Submit” button and wait for the program to calculate and plot the data.
  
  .csv files are saved in the folder “csv_files” that will be created in the directory where hybrid_system_modulater.exe is located.
  The modeling program supports any point on the Earth from 1984 to 2022. The annual consumption cannot be zero.

Using the library and API
-------------------------
    -NASA Power API
    
    -requests
    
    -tkinter
    
    -pandas

    -matplotlib.pyplot

    -seaborn

    -os




    

Українська
-----------
Короткий опис
-------------

  Програма моделює ефективність гібридної системи(сонячні панелі та електромережа) та виводить результат у вигляді графіків.
  За допомогою програми можна аналізувати змодельовану ефективність сонячних панелей у конкретній точці(за координатами) та кількість зекономленої енергії та грошей.
 
  Результати роботи представленні у вигляді таблиць, графіків та .csv файлів.
  
Список основних функцій
-----------------------

  На основі введених користувачем даних, програма будує стовпчасті графіки, де кожен стовбець це місяць.
  
  Графіки:
    
    -Використання енергії
    
    -Генерації енергії
    
    -Відсоток згенерованої енергії
    
    -Ціну споживаної енергії
    
    -Ціну згенерованої енергії
    
    -Відсоток зекономлених грошей

  Також, програма зберігає розраховані дані у вигляді .csv файлів та виводить у консоль дані у вигляді таблиць. 

Інструкція щодо установки
-------------------------

  Завантажити hybrid_system_modulater.exe з "https://github.com/amt0r/hybrid_solar_system/tree/main/dist" та запустити.

Використання
------------

  Програма на вхід приймає:
  
    -Довготу та широту точки для розміщення сонячних панелей
    
    -Річне споживання енергії
    
    -Номінальну потужність сонячних панелей
    
    -Ціну за кВт-год
    
    -Рік для отримання даних про інсоляцію

  Після введення даних у відповідні поля, потрібно натиснути на кнопку "Submit" та зачекати поки програма порахує та побудує графіки.
  
  .csv файли зберігаються у папці "csv_files" що створиться у тій директорії де знаходиться hybrid_system_modulater.exe
  Програма для моделювання підтримує будь-яку точку Землі з 1984 по 2022. Річне споживання не може бути нульовим.

Використанні бібліотеки та API
------------------------------
    -NASA Power API
    
    -requests
    
    -tkinter
    
    -pandas

    -matplotlib.pyplot

    -seaborn

    -os
