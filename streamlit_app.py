import streamlit as st

st.title("📊 Instagram Engagement Rate Analyzer")

st.markdown("Masukkan data dari 1 postingan Instagram")

likes = st.number_input("❤️ Jumlah Like", min_value=0)
comments = st.number_input("💬 Jumlah Komentar", min_value=0)
followers = st.number_input("👥 Jumlah Follower Akun", min_value=1)

if st.button("Hitung Engagement Rate"):
    like_rate = (likes / followers) * 100
    comment_rate = (comments / followers) * 100
    engagement_rate = ((likes + comments) / followers) * 100

    st.metric("📈 Like Rate (%)", f"{like_rate:.2f}%")
    st.metric("💬 Comment Rate (%)", f"{comment_rate:.2f}%")
    st.metric("🔥 Engagement Rate Total (%)", f"{engagement_rate:.2f}%")
