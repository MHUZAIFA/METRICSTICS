# METRICSTICS: Your Statistical Calculator 📊

Welcome to METRICSTICS, a Python-based statistical calculator with a sleek Tkinter GUI. METRICSTICS not only computes standard statistical measures but also provides an intuitive interface for loading and storing session information. It features a beautiful dark theme, ensuring a pleasant user experience.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

METRICSTICS helps in calculating descriptive statistics.

The purpose of descriptive statistics is to quantitatively describe a collection of data by measures of central tendency, measures of frequency, and measures of variability.

Let x be a random variable that can take values from a finite data set x1, x2, x3, ..., xn, with each value having the same probability.

1. The minimum, m, is the smallest of the values in the given data set. (m need not be unique.)

2. The maximum, M, is the largest of the values in the given data set. (M need not be unique.)

3. The mode, o, is the value that appears most frequently in the given data set. (o need not be unique.)

4. The median, d, is the middle number if n is odd, and is the arithmetic mean of the two middle numbers if n is even.

5. Mean (μ):
   μ = (1/n) * Σ(xi), where i ranges from 1 to n.

6. Mean Absolute Deviation (MAD):
   MAD = (1/n) * Σ |xi - μ|, where i ranges from 1 to n.

7. Standard Deviation (σ):
   σ = sqrt((1/n) * Σ(xi - μ)^2), where i ranges from 1 to n.


## Features

- Calculate statistics: min, max, mean, median, mode, mad, and standard deviation.
- User-friendly GUI built with Tkinter.
- A sleek dark theme for a modern and comfortable user experience.
- Input data through keyboard, file upload, or the interactive randomizer button.
- Convenient session management – store and load your statistical sessions effortlessly.
- Follows the Model-View-Controller (MVC) design pattern for a clean and modular code structure.

## Screenshots

![Screenshot 1](screenshots/metricstics_gui_keyboard.png)
*METRICSTICS GUI - Keyboard*



![Screenshot 2](screenshots/metricstics_gui_file.png)
*METRICSTICS GUI - File upload*



![Screenshot 3](screenshots/metricstics_gui_auto.png)
*METRICSTICS GUI - Auto (Randomizer)*

## Getting Started

### Prerequisites

Make sure you have Python 3.11.5 installed on your system. If not, download and install it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/metricstics.git
```
2. Navigate to the project directory:
```bash
cd metricstics
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the following command to start METRICSTICS:
```bash
python main.py
```

## Contributors

Thank you to the following contributors for their valuable contributions to the project:

- [Huzaifa Anjum](https://github.com/huzaifafcrit)
- [Anagha Harinath](https://github.com/Anagha630)
- [Srikar Hasthi](https://github.com/SrikarHasthi)
- [Sameer Kamble](https://github.com/sameer1130)
- [Madiha Itrat](https://github.com/MadihaMehdi)

Your efforts are greatly appreciated! 🙌

## Contributing

We welcome contributions! If you would like to contribute to METRICSTICS, please read our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- A big thanks to the Python community and the Tkinter team for making METRICSTICS possible.
- Special thanks to Professor [Mr. Pankaj Kamthan](kamthan@gmail.com) for guidance and support.