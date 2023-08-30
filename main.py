import streamlit as st


def power_voltage_current_conversion(power, voltage, current):
    if power and voltage:
        current = power / voltage
    elif power and current:
        voltage = power / current
    elif voltage and current:
        power = voltage * current
    return power, voltage, current


def main():
    st.title("Electrical Calculations")

    voltage_options = {
        "230V": 230,
        "400V": 400,
        "3.3kV": 3300,
        "6.6kV": 6600,
        "11kV": 11000
    }

    selected_voltage = st.radio("Select Voltage:", list(voltage_options.keys()))

    power_unit = st.radio("Select Power Unit:", ["Watts", "Kilowatts"])
    if power_unit == "Watts":
        power = int(st.number_input("Enter Power (Watts):", format="%.0f"))
    else:
        power = int(st.number_input("Enter Power (Kilowatts):", format="%.0f") * 1000)

    current = st.number_input("Enter Current (Amperes):")

    if st.button("Calculate"):
        selected_voltage_value = voltage_options[selected_voltage]
        power, voltage, current = power_voltage_current_conversion(power, selected_voltage_value, current)

        st.write(f"Calculated Voltage: {voltage} Volts")
        st.write(f"Calculated Current: {current} Amperes")
        st.write(f"Calculated Power: {power} Watts")


if __name__ == "__main__":
    main()
