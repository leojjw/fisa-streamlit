import streamlit as st

ani_list = ['짱구는못말려', '몬스터', '릭앤모티']
img_list = [
    'https://i.imgur.com/t2ewhfH.png', 
    'https://i.imgur.com/ECROFMC.png', 
    'https://i.imgur.com/MDKQoDc.jpg'
]


search_query = st.text_input("애니메이션 이름을 검색하세요:")

if search_query:
    results = [img_list[i] for i, ani in enumerate(ani_list) if search_query in ani]
    if results:
        for img_url in results:
            st.image(img_url, use_container_width =True)
    else:
        st.error(f"'{search_query}'와 일치하는 항목이 없습니다.")