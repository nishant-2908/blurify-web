# blurify-web
## Flask Implementation of [blurifypy-cli](https://www.github.com/nishant-2908/bluifypy-cli)

## Table of Contents
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
It is a Flask app which helps user to add blurred edges to the photo.
It runs on the localhost server, which renders the HTML pages according to the routes.
It needs the input image location and the output image directory location.
It then needs the type of blur, the distance from each side of the image to be blurred (in px).
It supports four modes:
- Overall
- Horizontal
- Vertical
- Custom
It crops the image to 960x960 if bigger than that
It then applies the required filters and the algorithms for bluring the edges of the photo.
It then previews the photo and if good enough, it can be too downloaded.

## Installation
Downloading the repository
```bash
git clone https://www.github.com/nishant-2908/blurify-web.git
```

## Usage
Running the app
```bash
python main.py
```

Navigate to `http://127.0.0.1:5000` on your browser. Or directly [Click here](http://127.0.0.1:5000)

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
Feel free to customize this README.md file to provide more specific details about your project.
Let me know if there's anything else I can help you with!
