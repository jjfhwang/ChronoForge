# ChronoForge: Your Pythonic Temporal Toolkit

ChronoForge is a Python library designed to simplify and enhance the management and manipulation of time-based data and operations. This toolkit provides a suite of functions and classes for parsing, validating, formatting, and calculating dates and times with precision and ease. It goes beyond standard Python datetime functionality to offer advanced features for handling timezones, recurring events, and temporal arithmetic, making it ideal for applications dealing with scheduling, logging, data analysis, and any domain requiring robust temporal handling.

ChronoForge addresses the common challenges developers face when working with time-related data. The standard Python datetime library, while powerful, can be cumbersome for certain tasks, particularly when dealing with complex scenarios like timezone conversions and recurring events. ChronoForge streamlines these operations by providing intuitive functions and classes that abstract away much of the underlying complexity. This allows developers to focus on their core application logic rather than wrestling with the intricacies of time manipulation. Furthermore, the library emphasizes clarity and readability, making your code easier to understand and maintain.

With ChronoForge, you can easily parse dates and times from various formats, validate their correctness, and format them according to your specific needs. The library also provides tools for calculating time differences, adding or subtracting time intervals, and determining the occurrence of recurring events. This functionality is crucial for applications that require precise scheduling, event management, or data analysis based on temporal patterns. By leveraging ChronoForge, you can significantly reduce development time and ensure the accuracy and reliability of your time-sensitive operations. Its robust error handling and comprehensive documentation further contribute to a smooth and efficient development experience.

ChronoForge isn't just about simplifying common tasks; it also offers advanced features that are often lacking in standard libraries. The library's timezone support is particularly noteworthy, allowing you to seamlessly convert between different timezones and handle daylight saving time transitions with confidence. Its recurring event functionality enables you to define complex event schedules and easily determine the dates and times of future occurrences. These advanced features make ChronoForge a valuable asset for developers building sophisticated applications that require precise and reliable temporal management.

## Key Features

*   **Flexible Date and Time Parsing:** Uses `datetime.strptime` under the hood but wraps it with custom error handling and allows for user-defined formats. Supports a wide variety of common date and time string formats and can be extended to handle custom formats. Implemented via the `parse_datetime(date_string, format_string=None)` function. If no `format_string` is provided, it attempts to infer the format based on common patterns.
*   **Robust Timezone Handling:** Leverages the `pytz` library to provide comprehensive timezone support. Allows for easy conversion between timezones using the `convert_timezone(datetime_object, target_timezone)` function. The function automatically handles daylight saving time transitions.
*   **Precise Time Interval Calculations:** Provides functions for calculating the difference between two datetimes with microsecond precision. The `calculate_time_difference(start_datetime, end_datetime)` function returns a `timedelta` object representing the time difference.
*   **Recurring Event Management:** Implements a flexible system for defining recurring events using the `dateutil.rrule` library. Allows for specifying recurrence rules based on frequency, interval, and other criteria. The `generate_recurring_events(start_date, recurrence_rule, number_of_events)` function returns a list of datetimes representing the occurrences of the event.
*   **Date and Time Formatting:** Offers a wide range of formatting options using `datetime.strftime`. Provides a set of predefined format strings for common use cases, as well as the ability to define custom formats. The `format_datetime(datetime_object, format_string)` function returns a string representation of the datetime object in the specified format.
*   **Validation of Date and Time Inputs:** Incorporates functions to validate the correctness of date and time inputs, ensuring that they fall within acceptable ranges and adhere to specified formats. The `validate_datetime(date_string, format_string=None)` function raises a `ValueError` if the input is invalid.
*   **Temporal Arithmetic:** Offers functions for adding or subtracting time intervals from datetimes. The `add_time_interval(datetime_object, timedelta_object)` and `subtract_time_interval(datetime_object, timedelta_object)` functions return a new datetime object with the specified time interval added or subtracted.

## Technology Stack

*   **Python 3.7+:** The core programming language used for the project.
*   **`datetime`:** Python's built-in module for working with dates and times. ChronoForge extends and enhances the functionality of this module.
*   **`pytz`:** A Python library for handling timezones. Used for accurate timezone conversions and daylight saving time management.
*   **`dateutil`:** A powerful Python library providing extensions to the standard `datetime` module, particularly useful for working with recurring events via `rrule`.
*   **`typing`:** Used for type hinting to improve code readability and maintainability.

## Installation

1.  **Clone the repository:**
    git clone https://github.com/jjfhwang/ChronoForge.git

2.  **Navigate to the project directory:**
    cd ChronoForge

3.  **Create a virtual environment (recommended):**
    python3 -m venv venv
    source venv/bin/activate (or venv\Scripts\activate on Windows)

4.  **Install the required dependencies:**
    pip install -r requirements.txt

## Configuration

ChronoForge relies on environment variables for certain configurations. These variables can be set in your `.env` file or directly in your shell environment.

*   `CHRONOFORGE_DEFAULT_TIMEZONE`: Sets the default timezone for the application. If not set, it defaults to UTC. Example: `CHRONOFORGE_DEFAULT_TIMEZONE=America/Los_Angeles`

These variables are accessed within the code using the `os` module:

import os

default_timezone = os.environ.get("CHRONOFORGE_DEFAULT_TIMEZONE", "UTC")

## Usage

Example 1: Parsing a datetime string

from chronoforge import parse_datetime

date_string = "2023-10-27 10:00:00"
datetime_object = parse_datetime(date_string)
print(datetime_object) # Output: 2023-10-27 10:00:00

Example 2: Converting timezone

from chronoforge import convert_timezone
import datetime

datetime_object = datetime.datetime.now()
target_timezone = "America/New_York"
converted_datetime = convert_timezone(datetime_object, target_timezone)
print(converted_datetime)

Example 3: Generating recurring events

from chronoforge import generate_recurring_events
import datetime
from dateutil import rrule

start_date = datetime.datetime(2023, 10, 27)
recurrence_rule = rrule.rrule(rrule.WEEKLY, count=5, dtstart=start_date)
events = generate_recurring_events(start_date, recurrence_rule, 5)

for event in events:
  print(event)

## Contributing

We welcome contributions to ChronoForge! To contribute, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes and write tests to ensure their correctness.
4.  Submit a pull request with a clear description of your changes.
5.  Ensure your code adheres to PEP 8 style guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/ChronoForge/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the developers of `datetime`, `pytz`, and `dateutil` for their invaluable contributions to the Python ecosystem.