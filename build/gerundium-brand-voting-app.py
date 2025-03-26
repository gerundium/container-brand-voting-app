import socket
import datetime
import streamlit as st

def get_system_info():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return hostname, current_time

# Streamlit UI
def voting_system():
    st.title("Gerunium Brand Voting System")
    hostname, current_time = get_system_info()
    
    # Display version, hostname, and current time in a dark grey background
    st.markdown("""
        <div style="background-color: #2f2f2f; padding: 20px; border-radius: 10px;">
            <h3 style="color: white; text-align: left; font-size: 18px;">Version: 3</h3>
            <h3 style="color: white; text-align: left; font-size: 18px;">Hostname: """ + hostname + """</h3>
            <h3 style="color: white; text-align: left; font-size: 18px;">Current Time: """ + current_time + """</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Add space between text div and buttons
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if 'votes' not in st.session_state:
        st.session_state.votes = {"Coke": 0, "Pepsi": 0}
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Coke", key="Coke", help="Vote for Coke", use_container_width=True):
            st.session_state.votes["Coke"] += 1
            st.success("You voted for Coke!")
    
    with col2:
        if st.button("Pepsi", key="Pepsi", help="Vote for Pepsi", use_container_width=True):
            st.session_state.votes["Pepsi"] += 1
            st.success("You voted for Pepsi!")
    
    st.write("## Voting Results:")
    st.write(f"Coke: {st.session_state.votes['Coke']} votes")
    st.write(f"Pepsi: {st.session_state.votes['Pepsi']} votes")

if __name__ == "__main__":
    voting_system()
