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
# Weather App 🌤️

A simple desktop **Weather Application** built with **Python, Tkinter, and OpenWeatherMap API**. The application allows users to search for a city, select it from autocomplete suggestions, and view its current weather information.

## Features

* 🌍 Search for cities from a predefined city list.
* 🔎 Real-time city autocomplete suggestions.
* 🌡️ Displays temperature in:

  * Celsius (°C)
  * Fahrenheit (°F)
* 💧 Displays humidity.
* ☁️ Displays current weather condition.
* 💨 Displays wind speed.
* 📊 Displays atmospheric pressure.
* 🌎 Displays the city and country code.
* ⚠️ Handles API and data-format errors.
* 🖥️ Simple and lightweight Tkinter graphical interface.

## Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **ttk** – Combobox widget
* **Requests** – HTTP/API requests
* **OpenWeatherMap API** – Weather data

## How It Works

The application uses the OpenWeatherMap current weather API to retrieve weather information for the selected city.

The user enters a city name into the search box. As they type, matching cities from the predefined list are displayed in a listbox.

After selecting a city, the user clicks **Get Weather**. The application sends a request to the OpenWeatherMap API and displays the returned weather information.

## Weather Information

The application displays:

| Information       | Description                      |
| ----------------- | -------------------------------- |
| City              | Selected city and country code   |
| Temperature       | Current temperature in °C and °F |
| Humidity          | Relative humidity percentage     |
| Weather Condition | Current weather description      |
| Wind Speed        | Wind speed in meters per second  |
| Pressure          | Atmospheric pressure in hPa      |

## Temperature Conversion

OpenWeatherMap returns temperature in **Kelvin** in this application.

### Kelvin to Celsius

```text
Celsius = Kelvin - 273.15
```

### Kelvin to Fahrenheit

```text
Fahrenheit = (Kelvin - 273.15) × 9/5 + 32
```

## Requirements

Make sure **Python 3** is installed.

Install the required `requests` package:

```bash
pip install requests
```

On some systems:

```bash
pip3 install requests
```

Tkinter is normally included with Python. On some Linux distributions, you may need to install it separately.

## API Key

This project uses the **OpenWeatherMap API**.

You need an API key to retrieve weather data.

Create an account on OpenWeatherMap and obtain your API key.

Then store the key in your Python program:

```python
api_key = "YOUR_API_KEY"
```

### ⚠️ Security Note

**Do not upload your actual API key to GitHub.**

Instead, use an environment variable.

For example:

```python
import os

api_key = os.getenv("OPENWEATHER_API_KEY")
```

Then configure the environment variable on your computer.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
```

### 2. Enter the project directory

```bash
cd weather-app
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Add your API key

Set your OpenWeatherMap API key using an environment variable or configure it locally in the Python file.

### 5. Run the application

```bash
python weather_app.py
```

On some systems:

```bash
python3 weather_app.py
```

## Project Structure

```text
weather-app/
│
├── weather_app.py
├── README.md
└── .gitignore
```

## Usage

1. Launch the application.
2. Click inside the city search box.
3. Start typing a city name.
4. Matching cities will appear below the search box.
5. Select the desired city.
6. Click **Get Weather**.
7. The current weather information will appear in the application.

### Example Output

```text
City: Chennai, IN
Temperature: 30.45 °C / 86.81 °F
Humidity: 72%
Weather Condition: scattered clouds
Wind Speed: 4.12 m/s
Pressure: 1008 hPa
```

The actual values will change according to the current weather conditions.

## Error Handling

The application handles common API-related errors using Python's `requests` exception handling.

If the API request fails, an error message is displayed:

```text
Error: ...
```

The application also handles unexpected API response formats:

```text
Error: Data format incorrect, please try again.
```

## Autocomplete Search

The application provides a simple autocomplete feature.

When the user types a city name, the program searches the predefined `cities` list:

```python
matches = [city for city in cities if value.lower() in city.lower()]
```

Matching cities are then displayed in the listbox.

For example, entering:

```text
chen
```

can display:

```text
Chennai
```

## Future Improvements

Some possible improvements for future versions:

* 📍 Automatically detect the user's location.
* 🗺️ Add interactive maps.
* 📅 Add a 5-day weather forecast.
* 🌙 Add dark mode.
* 🎨 Improve the graphical interface.
* 🌡️ Allow users to switch between Celsius and Fahrenheit.
* 🔄 Add a refresh button.
* 🕐 Display sunrise and sunset times.
* 🌧️ Add weather icons.
* 💾 Save recently searched cities.
* 🔐 Store the API key securely using environment variables.
* 📱 Create a responsive or mobile version.

## Security

Never commit your API key directly to a public GitHub repository.

A `.gitignore` file can be used to prevent local configuration files from being uploaded:

```text
.env
__pycache__/
*.pyc
```

If you use a `.env` file, you can store your API key like this:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

## Screenshot

