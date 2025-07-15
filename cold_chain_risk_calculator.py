import streamlit as st
import random

# Page config
st.set_page_config(page_title="Smart Cold Chain Risk Calculator", layout="centered")
st.title("🧊 Smart Cold Chain Risk Calculator")
st.markdown("""
Use this tool to evaluate shipment risk for temperature-sensitive products based on packaging type, transit time, location, and seasonal variation.
""")

# --- Input Section ---
st.header("📦 Shipment Details")
product_type = st.selectbox("Product Type", ["Vaccines", "Biologics", "Specimens", "Reagents", "Other"])
temp_range = st.selectbox("Required Temperature Range (°C)", ["2–8°C", "-20°C", "-80°C", "Room Temp"])
origin = st.text_input("Origin (City, Country)", "Lagos, Nigeria")
destination = st.text_input("Destination (City, Country)", "London, UK")
transit_time = st.slider("Transit Time (hours)", 1, 168, 24)
packaging = st.selectbox("Packaging Type", ["Passive (ice packs)", "Active (refrigerated)", "Dry Ice"])
carrier = st.selectbox("Carrier Type", ["Air", "Ground", "Sea"])
month = st.selectbox("Shipping Month", ["January", "April", "July", "October"])

# --- Risk Calculation Logic ---
def calculate_risks(temp_range, packaging, transit_time, origin, destination):
    # Temperature Risk Logic
    base_temp_risk = {
        "Room Temp": 10,
        "2–8°C": 40,
        "-20°C": 30,
        "-80°C": 20
    }.get(temp_range, 40)

    if "Passive" in packaging:
        base_temp_risk += 25
    elif "Dry Ice" in packaging and temp_range != "-80°C":
        base_temp_risk += 15

    # Transit Risk Logic
    transit_risk = min(100, (transit_time / 48) * 50 + (25 if carrier != "Air" else 0))

    # Region Risk Heuristics
    high_risk_regions = ["Nigeria", "India", "Kenya"]
    region_risk = 15
    for loc in [origin, destination]:
        if any(r in loc for r in high_risk_regions):
            region_risk = 35
            break

    # Weighted Overall Risk
    overall_risk = round(base_temp_risk * 0.4 + transit_risk * 0.3 + region_risk * 0.3, 2)

    return int(base_temp_risk), int(transit_risk), int(region_risk), overall_risk

# --- Output Section ---
if st.button("🔍 Calculate Risk"):
    temp_risk, transit_risk, region_risk, overall_risk = calculate_risks(
        temp_range, packaging, transit_time, origin, destination
    )

    st.header("📊 Risk Results")
    st.metric("Temperature Risk", f"{temp_risk} / 100")
    st.metric("Transit Risk", f"{transit_risk} / 100")
    st.metric("Region Risk", f"{region_risk} / 100")
    st.metric("Overall Risk Score", f"{overall_risk} / 100")

    # --- Recommendations ---
    st.subheader("🛠 Recommendations")
    if overall_risk > 75:
        st.warning("**High Risk** – Consider using active cooling or reducing transit time.")
    elif overall_risk > 50:
        st.info("**Moderate Risk** – Monitor shipment, review packaging, and routing.")
    else:
        st.success("**Low Risk** – Shipment setup appears stable.")

    st.markdown("---")
    st.caption("Built for smarter healthcare logistics by TOBI HealthOps AI.")

