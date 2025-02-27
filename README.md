# Flight Deals

The Flight Deals project is a Python-based application designed to help users find and monitor the best flight deals. It automates the process of searching for flights and notifies users when prices drop or when deals match their specified criteria.

## Features

- **Automated Flight Search**: Regularly searches for flights based on user-defined destinations and criteria.
- **Price Monitoring**: Tracks flight prices and identifies significant drops or deals.
- **User Notifications**: Sends alerts to users via email or SMS when matching deals are found.

## Project Structure

The project consists of the following modules:

- `data_manager.py`: Handles data storage and retrieval, managing user preferences and destination data.
- `flight_data.py`: Structures the flight data retrieved from the API, organizing it for easy access and manipulation.
- `flight_search.py`: Contains functions to interact with flight search APIs, performing searches based on user criteria.
- `notification_manager.py`: Manages the notification system, sending alerts to users when deals are found.
- `main.py`: The main script that ties all modules together and initiates the flight search and notification process.

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/amanuel496/flight-deals.git
   ```

2. **Install Dependencies**:

   Navigate to the project directory and install the required packages:

   ```bash
   cd flight-deals
   pip install -r requirements.txt
   ```

3. **Configure API Keys and Environment Variables**:

   Create a `.env` file in the project root directory and add your API keys and other environment variables:

   ```env
   FLIGHT_API_KEY=your_flight_api_key
   NOTIFICATION_SERVICE_API_KEY=your_notification_service_api_key
   # Add other necessary configurations
   ```

4. **Run the Application**:

   Execute the main script to start the flight deals tracker:

   ```bash
   python main.py
   ```

## Usage

- **Adding Destinations**: Update the `data_manager.py` module to include the destinations you want to monitor.
- **Setting Price Thresholds**: Define the price limits for each destination to receive notifications when deals fall within your budget.
- **Receiving Notifications**: Ensure your notification preferences are set up in the `notification_manager.py` module to receive alerts via your chosen method (email or SMS).

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

*Note: Ensure you have the necessary API access and adhere to the terms and conditions of the flight data providers and notification services used in this project.*

