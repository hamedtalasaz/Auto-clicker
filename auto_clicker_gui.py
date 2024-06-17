import pyautogui
import time
import random
import keyboard
import tkinter as tk


def auto_clicker():
    message.config(text="")
    try :
        click_count = int(click_counter_entry.get())
        click_speed = float(speed_entry.get())
        position_x_random_a_get =int(position_x_random_a.get())
        position_x_random_b_get =int(position_x_random_b.get())
        position_y_random_a_get =int(position_y_random_a.get())
        position_y_random_b_get =int(position_y_random_b.get())
        for _ in range(click_count): 
            pyautogui.click(random.randint(position_x_random_a_get,position_x_random_b_get),
                            random.randint(position_y_random_a_get,position_y_random_b_get))

            if (int(_) + 1) == 1 :
                clicked_counter_label.config(text='Clicked Just {}  !!!'.format(int(_) + 1))
            else :    
                clicked_counter_label.config(text='Clicked {} times !!!'.format(int(_) + 1))
            
            time.sleep(click_speed)
            if keyboard.is_pressed('q') :
                clicked_counter_label.config(text='Clicked {} times !!!\nStopped'.format(int(_) + 1))
                break
    except ValueError:
        message.config(text="Enter Number Please")
        pass

def pointer_position_finder():
    position = (str(pyautogui.position())).split()
    x , y = position[0] , position[1]
    position_x_finder_amount.config(text = x[8:-1])
    position_y_finder_amount.config(text = y[2:-1])
    root.after(100,pointer_position_finder)



root = tk.Tk()
root.title("Auto Clicker")
# Make it Always on top
root.attributes('-topmost',True)
root_width = 180
root_height = 480
root.minsize(root_width,root_height)
root.resizable(False,False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width / 2 - root_width
y = screen_height /2 - root_height
root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')

header_frame = tk.Frame(root,borderwidth=1,relief='solid')
header_frame.grid(row=0,column=0,pady=2,padx=20,sticky='w')
app_name = tk.Label(header_frame,text="Auto Clicker v 1.0.0")
app_name.grid(row=0,column=0,padx=(0,10))

pointer_position_finder_frame = tk.Frame(root,borderwidth=1,relief='solid')
pointer_position_finder_frame.grid(row=1,column=0,pady=2,padx=20,sticky='w')
pointer_x_title = tk.Label(pointer_position_finder_frame,text='Pointer X')
pointer_x_title.grid(row=0,column=0)
pointer_y_title = tk.Label(pointer_position_finder_frame,text='Pointer Y')
pointer_y_title.grid(row=0,column=1,padx=(0,10))
position_x_finder_amount = tk.Label(pointer_position_finder_frame,text= "X",width=7)
position_x_finder_amount.grid(row=1,column=0)
position_y_finder_amount = tk.Label(pointer_position_finder_frame,text= "Y",width=7)
position_y_finder_amount.grid(row=1,column=1)

random_position_frame = tk.Frame(root,borderwidth=1,relief='solid')
random_position_frame.grid(row=2,column=0,pady=2,padx=20,sticky='w')
position_x_range_label = tk.Label(random_position_frame,text='Rang of X')
position_x_range_label.grid(row=0,column=0)
position_Y_range_label = tk.Label(random_position_frame,text='Rang of Y')
position_Y_range_label.grid(row=0,column=1)
position_x_random_a = tk.Entry(random_position_frame,width=7)
position_x_random_a.insert(0,200)
position_x_random_a.grid(row=1,column=0)
position_x_random_b = tk.Entry(random_position_frame,width=7)
position_x_random_b.insert(0,350)
position_x_random_b.grid(row=2,column=0)
position_y_random_a = tk.Entry(random_position_frame,width=7)
position_y_random_a.insert(0,400)
position_y_random_a.grid(row=1,column=1,pady=2)
position_y_random_b = tk.Entry(random_position_frame,width=7)
position_y_random_b.insert(0,550)
position_y_random_b.grid(row=2,column=1,pady=6)

speed_frame = tk.Frame(root,borderwidth=1,relief='solid')
speed_frame.grid(row=3,column=0,pady=2,padx=20,sticky='w')
speed_entry = tk.Entry(speed_frame,width=7)
speed_entry.insert(0,0.01)
speed_entry.grid(row=1,column=0,pady=5)
speed_detail = tk.Label(speed_frame,text='Speed in milisecond')
speed_detail.grid(row=0,column=0)

click_counter_frame = tk.Frame(root,borderwidth=1,relief='solid')
click_counter_frame.grid(row=4,column=0,pady=2,padx=20,sticky='w')
click_counter_entry = tk.Entry(click_counter_frame,width=7)
click_counter_entry.insert(0,1)
click_counter_entry.grid(row=1,column=0,pady=5)
click_counter_entry_detail = tk.Label(click_counter_frame,text='Click Number')
click_counter_entry_detail.grid(row=0,column=0,padx=(22,22))

start_frame = tk.Frame(root,borderwidth=1,relief='solid')
start_frame.grid(row=5,column=0,pady=2,padx=20,sticky='w')
start_btn = tk.Button(start_frame,text="Start",width=7,command=auto_clicker)
start_btn.grid(row=0,column=0,pady=5,padx=(36,36))
stop_txt = tk.Label(start_frame,text = 'Press Q to Stop')
stop_txt.grid(row=1,column=0,pady=(0,5))

messages_frame = tk.Frame(root)
messages_frame.grid(row=6,column=0)
clicked_counter_label = tk.Label(messages_frame,text="")
clicked_counter_label.grid(row=0,column=0)
message = tk.Label(messages_frame,text="",fg='red')
message.grid(row=1,column=0)

pointer_position_finder()
root.mainloop()
