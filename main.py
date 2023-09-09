import streamlit as st

# Prices for each drink
prices = {
    "RGB": 410,
    "PET": 420,
    "AMBO": 370,
    "AMBO PET": 305,
    "AMBO FLAVOR": 365,
    "PREDATOR ENERGY": 435,
    "SUGAR FREE COCA": 312,
    "NOVIDA": 0,
}

# UI for the application
def main():
    st.title("Truck Sale Calculator")

    # Input for number of drinks dispatched in the morning
    st.subheader("Drinks Dispatched to Trucks in Morning")
    rgb_a = st.number_input("RGB for Truck A", 0)
    pet_a = st.number_input("PET for Truck A", 0)
    ambo_a = st.number_input("AMBO for Truck A", 0)
    ambo_pet_a = st.number_input("AMBO PET for Truck A", 0)
    ambo_flavor_a = st.number_input("AMBO FLAVOR for Truck A", 0)
    predator_energy_a = st.number_input("PREDATOR ENERGY for Truck A", 0)
    sugar_free_coca_a = st.number_input("SUGAR FREE COCA for Truck A", 0)
    novida_a = st.number_input("NOVIDA for Truck A", 0)
    print("*********************")
    rgb_b = st.number_input("RGB for Truck B", 0)
    pet_b = st.number_input("PET for Truck B", 0)
    ambo_b = st.number_input("AMBO for Truck B", 0)
    ambo_pet_b = st.number_input("AMBO PET for Truck B", 0)
    ambo_flavor_b = st.number_input("AMBO FLAVOR for Truck B", 0)
    predator_energy_b = st.number_input("PREDATOR ENERGY for Truck B", 0)
    sugar_free_coca_b = st.number_input("SUGAR FREE COCA for Truck B", 0)
    novida_b = st.number_input("NOVIDA for Truck B", 0)
    print("*********************")
    rgb_c = st.number_input("RGB for Truck C", 0)
    pet_c = st.number_input("PET for Truck C", 0)
    ambo_c = st.number_input("AMBO for Truck C", 0)
    ambo_pet_c = st.number_input("AMBO PET for Truck C", 0)
    ambo_flavor_c = st.number_input("AMBO FALVOR for Truck C", 0)
    predator_energy_c = st.number_input("PREDATOR ENERGY for Truck C", 0)
    sugar_free_coca_c = st.number_input("SUGAR FREE COCA for Truck C", 0)
    novida_c = st.number_input("NOVIDA for Truck C", 0)
    print("*********************")
    # Input for number of unsold drinks returned by each truck
    st.subheader("Unsold Drinks Returned by Trucks")
    rgb_a_r = st.number_input("Returned RGB for Truck A", 0)
    pet_a_r = st.number_input("Returned PET for Truck A", 0)
    ambo_a_r = st.number_input("Returned AMBO for Truck A", 0)
    ambo_pet_a_r = st.number_input("AMBO PET for Truck A", 0)
    ambo_flavor_a_r = st.number_input("AMBO FLAVOR for Truck A", 0)
    predator_energy_a_r = st.number_input("PREDATOR ENERGY for Truck A", 0)
    sugar_free_coca_a_r = st.number_input("SUGAR FREE COCA for Truck A", 0)
    novida_a_r = st.number_input("NOVIDA for Truck A", 0)
    print("---------------------")
    rgb_b_r = st.number_input("Returned RGB for Truck B", 0)
    pet_b_r = st.number_input("Returned PET for Truck B", 0)
    ambo_b_r = st.number_input("Returned AMBO for Truck B", 0)
    ambo_pet_b_r = st.number_input("AMBO PET for Truck B", 0)
    ambo_flavorb_b_r = st.number_input("AMBO FLAVOR for Truck B", 0)
    predator_energy_b_r = st.number_input("PREDATOR ENERGY for Truck B", 0)
    sugar_free_coca_b_r = st.number_input("SUGAR FREE COCA for Truck B", 0)
    novida_b_r = st.number_input("NOVIDA for Truck A", 0)
    print("---------------------")
    rgb_c_r = st.number_input("Returned RGB for Truck C", 0)
    pet_c_r = st.number_input("Returned PET for Truck C", 0)
    ambo_c_r = st.number_input("Returned AMBO for Truck C", 0)
    ambo_pet_c_r = st.number_input("AMBO PET for Truck C", 0)
    ambo_flavor_c_r = st.number_input("AMBO FLAVOR for Truck C", 0)
    predator_energy_c_r = st.number_input("PREDATOR ENERGY for Truck C", 0)
    sugar_free_coca_c_r = st.number_input("SUGAR FREE COCA for Truck C", 0)
    novida_c_r = st.number_input("NOVIDA for Truck C", 0)
    print("---------------------")
    # Calculate sold drinks and revenue for each truck
    sold_rgb_a = rgb_a - rgb_a_r
    sold_pet_a = pet_a - pet_a_r
    sold_ambo_a = ambo_a - ambo_a_r
    sold_ambo_pet_a = ambo_pet_a - ambo_pet_a_r
    sold_ambo_flavor_a = ambo_flavor_a - ambo_flavor_a_r
    sold_predator_energy_a = predator_energy_a - predator_energy_a_r
    sold_sugar_free_coca_a = sugar_free_coca_a - sugar_free_coca_a_r
    sold_novida_a = novida_a - novida_a_r

    sold_rgb_b = rgb_b - rgb_b_r
    sold_pet_b = pet_b - pet_b_r
    sold_ambo_b = ambo_b - ambo_b_r
    sold_ambo_pet_b = ambo_pet_b - ambo_pet_b_r
    sold_ambo_flavor_b = ambo_flavor_b - ambo_flavorb_b_r
    sold_predator_energy_b = predator_energy_b - predator_energy_b_r
    sold_sugar_free_coca_b = sugar_free_coca_b - sugar_free_coca_b_r
    sold_novida_b = novida_b - novida_b_r

    sold_rgb_c = rgb_c - rgb_c_r
    sold_pet_c = pet_c - pet_c_r
    sold_ambo_c = ambo_c - ambo_c_r
    sold_ambo_pet_c = ambo_pet_c - ambo_pet_c_r
    sold_ambo_flavor_c = ambo_flavor_c - ambo_flavor_c_r
    sold_predator_energy_c = predator_energy_c - predator_energy_c_r
    sold_sugar_free_coca_c = sugar_free_coca_c - sugar_free_coca_c_r
    sold_novida_c = novida_c - novida_c_r

    revenue_a = (sold_rgb_a * prices["RGB"] + sold_pet_a * prices["PET"] + sold_ambo_a * prices["AMBO"] +
            sold_ambo_pet_a * prices["AMBO PET"] + sold_ambo_flavor_a * prices["AMBO FLAVOR"] +
            sold_predator_energy_a * prices["PREDATOR ENERGY"] + sold_sugar_free_coca_a * prices["SUGAR FREE COCA"] +
            sold_novida_a * prices["NOVIDA"])

    revenue_b = (sold_rgb_b * prices["RGB"] + sold_pet_b * prices["PET"] + sold_ambo_b * prices["AMBO"] +
            sold_ambo_pet_b * prices["AMBO PET"] + sold_ambo_flavor_b * prices["AMBO FLAVOR"] +
            sold_predator_energy_b * prices["PREDATOR ENERGY"] + sold_sugar_free_coca_b * prices["SUGAR FREE COCA"] +
            sold_novida_b * prices["NOVIDA"])

    revenue_c = (sold_rgb_c * prices["RGB"] + sold_pet_c * prices["PET"] + sold_ambo_c * prices["AMBO"] +
            sold_ambo_pet_c * prices["AMBO PET"] + sold_ambo_flavor_c * prices["AMBO FLAVOR"] +
            sold_predator_energy_c * prices["PREDATOR ENERGY"] + sold_sugar_free_coca_c * prices["SUGAR FREE COCA"] +
            sold_novida_c * prices["NOVIDA"])

# Display the results
    st.subheader("Revenue from Sold Drinks")
    st.write(f"Truck A Revenue: ${revenue_a}")
    st.write(f"Truck B Revenue: ${revenue_b}")
    st.write(f"Truck C Revenue: ${revenue_c}")

    total_revenue = revenue_a + revenue_b + revenue_c
    st.write(f"Total Revenue: ${total_revenue}")

main()
