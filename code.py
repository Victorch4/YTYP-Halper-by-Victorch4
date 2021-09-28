# -*- coding: utf-8 -*-

import webbrowser, traceback, os, os.path, pyperclip
from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton  
from tkinter import messagebox

def write_err():
	if os.path.exists('errors_list.log'): os.remove('errors_list.log')
	err_list = open('errors_list.log', 'a')
	err_list.write('%s\n' % traceback.format_exc())
	err_list.close()
	
def print_txt(txt, lang):
	if txt == 'app_name': return 'YTYP Halper by Victorch4 (version 1.5)' ##############
	elif txt == 'v_file' and lang == 'ru': return 'Файл' ##############
	elif txt == 'v_file' and lang == 'en': return 'File'
	elif txt == 'v_file1' and lang == 'ru': return 'Открыть ODR' ##############
	elif txt == 'v_file1' and lang == 'en': return 'Open ODR'
	elif txt == 'v_file2' and lang == 'ru': return 'Копировать' ##############
	elif txt == 'v_file2' and lang == 'en': return 'Copy'
	elif txt == 'open_odr_xml' and lang == 'ru': return 'Для вставки через OpenIV' ##############
	elif txt == 'open_odr_xml' and lang == 'en': return 'For insert via OpenIV'
	elif txt == 'open_odr_cw' and lang == 'ru': return 'Для вставки через CodeWalker' ##############
	elif txt == 'open_odr_cw' and lang == 'en': return 'For insert via CodeWalker'
	elif txt == 'v_portals' and lang == 'ru': return 'Порталы' ##############
	elif txt == 'v_portals' and lang == 'en': return 'Portals'
	elif txt == 'insert_values' and lang == 'ru': return 'Указать значения' ##############
	elif txt == 'insert_values' and lang == 'en': return 'Enter values'
	elif txt == 'insert_values1' and lang == 'ru': return 'С улицы в интерьер (или из комнаты 1 в комнату 2)' ##############
	elif txt == 'insert_values1' and lang == 'en': return 'From exterior to interior (or from room 1 to room 2)'
	elif txt == 'insert_values2' and lang == 'ru': return 'С интерьера на улицу (или из комнаты 2 в комнату 1)' ##############
	elif txt == 'insert_values2' and lang == 'en': return 'From interior to exterior (or from room 2 to room 1)'
	elif txt == 'err_title' and lang == 'ru': return 'Ошибка при указании значений' ##############
	elif txt == 'err_title' and lang == 'en': return 'Error while entering values'
	elif txt == 'err_txt' and lang == 'ru':
		return '''При указании значений для координат допускаются только цифры.
		В качестве разделительного знака допускается точка или запятая.'''.replace('\t', '')
	elif txt == 'err_txt' and lang == 'en':
		return '''When entering values for coordinates, only numbers are allowed.
		A period or comma is allowed as a separator.'''.replace('\t', '')
	elif txt == 'get_portals1' and lang == 'ru': return 'Получить значения вставки через OpenIV' ##############
	elif txt == 'get_portals1' and lang == 'en': return 'Get values to insert via OpenIV'
	elif txt == 'get_portals2' and lang == 'ru': return 'Получить значения для вставки через CodeWalker' ##############
	elif txt == 'get_portals2' and lang == 'en': return 'Get values to insert via CodeWalker'
	elif txt == 'get_portals3' and lang == 'ru': return 'Данные успешно скопированы в буфер обмена' ##############
	elif txt == 'get_portals3' and lang == 'en': return 'Data copied to clipboard successfully'
	elif txt == 'get_portals4' and lang == 'ru': return ['Cнизу справа: ', 'Cверху справа: ', 'Cверху слева: ' , 'Cнизу слева: '] ##############
	elif txt == 'get_portals4' and lang == 'en': return ['Bottom Right:', 'Top Right:', 'Top Left:', 'Bottom Left:']
	elif txt == 'show_values' and lang == 'ru': return 'Получить значения для вставки в YTYP файл' ##############
	elif txt == 'show_values' and lang == 'en': return 'Get values for pasting into YTYP file'
	elif txt == 'v_language': return 'Language' ##############
	elif txt == 'rus': return 'Русский'
	elif txt == 'eng': return 'English'
	elif txt == 'v_about' and lang == 'ru': return 'О программе' ##############
	elif txt == 'v_about' and lang == 'en': return 'About'
	elif txt == 'how_use' and lang == 'ru': return 'Как пользоваться?' ##############
	elif txt == 'how_use_txt' and lang == 'ru':
		return '''С этой программой вы сможете значительно сэкономить своё время при 
		получении значений Boundary Box для моделей. 
		Чтобы получить значения, нужно выбрать, куда вы хотите вставить значения.
		Затем, выбрать один или несколько ODR файлов. После этого, программа 
		выведет необходимые строки для каждого файла и можно будет скопировать
		любой фрагмент из того что вывела программа.

		Кроме этого, программа сделает удобнее ввод координат для порталов.
		Теперь, не нужно вручную исправлять в координатах запятые на точки,
		программа всё сделает автоматически.
		Если какие-либо поля для координат оставить пустыми – для них будет
		установлено значение равное нулю.
		По завершению указания значений, нажмите одну из двух кнопок ниже.
		После этого, указанные значения будут скопированы в буфер обмена.'''.replace('\t', '')
	elif txt == 'how_use' and lang == 'en': return 'How to use?' ##############
	elif txt == 'how_use_txt' and lang == 'en':
		return '''With this program you can significantly save your time 
		when getting Boundary Box values ​​for models.
		To get the values, you need to choose where you want to insert the values.
		Then, select one or more ODR files. 
		After that, the program will display the necessary lines for each file and
		you can copy any fragment from what the program has displayed.

		In addition, the program will make it easier to enter coordinates for portals.
		Now, there is no need to manually correct commas to points in coordinates,
		the program will do everything automatically.
		If any fields for coordinates are left blank, they will be set to zero.
		When you are finished specifying values, click one of the two buttons below.
		After that, the specified values ​​will be copied to the clipboard.'''.replace('\t', '')
	elif txt == 'contact' and lang == 'ru': return 'Связаться с автором' ##############
	elif txt == 'contact' and lang == 'en': return 'Contact the author'
	elif txt == 'support' and lang == 'ru': return 'Поддержать автора' ##############
	elif txt == 'support' and lang == 'en': return 'Support the author'
	elif txt == 'short' and lang == 'ru': return ['VK', 'Discord', 'Telegram', 'QIWI кошелёк'] ##############
	elif txt == 'short' and lang == 'en': return ['VK', 'Discord', 'Telegram', 'QIWI wallet']

