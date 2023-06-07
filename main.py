import tkinter as tk



window = tk.Tk()
window.title("Порядок расчёта ребристого радиатора при естественном воздушном охлаждении")



def calculate_r_t_s_i_d(event):
    """
    Определяется тепловое сопротивление радиатора, Rт-с.исх.д, °С/Вт:
    """
    result = 0.96 * ((float(ent_ppp.get()) - float(ent_t_o_s.get())) - (float(ent_ppp.get()) * (float(ent_r_k_t.get()) + float(ent_r_p_k.get()))) / float(ent_ppp.get()))
    lab['text'] = result


# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Помещает рамку в окно приложения.
frm_form.pack()


# Создаем ярлык и текстовок поле для ввода ППП.
lbl_ppp = tk.Label(master=frm_form, text="Р, Вт:")
ent_ppp = tk.Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыка и
# однострочного поля для ввода текста в первый и второй столбец
# первой строки сетки.
lbl_ppp.grid(row=0, column=0, sticky="e")
ent_ppp.grid(row=0, column=1)


# Создаем ярлык и текстовок поле для ввода температуры окружающей среды, То.с, °С..
lbl_t_o_s = tk.Label(master=frm_form, text="То.с, °С:")
ent_t_o_s = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на вторую строку сетки
lbl_t_o_s.grid(row=1, column=0, sticky="e")
ent_t_o_s.grid(row=1, column=1)


# Создаем ярлык и текстовок поле для выбора из справочника максимальной температуры перехода, Тп, °С..
lbl_t_p = tk.Label(master=frm_form, text="Тп, °С:")
ent_t_p = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на третьей строке сетки.
lbl_t_p.grid(row=2, column=0, sticky="e")
ent_t_p.grid(row=2, column=1)



# Создаем ярлык и текстовок поле для выбора из справочника теплового сопротивления переход – корпус, Rп-к, °С/Вт..
lbl_r_p_k = tk.Label(master=frm_form, text="Rп-к, °С/Вт:")
ent_r_p_k = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на четвертой строке сетки.
lbl_r_p_k.grid(row=3, column=0, sticky=tk.E)
ent_r_p_k.grid(row=3, column=1)


# Создаем ярлык и текстовок поле для выбора из справочника теплового контактного сопротивления корпус – теплоотвод, Rк-т, °С/Вт.
lbl_r_k_t = tk.Label(master=frm_form, text="Rк-т, °С/Вт:")
ent_r_k_t = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на пятой строке сетки.
lbl_r_k_t.grid(row=4, column=0, sticky=tk.E)
ent_r_k_t.grid(row=4, column=1)


# Создаем новую рамку `frm_buttons` для размещения
# кнопок "Рассчитать" и вывода результата. Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)


# Создаем поля для вывода результата
lab1 = tk.Label(master=frm_buttons, text="Rт-с.исх.д:")
lab1.pack(side=tk.LEFT, padx=1, ipadx=1)
lab = tk.Label(master=frm_buttons)
lab.pack(side=tk.LEFT, padx=1, ipadx=1)

# Создаем кнопку "Рассчитать" и размещаем ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="Рассчитать")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


btn_submit.bind('<Button-1>', calculate_r_t_s_i_d)
# Запуск приложения.
window.mainloop()
