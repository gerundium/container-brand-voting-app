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
            <h3 style="color: white; text-align: left; font-size: 18px;">Version: 2.0</h3>
            <h3 style="color: white; text-align: left; font-size: 18px;">Hostname: """ + hostname + """</h3>
            <h3 style="color: white; text-align: left; font-size: 18px;">Current Time: """ + current_time + """</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Add space between text div and buttons
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if 'votes' not in st.session_state:
        st.session_state.votes = {"BMW": 0, "Mercedes": 0}
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("BMW", key="BMW", help="Vote for BMW", use_container_width=True):
            st.session_state.votes["BMW"] += 1
            st.success("You voted for BMW!")
    
    with col2:
        if st.button("Mercedes", key="Mercedes", help="Vote for Mercedes", use_container_width=True):
            st.session_state.votes["Mercedes"] += 1
            st.success("You voted for Mercedes!")
    
    st.write("## Voting Results:")
    st.write(f"BMW: {st.session_state.votes['BMW']} votes")
    st.write(f"Mercedes: {st.session_state.votes['Mercedes']} votes")

if __name__ == "__main__":
    voting_system()
