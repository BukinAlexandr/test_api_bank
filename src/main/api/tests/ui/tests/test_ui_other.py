from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_text_box(page):

    page.goto("https://demoqa.com/text-box")
    page.fill('#userName', 'Анна Ивановна')
    page.fill("input[placeholder='name@example.com']", 'anna@test.com')
    page.fill("textarea#currentAddress", 'Москва, ул. Радожская, 1')
    page.fill('#permanentAddress', 'Москва, ул. 64 Армии, 6')
    page.get_by_role("button", name="Submit").click()
    page.click('text=Submit')



def test_check_box(page):

    page.goto("https://demoqa.com/checkbox")

    for i in range(5):
        closed = page.locator(".rc-tree-switcher.rc-tree-switcher_close")
        if closed.count() > 0:
            closed.first.click()
            page.wait_for_timeout(300)
        else:
            break

    page.locator("span[aria-label='Select Desktop']").click()
    page.locator("span[aria-label='Select Documents']").click()
    page.locator("span[aria-label='Select Downloads']").click()

    result = page.locator("#result").inner_text()

    assert "home" in result


def test_radio_button(page):

    page.goto("https://demoqa.com/radio-button")

    yes_radio = page.locator("#yesRadio")
    impressive_radio = page.locator("#impressiveRadio")
    no_radio = page.locator("#noRadio")

    expect(yes_radio).to_be_visible()
    expect(impressive_radio).to_be_visible()
    expect(no_radio).to_be_visible()

    yes_radio.click()
    expect(yes_radio).to_be_checked()
    expect(page.locator(".text-success")).to_have_text("Yes")


    impressive_radio.click()
    expect(impressive_radio).to_be_checked()
    expect(page.locator(".text-success")).to_have_text("Impressive")

    expect(no_radio).to_be_disabled()

def test_click(page):
    page.goto("https://demoqa.com/buttons")

    dbl_click = page.locator("#doubleClickBtn")
    right_click = page.locator("#rightClickBtn")
    one_click = page.get_by_text("Click Me", exact=True)

    dbl_click.dblclick()
    right_click.click(button="right")
    one_click.click()

    expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")
    expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")

def test_download_file(page, tmp_path):
    page.goto("https://demoqa.com/upload-download")

    file_path = tmp_path / "demoqa_test_file.txt"
    file_path.write_text("Hello, this is a test file for DemoQA upload!")

    page.set_input_files("#uploadFile", str(file_path))

    uploaded_file_name = page.locator("#uploadedFilePath")
    assert file_path.name in uploaded_file_name.inner_text()

def test_dynamic_element(page):
    page.goto("https://demoqa.com/dynamic-properties")

    dynamic_btn = page.locator("#visibleAfter")
    expect(dynamic_btn).to_be_visible(timeout=6000)
    dynamic_btn.click()
    enable_btn = page.locator("#enableAfter")
    expect(enable_btn).to_be_enabled(timeout=6000)
    enable_btn.click()

def test_simple_alert(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "You clicked a button"
        dialog.accept()

    page.once("dialog", handle_alert)
    page.locator("#alertButton").click()

def test_five_seconds_alert(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "This alert appeared after 5 seconds"
        dialog.accept()

    page.once("dialog", handle_alert)

    five_sec_alert = page.locator("#timerAlertButton")
    five_sec_alert.click()

    page.wait_for_event("dialog", timeout=6000)

def test_confirm_alert(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "Do you confirm action?"
        assert dialog.type == "confirm"
        dialog.dismiss()

    page.once("dialog", handle_alert)
    page.locator("#confirmButton").click()

def test_prompt_alert(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "Please enter your name"
        dialog.accept("DemoQA")

    page.once("dialog", handle_alert)
    page.locator("#promtButton").click()

    output = page.locator("#promptResult").inner_text()
    assert "DemoQA" in output

def test_date_picker_select_option(page):
    page.goto("https://demoqa.com/date-picker")

    date_input = page.locator("#datePickerMonthYearInput")
    date_input.click()

    page.locator(".react-datepicker__month-select").select_option("7")
    page.locator(".react-datepicker__year-select").select_option("2025")
    page.locator(".react-datepicker__day--025").click()

    assert date_input.input_value() == "08/25/2025"


def test_date_picker_option(page):
    page.goto("https://demoqa.com/date-picker")

    date_input = page.locator("#dateAndTimePickerInput")
    date_input.click()

    page.locator(".react-datepicker__month-read-view").click()
    page.locator(".react-datepicker__month-option >> text=August").click()
    page.locator(".react-datepicker__day--025").click()
    page.locator(".react-datepicker__time-list").select_option("01:00")


def test_practice_form(page, tmp_path):
    page.goto("https://demoqa.com/automation-practice-form")

    page.fill("#firstName", "Alexandr")
    page.fill("#lastName", "Bukin")
    page.fill("#userEmail", "goose1337@goose.com")
    page.get_by_role("radio", name="Male", exact=True).click()
    page.fill("#userNumber", "79312875432")
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").select_option("11")
    page.locator(".react-datepicker__year-select").select_option("1997")
    page.get_by_role("gridcell", name="Choose Tuesday, December 30th").click()
    page.locator("#subjectsContainer div").nth(1).click()
    page.fill(".subjects-auto-complete__input", "88")
    page.get_by_role("checkbox", name="Sports").check()
    file_path = tmp_path / "demoqa_test_file.txt"
    file_path.write_text("Hello, this is a test file for DemoQA upload!")
    page.set_input_files("#uploadPicture", str(file_path))
    page.fill("#currentAddress", "Saint-Petersburg")
    page.locator("#state svg").click()
    page.get_by_role("option", name="NCR").click()
    page.locator("#city svg").click()
    page.get_by_role("option", name="Gurgaon").click()
    page.get_by_role("button", name="Submit").click()

