import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
import re
class FusionAnalysisPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

        self.wait = WebDriverWait(driver, 20)
        self.token = None

    # Fusion Analysis tab locator
    fusion_tab = (By.XPATH, "//a[normalize-space()='Fusion Analysis']")

    # Loader / overlay (jo click block kar raha hai)
    loader_overlay = (
        By.XPATH,
        "//div[contains(@style,'z-index: 1000')]"
    )
    activity_type_filter = (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-sm-1.3 css-o5aybn']//div[@class='MuiAutocomplete-root MuiAutocomplete-hasClearIcon MuiAutocomplete-hasPopupIcon custom-autocomplete textInput actTheme css-f7t77y']//button[@title='Open']//*[name()='svg']//*[name()='path' and contains(@d,'M7 10l5 5 ')]")
    search = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-colorPrimary scsbtn whitebtn css-110xwq5']//*[name()='svg']")

    overall_data = (By.XPATH, "//li[@id=':r0:-option-0']")
    force_disposition = (By.XPATH, "//li[@id=':r0:-option-1']")
    training = (By.XPATH, "//li[@id=':r0:-option-2']")
    imint = (By.XPATH, "//li[@id=':r0:-option-3']")
    infra = (By.XPATH, "//li[@id=':r0:-option-4']")
    sitrep = (By.XPATH, "//li[@id=':r0:-option-5']")
    sam_deployment = (By.XPATH, "//li[@id=':r0:-option-6']")
    air_aspect = (By.XPATH, "//li[@id=':r0:-option-7']")
    mobile_interception = (By.XPATH, "//li[@id=':r0:-option-8']")
    overall_force_dis = (By.XPATH, "//li[@id=':r0:-option-9']")



    def click_fusion_tab(self):
        self.logger.info("Clicking on fusion tab")

        # wait till loader disappears
        self.wait.until(
            EC.invisibility_of_element_located(self.loader_overlay)
        )

        # wait till tab clickable
        element = self.wait.until(
            EC.element_to_be_clickable(self.fusion_tab)
        )
        assert element.is_displayed(), "Fusion Analysis tab is NOT visible"
        element.click()
        self.logger.info("Clicked fusion tab successfully")


    # 2️ Click Activity Type filter
    def click_activity_type_filter(self):
        self.wait.until(
            EC.element_to_be_clickable(self.activity_type_filter)
        ).click()

    # 3️ Get list of activity types
    def get_activity_types_raw(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul//li")
            )
        )
        return [e.text for e in elements if e.text.strip()]


    TIME_PERIOD_FILTER = (By.XPATH, "//div[3]//div[1]//div[1]//div[1]//div[1]//button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M7 10l5 5 ')]")
    CUSTOM_OPTION = (By.XPATH, "//li[@id=':r3:-option-10']")
    TWO_YEARS = (By.XPATH, "//li[@id=':r3:-option-9']")

    START_DATE = (By.XPATH, "//input[@id=':rh:']")
    END_DATE = (By.XPATH, "//input[@id=':rj:']")

    TIME_PERIOD_OPTIONS = (
        By.XPATH,
        "//ul[@id=':r3:-listbox']"
    )

    def click_time_period_filter(self):
        self.wait.until(
            EC.element_to_be_clickable(self.TIME_PERIOD_FILTER)
        ).click()

    def get_time_period_options(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.TIME_PERIOD_OPTIONS)
        )

        options = []
        for el in elements:
            text = el.text.strip()
            if text:
                options.append(text)

        return options

    def click_custom_option(self):
        self.wait.until(EC.element_to_be_clickable(self.CUSTOM_OPTION)).click()

    def is_start_date_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.START_DATE)
        ).is_displayed()

    def is_end_date_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.END_DATE)
        ).is_displayed()

    LOCATION_FILTER = (By.XPATH, "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root actTheme css-feqhe6']//input[@role='combobox']")
    LOCATION_INPUT = (By.XPATH, "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root actTheme css-feqhe6']//input[@role='combobox']")
    LOCATION_SUGGESTIONS = (By.XPATH, "//ul[@id='-listbox']")
    TABLE_ICON = (By.XPATH, "//button[@title='Table']//*[name()='svg']")
    TABLE_ROWS = (By.XPATH, "//table[@aria-label='customized table']")
    TABLE_LOCATION_CELLS = (By.XPATH, "//th[5]//div[1]")



    input_equipment = (By.XPATH, "/html/body/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/input")
    EQUIPMENT_SUGGESTIONS  = (By.XPATH, "//ul[@id=':rh:-listbox']")
    equipment_filter = (By.XPATH, "/html/body/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/input")

    # ===== ACTIONS =====

    def SELECT_TWO_YEARS(self):
        self.wait.until(EC.element_to_be_clickable(self.TWO_YEARS)
        ).click()

    def open_location_filter(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOCATION_FILTER)
        ).click()

    def type_location(self, value):
        input_box = self.wait.until(
            EC.visibility_of_element_located(self.LOCATION_INPUT)
        )
        input_box.clear()
        input_box.send_keys(value)

    def select_location_from_suggestions(self, search_text):
        global suggestions
        selected = set()

        while True:
            # 1️⃣ focus + type again
            inp = self.wait.until(
                EC.element_to_be_clickable(self.LOCATION_INPUT)
            )
            inp.clear()
            inp.send_keys(search_text)
            short_wait = WebDriverWait(self.driver, 3)

            try:
                suggestions = short_wait.until(
                    EC.presence_of_all_elements_located(self.LOCATION_SUGGESTIONS)
                )
            except:
                break

            clicked = False

            for item in suggestions:
                text = item.text.strip()
                if not text:
                    continue

                if text.lower() in selected:
                    continue

                item.click()
                # print(f" Selected Location: {text}")
                selected.add(text.lower())
                clicked = True
                time.sleep(0.5)
                break  # DOM refresh required

            if not clicked:
                break
        return list(selected)

    def click_on_search(self):
        self.wait.until(EC.element_to_be_clickable(self.search)
        ).click()

    def click_on_table_view(self):
        self.wait.until(
            EC.element_to_be_clickable(self.TABLE_ICON)
        ).click()

    def is_table_data_present(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.TABLE_ROWS)
        )
        return len(rows) > 0

    def get_table_locations(self):
        """
        td[5] ko apne table ke Location column index ke hisaab se set karo
        """
        cells = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//table//tbody//tr//td[5]"))
        )
        return [c.text.strip() for c in cells if c.text.strip()]

    def get_selected_locations(self):
        chips = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,
             "//div[contains(@class,'chip') or contains(@class,'Chip') or contains(@class,'selected')]")
        ))
        return [c.text.strip() for c in chips if c.text.strip()]





    def click_more_filter(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@title='More Filters']//*[name()='svg']")
        )).click()

    def click_equipment_type_filter(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Equipment Type']")
        )).click()

    def open_equipment_filter(self):
        self.wait.until(
            EC.element_to_be_clickable(self.equipment_filter)
        ).click()

    def open_equipment_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-sm-12 css-h719to']//button[@title='Open']//*[name()='svg']")
        )).click()

    def type_equipment(self, value):
        input_box = self.wait.until(
            EC.visibility_of_element_located(self.input_equipment)
        )
        input_box.clear()
        input_box.send_keys(value)

    def select_equipment_by_search(self, search_text="art"):

        global suggestions
        selected = set()

        while True:

            # input focus + type
            inp = self.wait.until(
                EC.element_to_be_clickable(self.input_equipment)
            )
            inp.clear()
            inp.send_keys(search_text)

            short_wait = WebDriverWait(self.driver, 3)

            try:
                suggestions = short_wait.until(
                    EC.presence_of_all_elements_located(
                        self.EQUIPMENT_SUGGESTIONS
                    )
                )
            except:
                print("❌ Suggestion nahi mila")
                break

            clicked = False

            for item in suggestions:

                text = item.text.strip()

                if not text:
                    continue

                if text.lower() in selected:
                    continue

                # scroll safe click
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    item
                )

                time.sleep(0.2)
                item.click()

                # print(f"✅ Selected Equipment: {text}")

                selected.add(text.lower())
                clicked = True
                time.sleep(0.5)
                break   # DOM refresh

            if not clicked:
                break

        return list(selected)






































































































    # ---------------- SELECT ----------------

    def select_all_equipment_types(self):
        options = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//ul[@role='listbox']/li")
        ))

        total = len(options)
        if total == 0:
            raise AssertionError(" Equipment list empty hai")

        print(f"TOTAL EQUIPMENT OPTIONS: {total}")

        selected = []

        # first 50
        first_batch = options[:50]

        # last 50 (avoid overlap if list < 100)
        last_batch = options[-50:] if total > 50 else []

        for opt in first_batch + last_batch:
            text = opt.text.strip()
            if not text:
                continue

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", opt
            )
            time.sleep(0.15)
            self.driver.execute_script("arguments[0].click();", opt)

            selected.append(text)

        print(f"\nSELECTED {len(selected)} EQUIPMENTS (FIRST + LAST):")
        for s in selected:
            print("-", s)

        return selected

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Search']")
        )).click()

    # ---------------- TABLE ----------------
    def get_table_equipment_types(self):
        return [
            cell.text.strip()
            for cell in self.driver.find_elements(
                By.XPATH, "//table[@aria-label='customized table']"
            )
        ]