Add a screenshot of your application to the repository and include it in the README:

```markdown
![Weather App Screenshot](screenshot.png)
```

## Disclaimer

Weather information is provided through the OpenWeatherMap API. Weather conditions and measurements may change frequently, and the application should not be considered a source for emergency weather information.

## License

This project is open source and available under the **MIT License**.

# Random Password Generator 🔐

A simple desktop **Random Password Generator** built using **Python and Tkinter**. The application allows users to choose a password length and select different character types to generate a random password.

## Features

* 🔢 Set a custom password length.
* 🔠 Include uppercase letters.
* 🔡 Include lowercase letters.
* 🔢 Include digits.
* 🔣 Symbol selection option in the interface.
* 🎲 Generate a random password.
* 👁️ Password is hidden by default for privacy.
* 📋 Copy the generated password to the clipboard.
* ⚠️ Displays error messages for invalid input.
* ✨ Includes button hover effects.
* 💚 Includes a pulsating animation on the Generate Password button.
* 🖥️ Simple and lightweight graphical interface.

## Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **string** – Provides predefined character sets.
* **random** – Generates random password characters.

## How It Works

The user enters the desired password length and selects one or more character sets.

The application builds a character pool based on the selected options:

```python
character_set = ""

if uppercase_var.get():
    character_set += string.ascii_uppercase

if lowercase_var.get():
    character_set += string.ascii_lowercase

if digits_var.get():
    character_set += string.digits
```

A password is then generated by randomly selecting characters from the available character pool.

```python
password = ''.join(
    random.choice(character_set) for _ in range(length)
)
```

The generated password is displayed in the password field.

## Character Sets

The application currently supports:

| Character Type | Python Character Set |
| -------------- | -------------------- |
| Uppercase      | `A-Z`                |
| Lowercase      | `a-z`                |
| Digits         | `0-9`                |
| Symbols        | UI option included   |

### Important Note

The current version includes a **Symbols** checkbox in the interface, but the `generate_password()` function does not yet add `string.punctuation` when that checkbox is selected.

To enable symbols, add:

```python
if symbols_var.get():
    character_set += string.punctuation
```

## Requirements

You only need **Python 3**.

Tkinter is included with most standard Python installations.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external Python packages are required.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-generator.git
```

### 2. Navigate to the project directory

```bash
cd password-generator
```

### 3. Run the application

```bash
python password_generator.py
```

On some systems:

```bash
python3 password_generator.py
```

## Usage

1. Enter the desired password length.
2. Select the character types you want to include.
3. Click **Generate Password**.
4. The generated password will appear in the password field.
5. Click **Copy Password** to copy it to the clipboard.

### Example

For a password length of:

```text
12
```

With:

```text
✓ Uppercase
✓ Lowercase
✓ Digits
```

The application might generate:

```text
G7kP2mX9qL4a
```

Every generated password will be different because characters are selected randomly.

## Input Validation

The application checks whether the password length is valid.

If the user enters a value less than or equal to zero, an error message is displayed:

```text
Please enter a valid password length.
```

The application also checks whether at least one character set has been selected.

If no character set is selected:

```text
Please select at least one character set.
```

## Copy Password

The **Copy Password** button allows users to copy the generated password.

If there is no password available, the application displays:

```text
No password to copy.
```

Otherwise, a confirmation message is shown after the copy operation.

## User Interface

The application contains:

* Password length input
* Uppercase checkbox
* Lowercase checkbox
* Digits checkbox
* Symbols checkbox
* Generate Password button
* Password display field
* Copy Password button

The interface also includes hover effects that change the button colors when the mouse enters or leaves the buttons.

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## Security Considerations

This application is useful for generating random passwords, but the current implementation uses Python's `random` module.

For passwords intended for **real security-sensitive use**, it is better to use Python's `secrets` module because it is designed for cryptographically secure random values.

For example:

```python
import secrets

password = ''.join(
    secrets.choice(character_set)
    for _ in range(length)
)
```

## Future Improvements

Possible improvements include:

* 🔣 Fully enable symbol generation.
* 🔒 Use the `secrets` module for stronger password generation.
* 📊 Add a password strength indicator.
* 👁️ Add a show/hide password button.
* 📋 Improve clipboard handling.
* 🔄 Add a reset button.
* 📏 Add minimum and maximum password length limits.
* 🎨 Add dark mode.
* 💾 Allow users to save generated passwords securely.
* 🛡️ Add options for avoiding ambiguous characters such as `O`, `0`, `l`, and `1`.

## Screenshot

You can add a screenshot of the application to your repository:

```markdown
![Random Password Generator](screenshot.png)
```

Place the screenshot in the project directory as:

```text
screenshot.png
```

## Disclaimer

This project is intended for **educational purposes**. For highly sensitive accounts, use a reputable password manager or a cryptographically secure password-generation method.

## License

This project is open source and available under the **MIT License**.


