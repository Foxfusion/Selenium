from selenium import webdriver
import time


driver = webdriver.Chrome()


list_link = ['https://www.kayak.it/flights/MIL-PAL/2021-09-05/2021-09-06/?sort=bestflight__a&fs=stops=0', 'https://www.kayak.it/flights/MIL-ROM/2021-09-05/2021-09-06/?sort=bestflight__a&fs=stops=0']

for link in list_link:
    #driver = webdriver.Chrome(executable_path="path")
    webdriver.maximize_window()
    webdriver.implicitly_wait(10)
    webdriver.get(link)
    time.sleep(5)
    flights = driver.find_elements_by_class_name("resultInner")
    flights_dict = dict() # To add the dictionaries within a dictionary
    #flight_dict = [] # To add the dictionaries in a list.
    i = 1
print(len(flights))
for flight in flights:
    webdriver.execute_script("arguments[0].scrollIntoView(true);", flight)
    webdriver.execute_script("window.scrollBy(0,-300)")
    flightdetails = {}
    frowdet = []
    details = flight.find_elements_by_xpath(".//div[@class='mainInfo']//li")
    for d in details:
        fd = ""
        sd = ""
        first = d.find_elements_by_xpath(".//div[@class='top']")
        for f in first:
            fd += f.get_attribute("innerText") + ' '
        second = d.find_elements_by_xpath(".//div[@class='bottom']//span")
        for s in second:
            sd += s.get_attribute("innerText")
        detstr = sd + ' - ' + fd
        frowdet.append(detstr)

    fprice = flight.find_element_by_xpath(".//span[@class='price-text']").get_attribute("innerText")[:2]
    flightdetails["Flights"] = frowdet
    flightdetails["Price"] = fprice
    #print(flightdetails)
    flights_dict[i] = flightdetails
    i+=1
    #flight_dict.append(flightdetails) # Append dictionaries to a list.

print(flights_dict)
webdriver.quit()