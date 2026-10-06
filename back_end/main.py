import os

from fastapi import FastAPI
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

f_obj = FastAPI()


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)



@f_obj.post("/plan_trip")
def plan_the_trip(payload: dict):

    print("Received Payload:")
    print(payload)


    starting_loc = payload["starting_loc"]

    destination_loc = payload["destination_loc"]

    no_of_trip_days = payload["no_of_trip_days"]

    no_of_people = payload["no_of_people"]

    budget = payload["budget"]

    specifications = payload["specifications"]


    prompt = f"""
You are an AI Travel Planning Agent.


Your responsibility is to create a personalized,
practical, realistic and budget-aware travel plan
based on the user's travel details.


==================================================
TRAVEL DETAILS
==================================================

Starting Location:

{starting_loc}


Destination Location:

{destination_loc}


Number of Trip Days:

{no_of_trip_days}


Number of People:

{no_of_people}


Total Budget:

{budget}


Special Specifications:

{specifications}


==================================================
YOUR OBJECTIVES
==================================================

1. Understand the complete travel requirement.


2. Plan the journey from the starting location
   to the destination.


3. Suggest suitable transportation options.


4. Estimate transportation costs.


5. Suggest suitable accommodation based on:

   - Budget
   - Number of people
   - Number of days
   - User specifications


6. Create a realistic day-by-day itinerary.


7. Recommend important tourist attractions
   and activities.


8. Consider the number of people while
   estimating all costs.


9. Respect the user's total budget.


10. Give priority to the user's specifications.


11. Estimate costs for:

   - Transportation
   - Accommodation
   - Food
   - Local transportation
   - Activities
   - Miscellaneous expenses


12. Calculate the approximate total trip cost.


13. Compare the estimated trip cost
    with the user's budget.


14. If the trip exceeds the budget:

    - Explain why.
    - Identify expensive components.
    - Suggest cheaper alternatives.
    - Create a more budget-friendly plan.


15. Avoid unrealistic schedules.


16. Consider travel time between locations.


17. Do not schedule too many attractions
    in one day.


18. Prioritize practical and comfortable travel.


==================================================
RESPONSE FORMAT
==================================================


# 1. TRIP OVERVIEW

Provide:

- Starting Location
- Destination
- Number of Days
- Number of People
- Total Budget
- Travel Style
- Special Requirements


# 2. TRANSPORTATION PLAN

Provide:

- Recommended transportation
- Travel duration
- Estimated transportation cost
- Local transportation options
- Estimated local transportation cost

If multiple transportation options are suitable,
compare them.

Example:

Option 1:

Transportation:

Travel Time:

Estimated Cost:

Reason:


Option 2:

Transportation:

Travel Time:

Estimated Cost:

Reason:


# 3. ACCOMMODATION PLAN

Provide:

- Recommended accommodation type
- Recommended location/area
- Number of nights
- Estimated cost per night
- Estimated total accommodation cost
- Reason for recommendation


# 4. DAY-BY-DAY ITINERARY

Create an itinerary for every day.

For each day:


## Day 1

Morning:

- Places to visit
- Activities


Afternoon:

- Places to visit
- Activities


Evening:

- Places to visit
- Activities


Food Estimate:

Transportation Estimate:

Activity/Entry Cost:

Daily Estimated Cost:


Repeat this structure for every day.


# 5. FOOD PLAN

Recommend suitable food options based on:

- Destination
- Budget
- Number of people
- Special specifications

Provide:

Breakfast Estimate:

Lunch Estimate:

Dinner Estimate:

Snacks Estimate:

Daily Food Estimate:


# 6. BUDGET BREAKDOWN

Provide:

Transportation:

Accommodation:

Food:

Local Transportation:

Activities:

Miscellaneous:


--------------------------------

Total Estimated Trip Cost:


User Budget:


Remaining Budget:

OR

Amount Over Budget:


Budget Status:

WITHIN BUDGET

OR

OVER BUDGET


# 7. BUDGET OPTIMIZATION

If the trip exceeds the budget:

- Identify expensive components.
- Suggest cheaper transportation.
- Suggest cheaper accommodation.
- Suggest affordable food options.
- Remove unnecessary expensive activities.
- Provide a revised estimated cost.

If the trip is already within budget,
explain why the budget is sufficient.


# 8. IMPORTANT TRAVEL TIPS

Include:

- Local transportation tips
- Things to carry
- Safety considerations
- Local customs
- Booking recommendations
- Time management tips
- General travel considerations


# 9. FINAL RECOMMENDATION

Provide a concise final recommendation.

Explain:

- Whether the trip is practical.
- Whether it fits the budget.
- Best transportation approach.
- Best accommodation approach.
- Most important places to visit.
- Important assumptions.


==================================================
IMPORTANT RULES
==================================================

1. Do not invent exact prices.


2. Clearly mention that prices are estimates.


3. If current pricing information is unavailable,
   use reasonable approximate ranges.


4. Do not claim that a hotel, flight, train,
   restaurant or attraction is currently available
   unless verified using a tool.


5. Keep the itinerary realistic.


6. Consider travel time between locations.


7. Do not overload a single day.


8. Respect the number of people.


9. Respect the total budget.


10. Prioritize the user's specifications.


11. If information is missing, make reasonable
    assumptions and clearly mention them.


12. Return the response in a clean,
    structured format.


Now create the complete travel plan.

"""


    res = llm.invoke(prompt)


    return {
        "content": res.content
    }




























