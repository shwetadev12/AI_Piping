# Travel Recommendation App and API

## Travel Recommendation App (Frontend)

### Description
This is a React-based web application that allows users to get travel recommendations based on the selected country and season. It uses an external API to fetch travel recommendations and displays them to the user.

### Installation
To run this project, follow these steps:

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/shewtadev12/travel-recommendation-app.git
   ```

2. Navigate to the project directory:
   ```shell
   cd TRAVEL_RECOMMENDATION_APP/app
   ```

3. Install the required dependencies:
   ```shell
   npm install
   ```

4. Start the development server:
   ```shell
   npm start
   ```

5. Open your web browser and go to [http://localhost:3000](http://localhost:3000) to use the app.

### Usage
1. Enter the name of the country you want to travel to in the "Country" input field.
2. Select the season you are planning to travel in from the "Season" dropdown.
3. Click the "Search" button to fetch travel recommendations.
4. The recommendations will be displayed below.

### Contributing
If you'd like to contribute to this project, please follow these guidelines:
- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Make your changes and test them thoroughly.
- Submit a pull request to the main repository with a clear description of your changes.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
This project uses the following external libraries and tools:
- [React](https://reactjs.org/)
- [Material-UI](https://mui.com/)
- [TravelAppAPI](https://github.com/shewtadev12/travel-app-api)

---

## Travel Recommendation API (Backend)

### Description
This is a FastAPI-based web API that provides travel recommendations based on the selected country and season. It utilizes the OpenAI API to generate travel recommendations and returns them to the user in a structured format.

### Prerequisites
Before running this API, make sure you have the following set up:

- Python installed on your system (Python 3.7 or higher).
- Required Python packages installed. You can install them using pip:
  ```shell
  pip install fastapi uvicorn httpx python-dotenv openai
  ```

### Getting Started
1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/shewtadev12/travel-recommendation-api.git
   ```

2. Navigate to the project directory:
   ```shell
   cd TRAVEL_RECOMMENDATION_API
   ```

3. Create a `.env` file in the project root directory and add your OpenAI API key like this:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   OR

   Copy the content from  `.env.example` and replace the text with your API key.

4. Start the API server using `uvicorn`:
   ```shell
   uvicorn main:app --reload
   ```

5. The API will be accessible at [http://localhost:3000](http://localhost:3000).

### API Endpoints

#### Get Travel Recommendations
- **Endpoint**: `/travel-recommendations`
- **Method**: GET
- **Parameters**:
  - `country` (string): The name of the country you want to travel to.
  - `season` (string): The season for which you want travel recommendations (Options: 'Summer', 'Winter', 'Spring', 'Autumn').

#### Example Request
```http
GET /travel-recommendations?country=italy&season=summer
```

#### Example Response
```json
{
  "country": "italy",
  "season": "summer",
  "recommendations": [
    "Explore historic landmarks like the Colosseum.",
    "Indulge in authentic Italian cuisine at local restaurants.",
    "Relax on the beautiful beaches of the Amalfi Coast."
  ]
}
```

### CORS Configuration
This API is configured to allow cross-origin requests, making it accessible from different domains. You can adjust the CORS settings in the `main.py` file to restrict or expand access as needed.

### Contributing
If you'd like to contribute to this project, please follow these guidelines:
- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Make your changes and test them thoroughly.
- Submit a pull request to the main repository with a clear description of your changes.

### Test Cases
To run test cases: pytest test.py

### Contact
If you have any questions or feedback, feel free to contact the project owner:

- Shewta Verma shewtadevvermaa4@gmail.com
