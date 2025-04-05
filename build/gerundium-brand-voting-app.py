import socket
import datetime
import streamlit as st
from prometheus_client import Counter, start_http_server, REGISTRY
import threading

def get_system_info():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return hostname, current_time

# Function to get or create a Prometheus metric safely
def get_or_create_counter(name, description):
    if name not in REGISTRY._names_to_collectors:
        return Counter(name, description)
    return REGISTRY._names_to_collectors[name]

# Initialize Prometheus metrics
Playstation_VOTES = get_or_create_counter("Playstation_votes", "Number of votes for Playstation")
XBOX_VOTES = get_or_create_counter("XBOX_votes", "Number of votes for XBOX")

# Start Prometheus metrics server only once
def start_metrics_server():
    try:
        start_http_server(9090)
    except OSError:
        print("Cannot start metrics server")
        pass  # Ignore error if server is already running

if 'metrics_server_started' not in st.session_state:
    threading.Thread(target=start_metrics_server, daemon=True).start()
    st.session_state.metrics_server_started = True

def voting_system():
    st.title("Gerundium Brand Voting System")
    hostname, current_time = get_system_info()
    
    st.markdown("""
        <div style="background-color: #2f2f2f; padding: 20px; border-radius: 10px;">
            <h3 style="color: white; text-align: left; font-size: 24px;">Version: 5</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Hostname: """ + hostname + """</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Current Time: """ + current_time + """</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if 'votes' not in st.session_state:
        st.session_state.votes = {"Playstation": 0, "XBOX": 0}
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Playstation", key="Playstation", help="Vote for Playstation", use_container_width=True):
            st.session_state.votes["Playstation"] += 1
            Playstation_VOTES.inc()
            st.success("You voted for Playstation!")
    
    with col2:
        if st.button("XBOX", key="XBOX", help="Vote for XBOX", use_container_width=True):
            st.session_state.votes["XBOX"] += 1
            XBOX_VOTES.inc()
            st.success("You voted for XBOX!")
    
    st.write("## Voting Results:")
    st.write(f"Playstation: {st.session_state.votes['Playstation']} votes")
    st.write(f"XBOX: {st.session_state.votes['XBOX']} votes")

if __name__ == "__main__":
    voting_system()
