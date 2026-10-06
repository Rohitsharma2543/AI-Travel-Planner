
import streamlit as st
import requests as r

st.title("AI TRAVEL PLANNER")

st.subheader("Enter all trip data")


st.markdown("""
<style>

div.stButton > button {
    width:100%;
    background-color: blue;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: light grey;
    color: blue;
    border: 1px solid blue;
}

div.stButton > button:active {
    background-color: green;
    color: white;
}

div.stButton > button:focus {
    background-color: green;
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)


starting_loc = st.text_input("Enter Starting Location")

destination_loc = st.text_input("Enter Destination Location")

no_of_trip_days = st.number_input(
    "Enter Trip Days",
    min_value=1,
    step=1
)

no_of_people = st.number_input(
    "Enter People Count",
    min_value=1,
    step=1
)

budget = st.number_input(
    "Enter budget",
    min_value=10000,
    max_value=100000,
    step=10000
)

specifications = st.text_area(
    "Enter Your specifications",
    placeholder="Example: party places, temples etc.."
)

# btn = st.button("Build Travelling Plan")
btn = st.button("Build Travelling Plan", width="stretch")

if btn:
    payload={
        "starting_loc":starting_loc,
        "destination_loc":destination_loc,
        "no_of_trip_days":no_of_trip_days,
        "no_of_people":no_of_people,
        "budget":budget,
        "specifications":specifications
    }
    # r.post("http://127.0.0.1:8000/plan_trip",json=payload)
    # be_res=r.post("http://127.0.0.1:8000/plan_trip",json=payload)
    be_res = r.post("https://ai-travel-planner-6nq4.onrender.com/plan_trip", json=payload)
    if be_res.status_code == 200:
        st.write(be_res.json()["content"])








# # line 1
# # pip install streamlit
# # py -m pip install streamlit
# # python -m pip install streamlit

# # line 6 (To run front_end Program)
# # cd front_end
# # streamlit run app.py

# # py -m streamlit run app.py
# # python -m streamlit run app.py

# # line 16
# # pip install requests
# # py -m pip install requests
# # python -m pip install requests

# # requests module ---> methods
# # r.post()
# # r.get()
# # r.put()
# # r.delete()

# # To run back_end Program 
# # cd back_end
# # uvicorn main:f_obj --reload
























# import streamlit as st
# import requests as r

# st.title("AI TRAVEL PLANNER")

# st.subheader("Enter all trip data")

# starting_loc=st.text_input("Enter Starting Location")
# destination_loc=st.text_input("Enter Destination Location")
# no_of_trip_days=st.number_input("Enter Trip Days",min_value=1,step=1)
# no_of_people=st.number_input("Enter People Count",min_value=1,step=1)
# budget=st.number_input("Enter budget",min_value=10000,max_value=100000,step=10000)
# specifications=st.text_area("Enter Your specifications",placeholder="Example: party places, temples etc..")
# btn=st.button("Build Travelling Plan")

# if btn:
#     payload={
#         "starting_loc":starting_loc,
#         "destination_loc":destination_loc,
#         "no_of_trip_days":no_of_trip_days,
#         "no_of_people":no_of_people,
#         "budget":budget,
#         "specifications":specifications
#     }
#     # r.post("http://127.0.0.1:8000/plan_trip",json=payload)
#     be_res=r.post("http://127.0.0.1:8000/plan_trip",json=payload)
#     if be_res.status_code == 200:
#         st.write(be_res.json()["content"])

