# How to Run: streamlit run your_script.py
import streamlit as st


def main():

    st.set_page_config(page_title="음성 챗봇", page_icon="🎙️", layout="wide")

    # 제목
    st.header("음성 챗봇 프로그램")


    # 구분선
    st.markdown("---")

    # 기본 설명
    with st.expander("음성 챗봇 프로그램에 관하여", expanded = True):
        st.write(
            """
            - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
            - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
            - 답변은 OpenAI의 GPT 모델을 활용합니다. 
            - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
        """)
        
        st.markdown("")


    st.write("음성 챗봇 프로그램을 사용하시려면 아래의 버튼을 눌러주세요.")

    if st.button("음성 챗봇 시작"):
        st.write("음성 챗봇이 시작되었습니다.")

        # STT
        st.write("음성을 입력해주세요.")
        stt_result = st.text_input("음성 입력")
        st.write(f"음성 입력: {stt_result}")

        # TTS
        tts_result = st.text_input("챗봇 응답")
        st.write(f"챗봇 응답: {tts_result}")

        if st.button("음성 챗봇 종료"):
            st.write("음성 챗봇이 종료되었습니다.")

    st.write("음성 챗봇 프로그램을 종료하시려면 아래의 버튼을 눌러주세요.")



# 실행 함수
if __name__ == "__main__":
    print(__name__, "실행")
    main()