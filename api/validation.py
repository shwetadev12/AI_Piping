from decouple import config
from fastapi import HTTPException, Query
from const import seasons

openai_api_key = config('OPENAI_API_KEY')



def validate_season(season: str = Query(..., description="Please choose from these options:'Summer', 'Winter', 'Spring', 'Autumn')"),
):
    seasons
    if season.lower() not in seasons:
        raise HTTPException(status_code=400, detail="Please choose from given seasons")
    return season