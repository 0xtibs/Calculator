import streamlit as st

# Prices for each drink
prices = {
    "RGB": 410,
    "PET": 420,
    "AMBO": 370
}

# UI for the application
def main():
    st.title("Truck Sale Calculator")

    # Input for number of drinks dispatched in the morning
    st.subheader("Drinks Dispatched to Trucks in Morning")
    rgb_a = st.number_input("RGB for Truck A", 0)
    pet_a = st.number_input("PET for Truck A", 0)
    ambo_a = st.number_input("AMBO for Truck A", 0)

    rgb_b = st.number_input("RGB for Truck B", 0)
    pet_b = st.number_input("PET for Truck B", 0)
    ambo_b = st.number_input("AMBO for Truck B", 0)

    rgb_c = st.number_input("RGB for Truck C", 0)
    pet_c = st.number_input("PET for Truck C", 0)
    ambo_c = st.number_input("AMBO for Truck C", 0)

    # Input for number of unsold drinks returned by each truck
    st.subheader("Unsold Drinks Returned by Trucks")
    rgb_a_r = st.number_input("Returned RGB for Truck A", 0)
    pet_a_r = st.number_input("Returned PET for Truck A", 0)
    ambo_a_r = st.number_input("Returned AMBO for Truck A", 0)

    rgb_b_r = st.number_input("Returned RGB for Truck B", 0)
    pet_b_r = st.number_input("Returned PET for Truck B", 0)
    ambo_b_r = st.number_input("Returned AMBO for Truck B", 0)

    rgb_c_r = st.number_input("Returned RGB for Truck C", 0)
    pet_c_r = st.number_input("Returned PET for Truck C", 0)
    ambo_c_r = st.number_input("Returned AMBO for Truck C", 0)

    # Calculate sold drinks and revenue for each truck
    sold_rgb_a = rgb_a - rgb_a_r
    sold_pet_a = pet_a - pet_a_r
    sold_ambo_a = ambo_a - ambo_a_r

    sold_rgb_b = rgb_b - rgb_b_r
    sold_pet_b = pet_b - pet_b_r
    sold_ambo_b = ambo_b - ambo_b_r

    sold_rgb_c = rgb_c - rgb_c_r
    sold_pet_c = pet_c - pet_c_r
    sold_ambo_c = ambo_c - ambo_c_r

    revenue_a = sold_rgb_a * prices["RGB"] + sold_pet_a * prices["PET"] + sold_ambo_a * prices["AMBO"]
    revenue_b = sold_rgb_b * prices["RGB"] + sold_pet_b * prices["PET"] + sold_ambo_b * prices["AMBO"]
    revenue_c = sold_rgb_c * prices["RGB"] + sold_pet_c * prices["PET"] + sold_ambo_c * prices["AMBO"]

    # Display the results
    st.subheader("Revenue from Sold Drinks")
    st.write(f"Truck A sold {sold_rgb_a} RGB, {sold_pet_a} PET, {sold_ambo_a} AMBO. Revenue: ${revenue_a}")
    st.write(f"Truck B sold {sold_rgb_b} RGB, {sold_pet_b} PET, {sold_ambo_b} AMBO. Revenue: ${revenue_b}")
    st.write(f"Truck C sold {sold_rgb_c} RGB, {sold_pet_c} PET, {sold_ambo_c} AMBO. Revenue: ${revenue_c}")

    total_revenue = revenue_a + revenue_b + revenue_c
    st.write(f"Total Revenue: ${total_revenue}")

if __name__ == "__main__":
    main()
