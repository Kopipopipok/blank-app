import streamlit as st
import instaloader
import re

st.set_page_config(page_title="Analisa Sosmed", layout="centered")
st.title("📱 Analisa Sosmed - Instagram Engagement Rate")

st.markdown("Masukkan URL postingan Instagram publik untuk menghitung engagement rate.")

# Input URL
url = st.text_input("🔗 Masukkan URL Postingan Instagram", placeholder="https://www.instagram.com/p/XXXXX/")

# Fungsi ambil shortcode dari URL
def extract_shortcode(insta_url):
    match = re.search(r"/p/([^/]+)/", insta_url)
    return match.group(1) if match else None

# Fungsi ambil data dari Instaloader
def get_instagram_data(shortcode):
    try:
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        likes = post.likes
        comments = post.comments
        owner = post.owner_username
        profile = instaloader.Profile.from_username(L.context, owner)
        followers = profile.followers
        caption = post.caption
        image_url = post.url

        return {
            "likes": likes,
            "comments": comments,
            "followers": followers,
            "username": owner,
            "caption": caption,
            "image_url": image_url
        }

    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")
        return None

# Tombol Analisis
if st.button("🔍 Analisa"):
    shortcode = extract_shortcode(url)
    if shortcode:
        data = get_instagram_data(shortcode)
        if data:
            st.image(data['image_url'], caption=f"Posting oleh @{data['username']}", use_column_width=True)
            st.markdown(f"**Caption**: {data['caption'][:200]}...")

            # Hitung Engagement Rate
            if data['followers'] > 0:
                engagement_rate = ((data['likes'] + data['comments']) / data['followers']) * 100
            else:
                engagement_rate = 0

            st.metric("❤️ Jumlah Like", f"{data['likes']}")
            st.metric("💬 Jumlah Komentar", f"{data['comments']}")
            st.metric("👥 Jumlah Follower", f"{data['followers']}")
            st.metric("🔥 Engagement Rate", f"{engagement_rate:.2f}%")
    else:
        st.warning("URL tidak valid. Pastikan format URL sesuai dengan 'https://www.instagram.com/p/XXXXX/'")
