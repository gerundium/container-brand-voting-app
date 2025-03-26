import socket
import datetime
import streamlit as st

def get_system_info():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return hostname, current_time

# Streamlit UI
def voting_system():
    st.title("Gerundium Brand Voting System")
    hostname, current_time = get_system_info()
    
    # Display version, hostname, and current time in a dark grey background
    st.markdown("""
        <div style="background-color: #2f2f2f; padding: 20px; border-radius: 10px;">
            <h3 style="color: white; text-align: left; font-size: 24px;">Version: 1</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Hostname: """ + hostname + """</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Current Time: """ + current_time + """</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Add space between text div and buttons
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if 'votes' not in st.session_state:
        st.session_state.votes = {"Adidas": 0, "Nike": 0}
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Adidas", key="Adidas", help="Vote for Adidas", use_container_width=True):
            st.session_state.votes["Adidas"] += 1
            st.success("You voted for Adidas!")
    
    with col2:
        if st.button("Nike", key="Nike", help="Vote for Nike", use_container_width=True):
            st.session_state.votes["Nike"] += 1
            st.success("You voted for Nike!")
    
    st.write("## Voting Results:")
    st.write(f"Adidas: {st.session_state.votes['Adidas']} votes")
    st.write(f"Nike: {st.session_state.votes['Nike']} votes")

if __name__ == "__main__":
    voting_system()
