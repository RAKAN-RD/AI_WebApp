import streamlit as st


class Main_Menu:

    def __init__(self):
        # self.title = st.title('SSH', help=None)
        # self.input = st.text_input(label='Username')
        self.login_page()
    
    def login(self, username, password):
        if username == 'admin' and password == 'password123':
            return True
        else:
            return False

    def login_page(self):
        st.title("Login")

        self.username = st.text_input("Username")
        self.password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if self.login(self.username, self.password):
                st.success("Login berhasil!")
                st.write(f"Selamat datang, {self.username}!")
                self.username = ''
            else:
                st.error("Username atau password salah. Coba lagi.")

    

# Main_Menu()
