import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('400x600')
root.title('SideBar Tk')

# icons
toggle_icon = tk.PhotoImage(file='images/toggle_btn_icon.png')
home_icon = tk.PhotoImage(file='images/home_icon.png')
service_icon = tk.PhotoImage(file='images/services_icon.png')
updates_icon = tk.PhotoImage(file='images/updates_icon.png')
contact_icon = tk.PhotoImage(file='images/contact_icon.png')
about_icon = tk.PhotoImage(file='images/about_icon.png')
close_icon = tk.PhotoImage(file='images/close_btn_icon.png')

def switch_indication(indicator_lb):
    home_btn_indicator.config(bg=menu_bar_color)
    service_btn_indicator.config(bg=menu_bar_color)
    updates_btn_indicator.config(bg=menu_bar_color)
    contact_btn_indicator.config(bg=menu_bar_color)
    about_btn_indicator.config(bg=menu_bar_color)
    indicator_lb.config(bg='white')

# colors
menu_bar_color = "#383838"

menu_bar_frame = tk.Frame(root, bg=menu_bar_color)
menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate(flag=False)
menu_bar_frame.configure(width=45)

toggle_menu_btn = tk.Button(menu_bar_frame, image=toggle_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color)
toggle_menu_btn.place(x=4, y=10, width=30, height=40)

home_menu_btn = tk.Button(menu_bar_frame, image=home_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: switch_indication(indicator_lb=home_btn_indicator))
home_menu_btn.place(x=9, y=130, width=30, height=40)

home_btn_indicator = tk.Label(menu_bar_frame, bg='white')
home_btn_indicator.place(x=3, y=130, height=40, width=3)

service_menu_btn = tk.Button(menu_bar_frame, image=service_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: switch_indication(indicator_lb=service_btn_indicator))
service_menu_btn.place(x=9, y=190, width=30, height=40)

service_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
service_btn_indicator.place(x=3, y=190, height=40, width=3)

updates_menu_btn = tk.Button(menu_bar_frame, image=updates_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: switch_indication(indicator_lb=updates_btn_indicator))
updates_menu_btn.place(x=9, y=250, width=30, height=40)

updates_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
updates_btn_indicator.place(x=3, y=250, height=40, width=3)

contact_menu_btn = tk.Button(menu_bar_frame, image=contact_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: switch_indication(indicator_lb=contact_btn_indicator))
contact_menu_btn.place(x=9, y=310, width=30, height=40)

contact_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
contact_btn_indicator.place(x=3, y=310, height=40, width=3)

about_menu_btn = tk.Button(menu_bar_frame, image=about_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, command=lambda: switch_indication(indicator_lb=about_btn_indicator))
about_menu_btn.place(x=9, y=370, width=30, height=40)

about_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
about_btn_indicator.place(x=3, y=370, height=40, width=3)


root.mainloop()