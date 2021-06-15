# NABEGHEHA.COM

# First        : pip install selenium

# Github       : https://github.com/NABEGHEHACOM
# Youtube      : https://youtu.be/XB-f4r7MpqM
# Social Media : https://nabegheha.com/socials


from time import sleep
from selenium import webdriver

# We added this to use a username and password
from info import user, passwd

# Create a Class
class Bot():

    # Create a Constructor
    def __init__(self):
        self.login(user, passwd)

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://instagram.com')
        sleep(2)
        # To select the Username box
        username_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        # Enject Username to That Box
        username_input.send_keys(username)
        sleep(1)
        # To select the Password box
        password_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        # Enject Password to That Box
        password_input.send_keys(password)
        sleep(1)
        # Click on LOGIN BUTTON
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        # After logging in, it goes to this address
        self.driver.get(
            'https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(3)

        # This loop is made to click on the View More button
        number_of_clicks = 0

        # pay attention! This number can vary depending on your needs
        # For example, I needed to click the View More button 5 times. You may need to click the button 10 times

        while number_of_clicks < 5:
            # Click on View More 
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/article/main/button').click()
            sleep(1)
            number_of_clicks += 1
        # This loop will store all usernames in a list
        list_of_usernames = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_usernames.append(names.text)
        # This loop will put all usernames in front of the following URL
        for i in list_of_usernames:
            self.driver.get(f'https://instagram.com/{i}')
            sleep(1)
            # Click on REQUESTED Button
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            sleep(2)
            # Click on UNFOLLOW Button
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[1]').click()    

def main():
    myBot = Bot()


if __name__ == '__main__':
    main()
