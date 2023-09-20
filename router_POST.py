import openai
from fastapi import APIRouter, Depends, HTTPException

from validation import openai_api_key, validate_season

router = APIRouter()

openai.api_key = openai_api_key

"""
Generate travel recommendations for a given country and season.

Parameters:
- country (str): The name of the country for which recommendations are requested.
- season (str, optional): The season for which recommendations are requested.

Validation:
- Season has  a validation you can choose frm four given season. 

Returns:
- dict: A dictionary containing country, season, and a list of top 3 recommendations.

Raises:
- HTTPException: If no recommendations are available for the input.

Example usage:
- GET /travel-recommendations/?country=Italy&season=Summer

"""


@router.get("/travel-recommendations/")
async def travel_recommendations(
    country: str,
    season: str = Depends(validate_season),
):
    country = country.lower()
    prompt = f"Recommend list of only top 3 things to do in {country} during {season}."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )

    if not response.choices or not (response.choices[0] and response.choices[0].text):
        raise HTTPException(status_code=404, detail="No recommendations available for the given input.")

    recommendations_text = response.choices[0].text.strip()
    character_replace = str.maketrans({'1': None, '2': None, '3': None, '\n': None, })
    recommendations_text = recommendations_text.translate(character_replace)

    recommendations_list = [item.strip() for item in recommendations_text.split('.') if item.strip()]

    return {"country": country, "season": season, "recommendations": recommendations_list}


