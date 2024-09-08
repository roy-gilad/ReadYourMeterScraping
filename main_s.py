import emailsender
import main_scraping as scraping
import test
import time

start_time= time.time();
list=scraping.aradReadYourMeter_scraping()
#list=test.testt()

# one=list[0]
# two=list[1]
# msg="argumen first is {} and sc is {}".format(one,two)
# print(date,)

# emailsender.send_email(list[0],list[1])

print("--%s secound run time"% (time.time() - start_time))