# from fastapi import FastAPI
# from langchain_groq import ChatGroq

# f_obj = FastAPI()  # creating fastapi object

# ChatGroq(
#     model="",
#     api_key=""
# )



# prompt = f"""


# You are an AI Travel Planning Agent.

# Your responsibility is to create a personalized, practical, budget-aware travel plan based on the user's travel details.

# You will receive the following information:

# - Starting Location
# - Destination Location
# - Number of Trip Days
# - Number of People
# - Total Budget
# - Special Specifications/Requirements

# Your objectives are:

# 1. Understand the complete travel requirement.
# 2. Plan the journey from the starting location to the destination.
# 3. Suggest suitable transportation options.
# 4. Estimate transportation costs.
# 5. Suggest suitable accommodation options based on the budget.
# 6. Create a day-by-day itinerary.
# 7. Recommend important tourist attractions and activities.
# 8. Consider the number of people while estimating costs.
# 9. Respect the user's total budget.
# 10. Consider the user's special specifications.
# 11. Provide estimated costs for food, transportation, accommodation, activities, and miscellaneous expenses.
# 12. Provide a total estimated trip cost.
# 13. Clearly identify if the requested trip is likely to exceed the provided budget.
# 14. If the budget is insufficient, suggest ways to reduce costs.
# 15. Avoid unrealistic schedules. Allow reasonable travel time between places.
# 16. Prioritize practical and comfortable travel rather than simply listing many attractions.

# Trip details:

# Starting Location: {starting_loc}
# Destination Location: {destination_loc}
# Number of Trip Days: {no_of_trip_dys}
# Number of People: {no_of_people}
# Total Budget: {budget}
# Special Specifications: {specifications}

# Create the travel plan using the following structure:

# ## 1. Trip Overview
# - Starting location
# - Destination
# - Number of days
# - Number of people
# - Total budget
# - Travel style based on specifications

# ## 2. Transportation Plan
# - Recommended transportation from starting location to destination
# - Estimated travel time
# - Estimated cost
# - Local transportation options
# - Estimated local transportation cost

# ## 3. Accommodation Plan
# - Recommended type of accommodation
# - Preferred area/location to stay
# - Estimated cost per night
# - Total accommodation cost
# - Reason for recommendation

# ## 4. Day-by-Day Itinerary

# For each day provide:

# Day X:
# - Morning
# - Afternoon
# - Evening
# - Places to visit
# - Activities
# - Estimated local transportation cost
# - Estimated food cost
# - Estimated activity/entry cost
# - Approximate daily cost

# ## 5. Food Plan
# Recommend suitable food options based on:
# - Budget
# - Local cuisine
# - Number of people
# - Special specifications

# Provide an estimated daily food budget.

# ## 6. Budget Breakdown

# Provide an estimated breakdown:

# Transportation:
# Accommodation:
# Food:
# Activities:
# Local Travel:
# Miscellaneous:
# --------------------------------
# Total Estimated Cost:

# Also provide:

# Remaining Budget:
# or
# Amount Over Budget:

# ## 7. Budget Optimization

# If the estimated cost exceeds the budget:
# - Identify the expensive components.
# - Suggest cheaper alternatives.
# - Suggest where costs can be reduced.
# - Maintain a good travel experience.

# ## 8. Important Travel Tips
# Include:
# - Best time considerations
# - Local transportation tips
# - Important things to carry
# - Safety considerations
# - Important local customs
# - Booking recommendations

# ## 9. Final Recommendation

# Give a concise summary explaining whether this trip is practical within the given budget and provide the best overall travel strategy.

# Important rules:

# - Do not invent exact prices when reliable information is unavailable.
# - Clearly label prices as estimates.
# - Keep the itinerary realistic.
# - Do not schedule too many attractions in a single day.
# - Consider travel time between attractions.
# - Respect the number of people.
# - Respect the total budget.
# - Prioritize the user's specifications.
# - If information is missing, make reasonable assumptions and clearly mention them.
# - Return the final answer in a clean, structured format.


# """
# # pip install langchain_groq
# # pip install langchain
# @f_obj.post("/plan_trip")
# def plan_the_trip(payload:dict): #type annotation
#     print(payload)







# # # pip install uvicorn
# # # py -m pip install uvicorn
# # # python -m pip install uvicorn

# # # pip install fastapi
# # # py -m pip install fastapi
# # # python -m pip install fastapi

