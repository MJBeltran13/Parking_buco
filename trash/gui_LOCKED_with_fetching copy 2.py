import json
import time
from datetime import datetime
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\ADMIN\Documents\GitHub\Parking_buco\Dashboard\build\assets\frame0"
)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_image(canvas, image_path, x, y):
    image = PhotoImage(file=image_path)
    canvas_item = canvas.create_image(x, y, image=image)
    print(f"Image created at coordinates ({x}, {y})")
    return canvas_item, image

def delete_image(canvas, canvas_item):
    canvas.delete(canvas_item)
    print("Image deleted from canvas")

# def delete_all_images(canvas):
#     for image_item in canvas.find_all():
#         canvas.delete(image_item)
#     print("All images deleted from canvas")

def fetch_latest_data():
    latest_record = session.query(Sample).order_by(Sample.date_added.desc()).first()
    if latest_record:
        data = json.loads(latest_record.data)
        return data
    else:
        return None

def update_image(canvas, image_items, image_paths, data):
    for i in range(len(image_items)):
        if data[i] == 1:
            image_items[i], _ = create_image(canvas, image_paths[i], *image_positions[i])
        else:
            delete_image(canvas, image_items[i])

def update_canvas_text(canvas, ppm_text, ave_text, condition_text, data):
    canvas.itemconfig(ppm_text, text=str(data[42]))  # Update ppm text
    canvas.itemconfig(ave_text, text=str(data[43]))  # Update ave text
    canvas.itemconfig(condition_text, text=str(data[44]))  # Update condition text
    update_image(canvas, image_items, image_paths, data)
    print("Canvas updated")


def main():
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

    image_paths = [
        relative_to_assets(f"image_{i}.png") for i in range(1, 43)
    ]

    global image_positions
    image_positions = [
        (431.0, 235.0), (317.0, 73.0), (317.0, 114.0), (317.0, 155.0), (317.0, 192.0),
        (317.0, 230.0), (317.0, 271.0), (317.0, 312.0), (317.0, 349.0), (317.0, 390.0),
        (317.0, 427.0), (540.0, 32.99999999999999), (540.0, 74.0), (540.0, 115.0),
        (540.0, 152.0), (540.0, 190.0), (540.0, 231.0), (540.0, 272.0), (540.0, 309.0),
        (540.0, 350.0), (540.0, 387.0), (540.0, 428.0), (582.0, 371.0), (274.0, 410.0),
        (274.0, 330.0), (274.0, 252.0), (274.0, 173.0), (274.0, 94.0), (274.0, 410.0),
        (274.0, 330.0), (274.0, 252.0), (274.0, 173.0), (274.0, 94.0), (582.0, 212.0),
        (582.0, 133.0), (582.0, 54.0), (582.0, 292.0), (582.0, 371.0), (582.0, 212.0),
        (582.0, 133.0), (582.0, 54.0), (582.0, 292.0)
    ]

    global image_items
    image_items = [None] * len(image_paths)

    ppm_text = canvas.create_text(
        712.0,
        193.0,
        anchor="nw",
        text="Initial Text 1",
        fill="#FCFCFC",
        font=("RobotoRoman Black", 24),
    )

    ave_text = canvas.create_text(
        712.0,
        352.0,
        anchor="nw",
        text="Initial Text 2",
        fill="#FCFCFC",
        font=("RobotoRoman Black", 24),
    )

    condition_text = canvas.create_text(
        726.0,
        297.0,
        anchor="center",
        text="Initial Text 3",
        fill="#FCFCFC",
        font=("RobotoRoman Black", 24),
    )

    # Fetch latest data and update canvas after 5 seconds
    window.after(5000, lambda: update_canvas_text(canvas, ppm_text, ave_text, condition_text, fetch_latest_data()))

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()
