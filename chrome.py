from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()

chrome.get("https://www.google.com")


def pesquisa_facebook():
    campo_busca = chrome.find_element_by_class_name("gLFyf")
    campo_busca.send_keys("facebook")
    campo_busca.send_keys(Keys.ENTER)

def seleciona_facebook():
    facebook = chrome.find_element_by_class_name("LC20lb")
    facebook.click()

def login_facebook(email, senha):
    email_face = chrome.find_element_by_id("email")
    senha_face = chrome.find_element_by_id("pass")
    entrar_face = chrome.find_element_by_class_name("login_form_login_button")
    email_face.send_keys(email)
    senha_face.send_keys(senha)
    entrar_face.click()

if __name__ == "__main__":
    pesquisa_facebook()
    seleciona_facebook()
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    login_facebook(email, senha)
    



