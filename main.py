from tkinter import *
from tkinter.font import BOLD

# ---------------------------- CONSTANTS ------------------------------- #

#FONTS
FONT_NAME = "Courier"
LABEL_FONT = ("Helvetica" , 36 , BOLD)
#COLORS
WINDOW_BG_COLOR = "#394867"
HEADER_COLOR = "#f1f6f9"
SHORT_BREAK_COLOR = "#aee6e6"
LONG_BREAK_COLOR = "#ffd369"
#TIMER 
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#Button
BUTTONS_STATE = "normal"

#LOOP GLOBALS
WORK_LOOP = 0
IS_LOOP_CONTINUE = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global WORK_LOOP , IS_LOOP_CONTINUE
    checkmark_list.clear()
    print_checkmarks(checkmark_list)
    timer_label.config( text="POMODORO TIMER" , fg=HEADER_COLOR )
    start_button.config( state="normal")
    IS_LOOP_CONTINUE = False
    WORK_LOOP = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global WORK_LOOP , IS_LOOP_CONTINUE
    if not ( IS_LOOP_CONTINUE ) :
        start_button.config( state="disable" )
        reset_button.config( state="disable" )
        IS_LOOP_CONTINUE = True
    
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if WORK_LOOP % 2 == 0 and WORK_LOOP < 8:
        timer_label.config( text="Work Time" , fg=LONG_BREAK_COLOR )
        count_down(work_sec)
        
    elif WORK_LOOP % 2 != 0 and WORK_LOOP < 8:
        timer_label.config( text="Short Break" ,  fg=SHORT_BREAK_COLOR )
        count_down( short_break_sec )
        add_checkmark()
        print_checkmarks( checkmark_list )
        

    elif WORK_LOOP == 8:
        timer_label.config( text="Long Break" )
        add_checkmark()
        print_checkmarks( checkmark_list )
        count_down( long_break_sec ) 
        reset_button.config( state="normal" )
        
        
        
        
    WORK_LOOP += 1

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minute = count // 60
    second = count % 60

    if second ==0:
        second ="00"
    
    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text , text = f"{ minute }:{ second }")

    if count > 0:

        window.after(1000 , count_down , count - 1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100 , pady=10 , bg=WINDOW_BG_COLOR)


# Timer Canvas
canvas = Canvas(width=512 , height= 512 , bg=WINDOW_BG_COLOR , highlightthickness=0)
timer_img = PhotoImage(file="clock.png")
canvas.create_image(256,256, image=timer_img)

timer_text = canvas.create_text(256 , 128 , text="00:00" , font=( FONT_NAME , 35 ,"bold" )   )
canvas.grid(column=1 , row=1 , pady= (0,100) )



#Labels
timer_label = Label(text="POMODORO TIMER" ,fg=HEADER_COLOR,  font=LABEL_FONT)
timer_label.config(padx=20,pady=30 , bg=WINDOW_BG_COLOR)
timer_label.grid(column=1 , row=0)

#Check marks canvas

checkmark_list = []

#Check mark functions
def add_checkmark():
    canvas_img = PhotoImage(file="check.png" )
    canvas_img = canvas_img.subsample(8)
    checkmark_list.append(canvas_img)
    

def print_checkmarks(checkmark_list):
    pos_x = 56 
    pos_y = 75

    for checkmark in checkmark_list:
        check_canvas.create_image(pos_x,pos_y , image = checkmark)
        check_canvas.grid(column=1 , row=2)
        pos_x += 100
   

# Checkmark canvas
check_canvas  =  Canvas(width=512 , height= 150 , bg=WINDOW_BG_COLOR ,highlightthickness=0  )


#Buttons 

# Start Button 
start_button = Button(text="Start", command=start_timer , font=LABEL_FONT , width= 8 , state = BUTTONS_STATE )
start_button.grid(column=0,row=2 , padx=(0,100))

# Reset Button
reset_button = Button(text="Reset", command=reset_timer , font=LABEL_FONT , padx= 20 , width= 8 , state = BUTTONS_STATE)
reset_button.grid(column=2,row=2 , padx=(100,0))


window.mainloop()