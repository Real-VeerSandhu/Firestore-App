import streamlit as st
from google.cloud import firestore, storage
from database import database_info

st.title('Firestore Post App')

sr, db = database_info()

title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

if title and url and submit:
	doc_ref = db.collection("posts").document(title)
	doc_ref.set({
		"title": title,
		"url": url
	})

posts_ref = db.collection("posts")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]('https://+'{url})")

def test_db():
	return 'Database Accessed', type(db)

def run_set(key)
	return type(key), 12