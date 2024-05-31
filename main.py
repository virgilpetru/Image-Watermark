from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog


# ---------------------------- FILE UPLOAD / SUBMIT ------------------------------- #

def upload_image():
    global filename
    filename = filedialog.askopenfilename()
    upload_image_button.config(fg="white")
    print("Selected:" + filename)

def watermark_image():
    global filename
    text_to_write = type_box.get()
    main_img = Image.open(filename).convert('RGBA')

    watermark = Image.new('RGBA', main_img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    weight, height = main_img.size
    a, b = int(weight / 2), int(height / 2)
    if a > b:
        font_size = b
    elif a < b:
        font_size = a
    else:
        font_size = a

    font = ImageFont.truetype('Arial',int(font_size/8))
    draw.text((a, b), text_to_write, font=font, fill=(255, 255, 255, 170), anchor="ms")
    final_image = Image.alpha_composite(main_img, watermark)

    id_to_save = filename.split('.')[0] + '.png'
    final_image.save(id_to_save)
    final_image.show()

    type_box.delete(0, END)
    upload_image_button.config(fg="black")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Image Watermark Generator")
window.config(padx=10, pady=10)

image = Image.open("photo-1550684376-efcbd6e3f031.jpeg")
image = image.resize((800, 600))
background_img = ImageTk.PhotoImage(image)
canvas = Canvas(width=700, height=500)
canvas.create_image(300, 200, image=background_img)
canvas.grid(column=0, row=0, rowspan=18, columnspan=4)

# Text Messages
welcome_text = canvas.create_text(350,100, fill="orange red", text="Welcome to Image Watermark Generator",
                                  font=("Times", 30))
type_text = canvas.create_text(350,150, fill="orange red", text="Type your text below", font=("Times", 25))

# Entry Box
type_box = Entry(fg="white", bg="black", font=("Arial", 20, 'bold'))
type_box.grid(column=1, row=8, columnspan=2,sticky=W+E)

# Buttons
upload_image_button = Button(text="Upload", font=("Arial", 20, "bold"), command=upload_image)
upload_image_button.grid(column=1, row=9,sticky=W+E)

submit = Button(text="Submit", font=("Arial", 20, "bold"),command=watermark_image)
submit.grid(column=2, row=9, sticky=W+E)

window.mainloop()