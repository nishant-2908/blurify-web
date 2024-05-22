# Importing the required libraries and objects
from flask import Flask, render_template, request, redirect
from flask_session import Session
from base64 import b64encode
from io import BytesIO
from PIL import Image, ImageFilter
from helpers import apology
from os import path

# Setting up the flask application
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Defining global variables to store the required info
completed = False

# Defining a list containing the extensions which are valid
extensions = [".jpg", ".png", ".jpeg"]


# Defining a list to store the radius
radius = []


# Ensures that the cache is removeed
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Supporting both the methods for GET and POST
@app.route("/", methods=["GET", "POST"])
def main():

    # If the request method is POST
    if request.method == "POST":

        # Defining some global variables to store the input file name and output directory
        global input_file_name
        global output_directory

        # Getting the input file name and output directory
        input_file_name = request.form.get("file")
        output_directory = request.form.get("directory")

        # If the output directory does not exists
        if not path.exists(output_directory):

            # Return an apology message
            return apology("Directory does not exist")

        # If the image does not exists
        elif not path.exists(input_file_name):
            # Return an apology message
            return apology("Image does not exist")

        # If the input file name is not in valid extensions
        elif not path.splitext(input_file_name)[1] in extensions:

            # Return an apology message
            return apology("Invalid file found")

        # Else render the template for adjusting the image blur
        else:
            return redirect("/adjust")

    # Rendering the main template
    return render_template("index.html")


# Supporting both the request methods of GET and POST
@app.route("/adjust", methods=["GET", "POST"])
def adjust():

    # If the request method is POST
    if request.method == "POST":

        # Defining a global variable to store the blur values
        global typeBlur

        # Getting the blur type from the form
        typeBlur = request.form.get("typeBlur")

        # Getting the blur radius from the form
        distance = request.form.get("typeEdge")

        # If the blur type is overall
        if distance == "overall":

            # Get the overall blur raduis
            all = int(request.form.get("radius-overall"))

            # If the radius is less than zero
            if all < 0:

                # Redirect to an apology message
                return apology("Radius must not be zero")

            # Else
            else:

                # Clear all the previous values of blur values
                radius.clear()

                # For overall blur type, all the four values are same
                for i in range(4):

                    # Appending the blur value to the list
                    radius.append(all)

        # If the blur type is horizontal
        elif distance == "horizontal":

            # Getting the left blur radius
            left = int(request.form.get("radius-left-h"))

            # Getting the right blur radius
            right = int(request.form.get("radius-right-h"))

            # If any of the radius is less than zero
            if left < 0:

                # Return an apology message
                return apology("Left Radius must not be less than zero")

            elif right < 0:

                # Return an apology message
                return apology("Right Radius must not be less than zero")
            # Otherwise
            else:

                # Clear all the previous readings of the list
                radius.clear()

                # Append the required values to the list
                radius.append(0)
                radius.append(left)
                radius.append(0)
                radius.append(right)

        # If the blur type is vertical
        elif distance == "vertical":

            # Getting the top blur radius
            top = int(request.form.get("radius-top-v"))

            # Getting the bottom blur radius
            bottom = int(request.form.get("radius-bottom-v"))

            # If any of the radius is less than zero
            if top < 0:

                # Return an apology message
                return apology("Top Radius must not be zero")

            elif bottom < 0:

                # Return an apology message
                return apology("Bottom Radius must not be zero")

            # Otherwise
            else:

                # Clear all the previous readings in the list
                radius.clear()

                # Append the required values to the list
                radius.append(top)
                radius.append(0)
                radius.append(bottom)
                radius.append(0)

        # If the blur distance is custom
        elif distance == "custom":

            # Getting the top blur radius
            top = int(request.form.get("radius-top"))

            # Getting the left blur radius
            left = int(request.form.get("radius-left"))

            # Getting the bottom blur radius
            bottom = int(request.form.get("radius-bottom"))

            # Getting the right blur radius
            right = int(request.form.get("radius-right"))

            # Clearing all the previous blur values
            radius.clear()

            # Appending the required values
            radius.append(left)
            radius.append(top)
            radius.append(right)
            radius.append(bottom)

        # Defining a global variable to store the image
        global image

        # Calling the function to change the image
        image = changeImage()

        # Converting the image into base64
        buffered = BytesIO()

        # Saving the image
        image.save(buffered, format="PNG")

        # Encoding the image
        image_data = b64encode(buffered.getvalue()).decode("utf-8")

        # Rendering the required template with the image
        return render_template(
            "image.html",
            image_data=image_data,
            height=720,
            width=720,
        )

    # If the request method is GET
    else:

        # Rendering the template
        try:
            return render_template(
                "adjust.html",
                input=input_file_name,
                directory=output_directory,
            )

        # In case of a NameError, redirect to the main route
        except NameError:
            return redirect("/")


# Defining a function to process the image
def changeImage():

    # Opening the image in Pillow Image Object
    image = Image.open(input_file_name)

    # Getting the width and height
    width = image.width
    height = image.height

    # Calculate the center of the image (960 x 960)
    dx = 0 if width <= 960 else (width - 960) / 2
    dy = 0 if height <= 960 else (height - 960) / 2

    # Cropping the original image
    imagec = image.crop((dx, dy, width - dx, height - dy))

    # If the blur type is gaussian
    if typeBlur == "gaussian":

        # Apply the gaussian blur filter
        blurred_image = imagec.filter(filter=ImageFilter.GaussianBlur(32))

    # Otherwise
    else:

        # Apply Box Blur over the image
        blurred_image = imagec.filter(filter=ImageFilter.BoxBlur(32))

    # Cropping the cropped image with the required radius values
    cropped_image = imagec.crop(
        box=(radius[0], radius[1], imagec.width - radius[2], imagec.height - radius[3])
    )

    # Pasting the cropped image over the blurred image
    blurred_image.paste(cropped_image, (radius[0], radius[1]))

    # Return the blurred image
    return blurred_image


# Supporting only POST method
@app.route("/download", methods=["POST"])
def download():

    # Saving the image in the output directory
    image.save(f"{output_directory}/blurred_image{path.splitext(input_file_name)[1]}")

    # Rendering the required template
    return render_template("success.html")


# Running the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