def get_coords(odr_files, root, lang):
	total_values_cw, total_values = '', ''
	
	for a in range(0, len(odr_files)):
		with open(odr_files[a]) as odr_files[a]: odr_lines = odr_files[a].read().split('\n')
		filename = str(odr_files[a]).split('/')[-1].split('.odr')[0].strip("'")
		f_filename, f_bbmin, f_bbmax, f_center, f_radius = '', '', '', '', ''
		f_bbmin_cw, f_bbmax_cw, f_center_cw, f_radius_cw = '', '', '', ''
		
		for b in range(0, len(odr_lines)):
			if odr_lines[b].count('AABBMin'): f_filename += '%s' % filename
			if odr_lines[b].count('AABBMin'): 
				bbmin = odr_lines[b].strip('\t').strip('AABBMin ')
				x, y, z, = bbmin.split(' ')
				f_bbmin += '      <bbMin x="%s" y="%s" z="%s"/>' % (x, y, z)
				f_bbmin_cw += 'BBMin: %s, %s, %s' % (x, y, z)
			if odr_lines[b].count('AABBMax'):
				bbmax = odr_lines[b].strip('\t').strip('AABBMax ')
				x, y, z, = bbmax.split(' ')
				f_bbmax += '      <bbMax x="%s" y="%s" z="%s"/>' % (x, y, z)
				f_bbmax_cw += 'BBMax: %s, %s, %s' % (x, y, z)
			if odr_lines[b].count('Radius'):
				radius = odr_lines[b].strip('\t').strip('Radius ')
				f_radius += '      <bsRadius value="%s"/>' % radius
				f_radius_cw += 'BS Radius: %s' % radius
			if odr_lines[b].count('Center'):
				center = odr_lines[b].strip('\t').strip('Center ')
				x, y, z, = center.split(' ')
				f_center += '      <bsCentre x="%s" y="%s" z="%s"/>' % (x, y, z)
				f_center_cw += 'BS Centre: %s, %s, %s' % (x, y, z)
		total_values += '%s:\n%s\n%s\n%s\n%s\n\n' % (f_filename, f_bbmin, f_bbmax, f_center, f_radius)
		total_values_cw += '%s:\n%s\n%s\n%s\n%s\n\n' % (f_filename, f_bbmin_cw, f_bbmax_cw, f_center_cw, f_radius_cw)
	
	tmp1 = Label(root, justify='left', font="Verdana 10", text='%s%s' % (' ' * 500, '\n' * 500))
	tmp1.place(relx=0.0, rely=0.0)
	
	def total_val(mode):
		txt = scrolledtext.ScrolledText(root, width=70, height=40)
		txt.place(relx=0.0, rely=0.05)
		if mode == 0: txt.insert(INSERT, total_values)
		elif mode == 1: txt.insert(INSERT, total_values_cw)
		txt.configure(state='disabled')
		txt.bind('<Button-3>',rClicker, add='')
	
	rad1 = Radiobutton(root, text=print_txt('open_odr_xml', lang), value=1, command=lambda: total_val(0))  
	rad2 = Radiobutton(root, text=print_txt('open_odr_cw', lang), value=2, command=lambda: total_val(1))   
	rad1.place(relx=0.0, rely=0.0)
	rad2.place(relx=0.3, rely=0.0)
	# root.mainloop()

