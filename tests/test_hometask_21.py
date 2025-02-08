import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_work_with_window(driver):

    driver.get("https://demoqa.com/browser-windows")
    main_window = driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR, "[id=tabButton]").click()
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])
    text2 = driver.find_element(By.ID, "sampleHeading")
    assert text2.text == "This is a sample page"
    driver.close()
    driver.switch_to.window(main_window)


def test_work_with_iframe(driver):

    driver.get("https://demoqa.com/frames")
    driver.switch_to.frame("frame1")
    text1 = driver.find_element(By.ID, "sampleHeading")
    assert text1.text == "This is a sample page"
    driver.switch_to.default_content()
    driver.switch_to.frame("frame2")
    text3 = driver.find_element(By.ID, "sampleHeading")
    assert text3.text == "This is a sample page"
    driver.switch_to.default_content()

    driver.quit()

def test_work_with_alert(driver):

    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.CSS_SELECTOR, "[id=alertButton]").click()
    alert1 = driver.switch_to.alert
    alert1.accept()

    confirm_button = driver.find_element(By.CSS_SELECTOR, "[id=confirmButton]")
    driver.execute_script("arguments[0].scrollIntoView();", confirm_button)
    confirm_button.click()
    alert2 = driver.switch_to.alert
    alert2.dismiss()
    text0 = driver.find_element(By.ID, "confirmResult")
    assert text0.text == "You selected Cancel"

    driver.find_element(By.ID, "promtButton").click()
    alert3 = driver.switch_to.alert
    alert3.send_keys("Selenium Test")
    alert3.accept()
    text4 = driver.find_element(By.ID, "promptResult")
    assert text4.text == "You entered Selenium Test"

    driver.quit()

def test_work_with_capabilities(driver):


    driver.get("https://www.google.com")
    text5 = driver.find_element(By.ID, "SIvCob")
    assert text5.text == "Сервисы Google доступны на этих языках: Беларуская"
    print("Открыта страница с русским интерфейсом.")



def test_with_actions(driver):

    driver.get("https://jqueryui.com/droppable")
    frame = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(frame)
    element_for_move = driver.find_element(By.ID, "draggable")
    element2 = driver.find_element(By.ID, "droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(element_for_move, element2).perform()

    assert "Dropped!" in element2.text
    print("Перетаскивание выполнено успешно!")

    driver.quit()


