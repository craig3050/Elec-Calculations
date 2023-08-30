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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("P=IV")
        voltage_options = {
            "230V": 230,
            "400V": 400,
            "3.3kV": 3300,
            "6.6kV": 6600,
            "11kV": 11000
        }
        selected_voltage_1 = st.radio("Select Voltage:", list(voltage_options.keys()), key=1)

        power_unit = st.radio("Select Power Unit:", ["Watts", "Kilowatts"])
        if power_unit == "Watts":
            power = int(st.number_input("Enter Power (Watts):", format="%.0f"))
        else:
            power = int(st.number_input("Enter Power (Kilowatts):", format="%.0f") * 1000)

        current = st.number_input("Enter Current (Amperes):")

        if st.button("Calculate"):
            selected_voltage_value = voltage_options[selected_voltage_1]
            power, voltage, current = power_voltage_current_conversion(power, selected_voltage_value, current)

            st.write(f"Calculated Voltage: {voltage} Volts")
            st.write(f"Calculated Current: {current} Amps")

    with col2:
        st.header("Fault Current Calculation")

        def calculate_fault_current(secondary_voltage_str, transformer_size, impedance):
            secondary_voltage = voltage_options[secondary_voltage_str]
            base_fault_current = (transformer_size * 1000) / (1.732 * secondary_voltage * (impedance / 100))
            return base_fault_current


        selected_voltage_2 = st.radio("Select Voltage:", list(voltage_options.keys()), key=2)
        transformer_size = st.number_input("Transformer Size (KVA)", format="%.0f")
        impedance = st.number_input("Transformer Impedance (%)")

        if st.button("Calculate Fault Current"):
            fault_current = calculate_fault_current(selected_voltage_2, transformer_size, impedance)
            fault_current = fault_current / 1000
            st.write(f"Base Fault Current: {fault_current:.2f} kA")


    with col3:
        st.header("Calculation 3")
        st.write("Result 3 content...")


if __name__ == "__main__":
    main()
