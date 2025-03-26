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
Marvel_VOTES = get_or_create_counter("Marvel_votes", "Number of votes for Marvel")
DC_VOTES = get_or_create_counter("DC_votes", "Number of votes for DC")

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
            <h3 style="color: white; text-align: left; font-size: 24px;">Version: 4</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Hostname: """ + hostname + """</h3>
            <h3 style="color: white; text-align: left; font-size: 20px;">Current Time: """ + current_time + """</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if 'votes' not in st.session_state:
        st.session_state.votes = {"Marvel": 0, "DC": 0}
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Marvel", key="Marvel", help="Vote for Marvel", use_container_width=True):
            st.session_state.votes["Marvel"] += 1
            Marvel_VOTES.inc()
            st.success("You voted for Marvel!")
    
    with col2:
        if st.button("DC", key="DC", help="Vote for DC", use_container_width=True):
            st.session_state.votes["DC"] += 1
            DC_VOTES.inc()
            st.success("You voted for DC!")
    
    st.write("## Voting Results:")
    st.write(f"Marvel: {st.session_state.votes['Marvel']} votes")
    st.write(f"DC: {st.session_state.votes['DC']} votes")

if __name__ == "__main__":
    voting_system()
