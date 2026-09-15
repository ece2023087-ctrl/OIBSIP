# BMI Calculator

A simple and user-friendly **BMI (Body Mass Index) Calculator** built with **Python and Tkinter**. The application allows users to enter their weight and height using different units and calculates their BMI, BMI category, and suggested healthy weight range.

## Features

* Calculate BMI using weight and height.
* Supports **kilograms (kg)** and **pounds (lbs)** for weight.
* Supports **meters** and **inches** for height.
* Automatically converts units when required.
* Displays BMI up to two decimal places.
* Determines BMI category:

  * Underweight
  * Normal weight
  * Overweight
  * Obese
* Dynamically changes the result area's background and text colors according to the BMI category.
* Displays a suggested weight range based on a BMI of 18.5–24.9.
* Includes input validation and error messages for invalid values.
* Clean graphical interface using Tkinter and ttk.

## Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **ttk** – Styled Tkinter widgets

## BMI Categories

| BMI Range      | Category      |
| -------------- | ------------- |
| Below 18.5     | Underweight   |
| 18.5 – 24.89   | Normal weight |
| 24.9 – 29.89   | Overweight    |
| 29.9 and above | Obese         |

> **Note:** BMI is a general screening measure and does not account for factors such as muscle mass, age, or body composition.

## How It Works

The application uses the standard BMI formula:

```text
BMI = Weight (kg) / Height² (m²)
```

For example, if a person weighs **58 kg** and is **1.67 meters** tall:

```text
BMI = 58 / (1.67²)
BMI ≈ 20.80
```

The application then identifies the corresponding BMI category and displays the result.

## Unit Conversion

### Weight

If the user selects pounds:

```text
kg = lbs × 0.45359237
```

### Height

If the user selects inches:

```text
meters = inches × 0.0254
```

If meters are entered as a value greater than 3.0, the program assumes the value was entered in centimeters and converts it to meters.

## Suggested Weight Range

The application calculates the suggested weight range using the BMI values **18.5** and **24.9**:

```text
Minimum weight = 18.5 × height²
Maximum weight = 24.9 × height²
```

The result is displayed in kilograms.

## Requirements

Make sure Python 3 is installed on your computer.

Tkinter is included with most standard Python installations.

You can check your Python installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bmi-calculator.git
```

### 2. Navigate to the project directory

```bash
cd bmi-calculator
```

### 3. Run the application

```bash
python bmi_calculator.py
```

On some systems, you may need:

```bash
python3 bmi_calculator.py
```

## Project Structure

```text
bmi-calculator/
│
├── bmi_calculator.py
└── README.md
```

## Usage

1. Enter your weight.
2. Select the weight unit (`kg` or `lbs`).
3. Enter your height.
4. Select the height unit (`meters` or `inches`).
5. Click **Calculate**.
6. The application displays:

   * BMI
   * BMI category
   * Suggested weight range
   * Suggested height range

## Error Handling

The application handles invalid input using popup error messages.

For example:

* Empty input
* Non-numeric values
* Zero or negative height
* Zero or negative weight

An appropriate error message is displayed instead of allowing the program to calculate an invalid BMI.

## Screenshots

You can add a screenshot of the application here:

```markdown
![BMI Calculator Screenshot](screenshot.png)
```

Place your screenshot file in the project directory and name it `screenshot.png`.

## Future Improvements

Possible improvements include:

* Add a reset/clear button.
* Make the suggested height range dynamic based on the entered weight.
* Add a BMI scale or progress bar.
* Improve the UI with custom themes.
* Add age and gender information.
* Store previous BMI calculations.
* Add dark mode.
* Package the application as a Windows `.exe` file.
* Add more detailed health information for each BMI category.

## Disclaimer

This BMI calculator is intended for **educational and informational purposes only**. BMI is a general screening tool and should not be considered a medical diagnosis. For health-related decisions, consult a qualified healthcare professional.

## License

This project is open source and available under the **MIT License**.
