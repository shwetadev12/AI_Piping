import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestTravelRecommendationsEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch('router_POST.openai.Completion.create')
    def test_travel_recommendations(self, mock_openai_completion):
        mock_openai_completion.return_value.choices[0].text = "1. Visit the Eiffel Tower. 2. Try French cuisine."

        response = self.client.get("/travel-recommendations/?country=France&season=summer&no_of_recommendations=2")
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "country": "france",
            "season": "summer",
            "recommendations": ["Visit the Eiffel Tower", "Try French cuisine"]
        }
        self.assertEqual(response.json(), expected_response)

    def test_travel_recommendations_invalid_season(self):
        response = self.client.get("/travel-recommendations/?country=France&season=invalid&no_of_recommendations=2")
        self.assertEqual(response.status_code, 400) 
        expected_response = {"detail": "Please choose from given seasons"}  
        self.assertEqual(response.json(), expected_response)


if __name__ == '__main__':
    unittest.main()