def ask_window(root, lang):
	if lang == 'ru': txt1, txt2  = 'Выберете файлы', ([(u'Файлы GIMS Evo', '*.odr')])
	elif lang == 'en': txt1, txt2  = 'Select files', ([(u'Files GIMS Evo', '*.odr')])
	odr_files = list(askopenfilenames(title = txt1, initialdir = '%desktop%', filetypes = txt2))
	if odr_files: get_coords(odr_files, root, lang)

def rClicker(e):
	try:
		def rClick_Copy(e, apnd=0): e.widget.event_generate('<<Copy>>')
		e.widget.focus()
		rmenu = Menu(None, tearoff=0, takefocus=0)
		rmenu.add_command(label=print_txt('v_file2', lang), command=lambda e=e: rClick_Copy(e))
		rmenu.tk_popup(e.x_root+60, e.y_root+15,entry="0")

	except TclError: write_err()
	return "break"

def rClickbinder(r):
	try:
		for b in ['Text', 'Entry', 'Listbox', 'Label']: r.bind_class(b, sequence='<Button-3>', func=rClicker, add='')
	except TclError: write_err()

def set_lang(lng):
	lang_conf = open('lang.ini', 'w')
	lang_conf.write(lng)
	lang_conf.close()

def sel_lang(root, lang):
	try:
		if lang == 'ru': lng = 'Language\tru\t1\nLanguage\ten\t0'
		elif lang == 'en': lng = 'Language\tru\t0\nLanguage\ten\t1'
	except: write_err()
	else: set_lang(lng)
	
	if lang == 'ru':
		root.destroy()
		start_app(lang)
	elif lang == 'en':
		root.destroy()
		start_app(lang)

