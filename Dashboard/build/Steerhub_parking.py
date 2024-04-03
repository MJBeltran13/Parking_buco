from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json
import time

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True)
    data = Column(String)
    date_added = Column(DateTime, default=datetime.now)

engine = create_engine('sqlite:///sample.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\ADMIN\Documents\GitHub\Parking_buco\Dashboard\build\assets\frame0"
)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("862x471")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=471,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(431.0, 235.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(317.0, 73.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(317.0, 114.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(317.0, 155.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(317.0, 192.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(317.0, 230.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(317.0, 271.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(317.0, 312.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(317.0, 349.0, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(317.0, 390.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(317.0, 427.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(540.0, 32.99999999999999, image=image_image_12)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(540.0, 74.0, image=image_image_13)

image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(540.0, 115.0, image=image_image_14)

image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(540.0, 152.0, image=image_image_15)

image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(540.0, 190.0, image=image_image_16)

image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(540.0, 231.0, image=image_image_17)

image_image_18 = PhotoImage(file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(540.0, 272.0, image=image_image_18)

image_image_19 = PhotoImage(file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(540.0, 309.0, image=image_image_19)

image_image_20 = PhotoImage(file=relative_to_assets("image_20.png"))
# image_20 = canvas.create_image(540.0, 350.0, image=image_image_20)

image_image_21 = PhotoImage(file=relative_to_assets("image_21.png"))
# image_21 = canvas.create_image(540.0, 390.0, image=image_image_21)

image_image_22 = PhotoImage(file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(540.0, 428.0, image=image_image_22)


image_image_23 = PhotoImage(file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(582.0, 371.0, image=image_image_23)

image_image_24 = PhotoImage(file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(274.0, 410.0, image=image_image_24)

image_image_25 = PhotoImage(file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(274.0, 330.0, image=image_image_25)

image_image_26 = PhotoImage(file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(274.0, 252.0, image=image_image_26)

image_image_27 = PhotoImage(file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(274.0, 173.0, image=image_image_27)

image_image_28 = PhotoImage(file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(274.0, 94.0, image=image_image_28)

image_image_29 = PhotoImage(file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(274.0, 410.0, image=image_image_29)

image_image_30 = PhotoImage(file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(274.0, 330.0, image=image_image_30)

image_image_31 = PhotoImage(file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(274.0, 252.0, image=image_image_31)

image_image_32 = PhotoImage(file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(274.0, 173.0, image=image_image_32)

image_image_33 = PhotoImage(file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(274.0, 94.0, image=image_image_33)

image_image_34 = PhotoImage(file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(582.0, 212.0, image=image_image_34)

image_image_35 = PhotoImage(file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(582.0, 133.0, image=image_image_35)

image_image_36 = PhotoImage(file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(582.0, 54.0, image=image_image_36)

image_image_37 = PhotoImage(file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(582.0, 292.0, image=image_image_37)

image_image_38 = PhotoImage(file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(582.0, 371.0, image=image_image_38)

image_image_39 = PhotoImage(file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(582.0, 212.0, image=image_image_39)

image_image_40 = PhotoImage(file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(582.0, 133.0, image=image_image_40)

image_image_41 = PhotoImage(file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(582.0, 54.0, image=image_image_41)

image_image_42 = PhotoImage(file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(582.0, 292.0, image=image_image_42)

image_Ground = PhotoImage(file=relative_to_assets("Ground.png"))
# Ground = canvas.create_image(582.0, 371.0, image=image_Ground)

image_Ground1 = PhotoImage(file=relative_to_assets("Ground.png"))

ppm = canvas.create_text(
    712.0,
    193.0,
    anchor="nw",
    text="Initial Text 1",
    fill="#FCFCFC",
    font=("RobotoRoman Black", 24 * -1),
)

ave = canvas.create_text(
    712.0,
    352.0,
    anchor="nw",
    text="Initial Text 2",
    fill="#FCFCFC",
    font=("RobotoRoman Black", 24 * -1),
)

condition = canvas.create_text(
    726.0,
    297.0,
    anchor="center",
    text="Initial Text 3",
    fill="#FCFCFC",
    font=("RobotoRoman Black", 24 * -1),
)

# All defs

def create_image(canvas_item, image_path, x, y):
    image = PhotoImage(file=image_path)
    canvas_item = canvas.create_image(x, y, image=image)
    return canvas_item, image

def delete_image(canvas_item):
    try:
        canvas.delete(canvas_item)
    except Exception as e:
        print(f"Error deleting canvas item: {e}")


def fetch_latest_data():
    latest_record = session.query(Sample).order_by(Sample.date_added.desc()).first()
    if latest_record:
        data = json.loads(latest_record.data)
        return data
    else:
        return None
    
image_21 = None 
image_20 = None

def update_image(array):
    """
    Update canvas images based on the array.

    Args:
        array: Array indicating whether to display or hide each image.
    """
    global Ground, Ground1, image_20, image_21, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, image_10, image_11, image_12, image_13, image_14, image_15, image_16, image_17, image_18, image_19, image_20, image_21, image_22, image_23, image_24, image_25, image_26, image_27, image_28, image_29, image_30, image_31, image_32, image_33, image_34, image_35, image_36, image_37, image_38, image_39, image_40, image_41, image_42  # Add other image variables here as needed  # Add other image variables here as needed

    # if array[0] == 1:
    #     image_1 = create_image(canvas, relative_to_assets("image_1.png"), 431.0, 235.0)
    # elif array[0] == 0:
    #     delete_image(image_1)

    if array[1] == 1:
        image_2 = create_image(canvas, relative_to_assets("image_2.png"), 317.0, 73.0)
    elif array[1] == 0:
        delete_image(image_2)

    if array[2] == 1:
        image_3 = create_image(canvas, relative_to_assets("image_3.png"), 317.0, 114.0)
    elif array[2] == 0:
        delete_image(image_3)

    if array[3] == 1:
        image_4 = create_image(canvas, relative_to_assets("image_4.png"), 317.0, 155.0)
    elif array[3] == 0:
        delete_image(image_4)

    if array[4] == 1:
        image_5 = create_image(canvas, relative_to_assets("image_5.png"), 317.0, 192.0)
    elif array[4] == 0:
        delete_image(image_5)

    if array[5] == 1:
        image_6 = create_image(canvas, relative_to_assets("image_6.png"), 317.0, 230.0)
    elif array[5] == 0:
        delete_image(image_6)

    if array[6] == 1:
        image_7 = create_image(canvas, relative_to_assets("image_7.png"), 317.0, 271.0)
    elif array[6] == 0:
        delete_image(image_7)

    if array[7] == 1:
        image_8 = create_image(canvas, relative_to_assets("image_8.png"), 317.0, 312.0)
    elif array[7] == 0:
        delete_image(image_8)

    if array[8] == 1:
        image_9 = create_image(canvas, relative_to_assets("image_9.png"), 317.0, 349.0)
    elif array[8] == 0:
        delete_image(image_9)

    if array[9] == 1:
        image_10 = create_image(
            canvas, relative_to_assets("image_10.png"), 317.0, 390.0
        )
    elif array[9] == 0:
        delete_image(image_10)

    if array[10] == 1:
        image_11 = create_image(
            canvas, relative_to_assets("image_11.png"), 317.0, 427.0
        )
    elif array[10] == 0:
        delete_image(image_11)

    if array[11] == 1:
        image_12 = create_image(
            canvas, relative_to_assets("image_12.png"), 540.0, 32.99999999999999
        )
    elif array[11] == 0:
        delete_image(image_12)

    if array[12] == 1:
        image_13 = create_image(canvas, relative_to_assets("image_13.png"), 540.0, 74.0)
    elif array[12] == 0:
        delete_image(image_13)

    if array[13] == 1:
        image_14 = create_image(
            canvas, relative_to_assets("image_14.png"), 540.0, 115.0
        )
    elif array[13] == 0:
        delete_image(image_14)

    if array[14] == 1:
        image_15 = create_image(
            canvas, relative_to_assets("image_15.png"), 540.0, 152.0
        )
    elif array[14] == 0:
        delete_image(image_15)

    if array[15] == 1:
        image_16 = create_image(
            canvas, relative_to_assets("image_16.png"), 540.0, 190.0
        )
    elif array[15] == 0:
        delete_image(image_16)

    if array[16] == 1:
        image_17 = create_image(
            canvas, relative_to_assets("image_17.png"), 540.0, 231.0
        )
    elif array[16] == 0:
        delete_image(image_17)

    if array[17] == 1:
        image_18 = create_image(
            canvas, relative_to_assets("image_18.png"), 540.0, 272.0
        )
    elif array[17] == 0:
        delete_image(image_18)

    if array[18] == 1:
        image_19 = create_image(
            canvas, relative_to_assets("image_19.png"), 540.0, 309.0
        )
    elif array[18] == 0:
        delete_image(image_19)

    if array[19] == 1:
        image_20 = create_image(canvas, relative_to_assets("image_20.png"), 540.0, 350.0)
        
    elif array[19] == 0:
        print("car1 is deleted")
        # delete_image(image_20)
        # delete_image(image_20)
        Ground = create_image(canvas, relative_to_assets("Ground.png"), 539.0, 350.0)

    if array[20] == 1:
        image_21 = create_image(canvas, relative_to_assets("image_21.png"), 540.0, 390.0)  # car2
        # car2
    elif array[20] == 0:
        print("car2 is deleted")
        # delete_image(image_21)
        # delete_image(image_21)
        Ground1 = create_image(canvas, relative_to_assets("Ground1.png"), 539.0, 390.0)

    if array[21] == 1:
        image_22 = create_image(
            canvas, relative_to_assets("image_22.png"), 540.0, 428.0
        )
    elif array[21] == 0:
        delete_image(image_22)

    if array[22] == 1:
        image_23 = create_image(
            canvas, relative_to_assets("image_23.png"), 582.0, 371.0
        )
    elif array[22] == 0:
        delete_image(image_23)

    if array[23] == 1:
        image_24 = create_image(
            canvas, relative_to_assets("image_24.png"), 274.0, 410.0
        )
    elif array[23] == 0:
        delete_image(image_24)

    if array[24] == 1:
        image_25 = create_image(
            canvas, relative_to_assets("image_25.png"), 274.0, 330.0
        )
    elif array[24] == 0:
        delete_image(image_25)

    if array[25] == 1:
        image_26 = create_image(
            canvas, relative_to_assets("image_26.png"), 274.0, 252.0
        )
    elif array[25] == 0:
        delete_image(image_26)

    if array[26] == 1:
        image_27 = create_image(
            canvas, relative_to_assets("image_27.png"), 274.0, 173.0
        )
    elif array[26] == 0:
        delete_image(image_27)

    if array[27] == 1:
        image_28 = create_image(canvas, relative_to_assets("image_28.png"), 274.0, 94.0)
    elif array[27] == 0:
        delete_image(image_28)

    if array[28] == 1:
        image_29 = create_image(
            canvas, relative_to_assets("image_29.png"), 274.0, 410.0
        )
    elif array[28] == 0:
        delete_image(image_29)

    if array[29] == 1:
        image_30 = create_image(
            canvas, relative_to_assets("image_30.png"), 274.0, 330.0
        )
    elif array[29] == 0:
        delete_image(image_30)

    if array[30] == 1:
        image_31 = create_image(
            canvas, relative_to_assets("image_31.png"), 274.0, 252.0
        )
    elif array[30] == 0:
        delete_image(image_31)

    if array[31] == 1:
        image_32 = create_image(
            canvas, relative_to_assets("image_32.png"), 274.0, 173.0
        )
    elif array[31] == 0:
        delete_image(image_32)

    if array[32] == 1:
        image_33 = create_image(canvas, relative_to_assets("image_33.png"), 274.0, 94.0)
    elif array[32] == 0:
        delete_image(image_33)

    if array[33] == 1:
        image_34 = create_image(
            canvas, relative_to_assets("image_34.png"), 582.0, 212.0
        )
    elif array[33] == 0:
        delete_image(image_34)

    if array[34] == 1:
        image_35 = create_image(
            canvas, relative_to_assets("image_35.png"), 582.0, 133.0
        )
    elif array[34] == 0:
        delete_image(image_35)

    if array[35] == 1:
        image_36 = create_image(canvas, relative_to_assets("image_36.png"), 582.0, 54.0)
    elif array[35] == 0:
        delete_image(image_36)

    if array[36] == 1:
        image_37 = create_image(
            canvas, relative_to_assets("image_37.png"), 582.0, 292.0
        )
    elif array[36] == 0:
        delete_image(image_37)

    if array[37] == 1:
        image_38 = create_image(
            canvas, relative_to_assets("image_38.png"), 582.0, 371.0
        )
    elif array[37] == 0:
        delete_image(image_38)

    if array[38] == 1:
        image_39 = create_image(
            canvas, relative_to_assets("image_39.png"), 582.0, 212.0
        )

    elif array[38] == 0:
        delete_image(image_39)

    if array[39] == 1:
        image_40 = create_image(
            canvas, relative_to_assets("image_40.png"), 582.0, 133.0
        )

    elif array[39] == 0:
        delete_image(image_40)

    if array[40] == 1:
        image_41 = create_image(canvas, relative_to_assets("image_41.png"), 582.0, 54.0)
    elif array[40] == 0:
        delete_image(image_41)

    if array[41] == 1:
        image_42 = create_image(
            canvas, relative_to_assets("image_42.png"), 582.0, 292.0
        )
    elif array[41] == 0:
        delete_image(image_42)

def update_canvas_text():
    global sample_array
    sample_array = fetch_latest_data()
    canvas.itemconfig(ppm, text=str(sample_array[42]))  # Update ppm text
    canvas.itemconfig(ave, text=str(sample_array[43]))  # Update ave text
    canvas.itemconfig(condition, text=str(sample_array[44]))  # Update condition text
    print("updated text")
    print(sample_array)
    update_image(sample_array)
    print("canva deleted")
    print(sample_array[19])
    print(sample_array[20])
    print("updated parking")
    window.after(5000, update_canvas_text)




# Void Loop
update_canvas_text()
window.resizable(False, False)
window.mainloop()
