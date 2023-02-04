import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class Calendar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.calendar = ttk.LabelFrame(self, text='Calendar')
        self.calendar.grid(column=0, row=0, padx=8, pady=4)

        ttk.Label(self.calendar, text="Year:").grid(column=1, row=0)
        self.year_entry = ttk.Entry(self.calendar)
        self.year_entry.grid(column=2, row=0)

        ttk.Label(self.calendar, text="Month:").grid(column=3, row=0)
        self.month_entry = ttk.Entry(self.calendar)
        self.month_entry.grid(column=4, row=0)

        ttk.Button(self.calendar, text='Show', command=self.show_calendar).grid(column=5, row=0)

        self.calendar_display = ttk.LabelFrame(self, text='Calendar')
        self.calendar_display.grid(column=0, row=1, padx=8, pady=4)

    def show_calendar(self):
        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        self.display_calendar(year, month)

    def display_calendar(self, year, month):
        cal = calendar.monthcalendar(year, month)

        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day == 0:
                    continue
                btn = ttk.Button(self.calendar_display, text=day)
                btn.grid(column=j, row=i)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calendar")
    Calendar(root).pack(fill='both', expand=True)
    root.mainloop()