def portals(root, lang):

	def display_full_name(mode, coords_list):
		no_err = True
		
		def get_info():
			info = Label(root, justify='left', fg="blue", font="Verdana 10", text=print_txt('get_portals3', lang))
			info.place(relx=0.21, rely=0.9)
			info.after(1500 , lambda: info.destroy())
		
		v_list = []
		for a in range (0, len(coords_list)):
			vert = coords_list[a].get()
			if vert == '': vert = 0.0
			else: 
				try: vert = float(vert.replace(',', '.'))
				except:
					no_err = False
					messagebox.showerror(print_txt('err_title', lang), print_txt('err_txt', lang))
					portals(root, lang)
					break
			v_list.append(vert)
		
		
		if mode in range(0, 2) and no_err: 
			res = '''            %s\t%s\t%s
            %s\t%s\t%s
            %s\t%s\t%s
            %s\t%s\t%s''' % (v_list[0], v_list[1], v_list[2], v_list[3], v_list[4], v_list[5], v_list[6], v_list[7], v_list[8], v_list[9], v_list[10], v_list[11])
			pyperclip.copy(res)
			get_info()

		if mode in range(2, 4) and no_err:
			res = ('''%s, %s, %s\n%s, %s, %s\n%s, %s, %s
			%s, %s, %s''' % (v_list[0], v_list[1], v_list[2], v_list[3], v_list[4], v_list[5], v_list[6], v_list[7], v_list[8], v_list[9], v_list[10], v_list[11])).replace('\t', '')
			pyperclip.copy(res)
			get_info()
		
	tmp1 = Label(root, justify='left', font="Verdana 10", text='%s%s' % (' ' * 500, '\n' * 500))
	tmp1.place(relx=0.0, rely=0.0)
	
	def get_entry(mode):
		coords_list, x, y, t_pl = [], 0.08, 0.19, print_txt('get_portals4', lang)

		if mode == 0: vertix_list = [[t_pl[0], [x, y]], [t_pl[1], [x, y+0.1]], [t_pl[2], [x, y+0.2]], [t_pl[3], [x, y+0.3]]]
		elif mode == 1: vertix_list = [[t_pl[3], [x, y]], [t_pl[2], [x, y+0.1]], [t_pl[1], [x, y+0.2]], [t_pl[0], [x, y+0.3]]]
		
		for a in range(0, len(vertix_list)):
			vertix_x, vertix_y, vertix_z = StringVar(), StringVar(), StringVar()
			vertix_lebel = Label(text=vertix_list[a][0])
			vertix_lebel_x = Label(text='X = ')
			vertix_lebel_y = Label(text='Y = ')
			vertix_lebel_z = Label(text='Z = ')
			vertix_lebel.place(relx=vertix_list[a][1][0], rely=vertix_list[a][1][1])
			vertix_lebel_x.place(relx=vertix_list[a][1][0] + 0.17, rely=vertix_list[a][1][1])
			vertix_lebel_y.place(relx=vertix_list[a][1][0] + 0.39, rely=vertix_list[a][1][1])
			vertix_lebel_z.place(relx=vertix_list[a][1][0] + 0.61, rely=vertix_list[a][1][1])
			vertix_entry_x = Entry(textvariable=vertix_x)
			vertix_entry_y = Entry(textvariable=vertix_y)
			vertix_entry_z = Entry(textvariable=vertix_z)
			vertix_entry_x.place(relx=vertix_list[a][1][0] + 0.21, rely=vertix_list[a][1][1] + 0.01, width=100)
			vertix_entry_y.place(relx=vertix_list[a][1][0] + 0.43, rely=vertix_list[a][1][1] + 0.01, width=100)
			vertix_entry_z.place(relx=vertix_list[a][1][0] + 0.65, rely=vertix_list[a][1][1] + 0.01, width=100)
			coords_list += [vertix_x, vertix_y, vertix_z]

		message_button = Button(text=print_txt('get_portals1', lang), font="Verdana 10", command=lambda: display_full_name(mode, coords_list))
		message_button.place(relx=x+0.117, rely=y+0.45, width=350, height = 40)
		message_button1 = Button(text=print_txt('get_portals2', lang), font="Verdana 10", command=lambda: display_full_name(mode+2, coords_list))
		message_button1.place(relx=x+0.117, rely=y+0.6, width=350, height = 40)
		
	rad1 = Radiobutton(root, text=print_txt('insert_values1', lang), value=1, command=lambda: get_entry(0))  
	rad2 = Radiobutton(root, text=print_txt('insert_values2', lang), value=2, command=lambda: get_entry(1))   
	if lang == 'ru': x_pl = 0.22
	elif lang == 'en': x_pl = 0.24
	rad1.place(relx=x_pl, rely=0.03)
	rad2.place(relx=x_pl, rely=0.09)

def about(root, lang, mode):
	tmp0 = Label(root, justify='left', font="Verdana 10", text='%s%s' % (' ' * 500, '\n' * 500))
	tmp1 = Label(root, justify='left', font="Verdana 10", text='%s%s' % (' ' * 500, '\n' * 500))
	label1 = Label(root, justify='left', font="Verdana 10", text = print_txt('how_use_txt', lang))
	label2 = Label(root, font="Verdana 12", text = print_txt('contact', lang))
	label3 = Label(root, font="Verdana 10", text = print_txt('short', lang)[0], fg="blue", cursor="hand2")
	label4 = Label(root, font="Verdana 10", text = print_txt('short', lang)[1], fg="blue", cursor="hand2")
	label5 = Label(root, font="Verdana 10", text = print_txt('short', lang)[2], fg="blue", cursor="hand2")
	label6 = Label(root, font="Verdana 10", text = print_txt('support', lang))
	label7 = Label(root, font="Verdana 10", text = print_txt('short', lang)[3], fg="blue", cursor="hand2")
	
	def callback(url): webbrowser.open_new(url)
	
	if mode == 0: 
		tmp0.place(relx=0.0, rely=0.0)
		tmp1.place(relx=0.0, rely=0.4)
		label1.place(relx=0.03, rely=0.2)
	if mode == 1:
		tmp0.place(relx=0.0, rely=0.0)
		tmp1.place(relx=0.0, rely=0.4)
		label2.place(relx=0.345, rely=0.35)
		label3.place(relx=0.335, rely=0.41)
		label3.bind("<Button-1>", lambda e: callback("https://vk.com/im?sel=75339513"))
		label4.place(relx=0.42, rely=0.41)
		label4.bind("<Button-1>", lambda e: callback("https://discord.gg/jz65XaVrFy"))
		label5.place(relx=0.56, rely=0.41)
		label5.bind("<Button-1>", lambda e: callback("https://t.me/Victorch4"))
	if mode == 2:
		tmp0.place(relx=0.0, rely=0.0)
		tmp1.place(relx=0.0, rely=0.4)
		label6.place(relx=0.37, rely=0.35)
		label7.place(relx=0.4, rely=0.42)
		label7.bind("<Button-1>", lambda e: callback("https://qiwi.com/n/VICTORCH4"))
	# root.mainloop()

def window(root, name, size_w, size_h):
	size = '%sx%s' % (size_w, size_h)
	root.title(name)
	root.geometry(size)

def cascad_menu(root, menu, casname, pp_menu, p_list, functions):
	for a in range(0, len(p_list)): casname.add_command(label = p_list[a], command = functions[a])
	menu.add_cascade(label = pp_menu, menu = casname)
	root.config(menu = menu)

try:
	with open('lang.ini') as lng: lng = lng.read().split('\n')
	value = []
	for a in range(0, len(lng)): value.append(int(lng[a].split('\t')[2]))
	ru, en = value
	if ru == 1 and en == 0: lang = 'ru'
	elif ru == 0 and en == 1: lang = 'en'
	else:
		lang = 'ru'
		set_lang('Language\tru\t1\nLanguage\ten\t0')
except:
	write_err()
	lang = 'ru'
	set_lang('Language\tru\t1\nLanguage\ten\t0')

def start_app(lang):
	root = Tk()
	root.resizable(width=False, height=False)
	try: root.iconbitmap('icon.ico')
	except: write_err()
	menu = Menu(root)
	window(root, print_txt('app_name', 'multi'), 580, 450)
	cascad_menu(root, menu, Menu(menu, tearoff = 0), print_txt('v_file', lang), [print_txt('v_file1', lang)], [lambda: ask_window(root, lang)])
	cascad_menu(root, menu, Menu(menu, tearoff = 0), print_txt('v_portals', lang), [print_txt('insert_values', lang)], [lambda: portals(root, lang)])
	
	cascad_menu(root, menu, Menu(menu, tearoff = 0), print_txt('v_language', lang),
	[print_txt('rus', lang), print_txt('eng', lang)], [lambda: sel_lang(root, 'ru'), lambda: sel_lang(root, 'en')])
	
	cascad_menu(root, menu, Menu(menu, tearoff = 0), print_txt('v_about', lang),
	[print_txt('how_use', lang), print_txt('contact', lang), print_txt('support', lang)],
	[lambda: about(root, lang, 0), lambda: about(root, lang, 1), lambda: about(root, lang, 2)])
	root.mainloop()

if __name__ ==  '__main__': start_app(lang)
