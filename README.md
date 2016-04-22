# Newspade
Welcome to this space. For the finished product you can visit http://newspade.com and play around with the search engine

The main purpose of this documentation is to give developers a chance to add their own scrapers an successfully run them in production time.
Please note that due to this I will only cover the code hosted on the mysites app. However i will give a quick recap on the articles application towards the end of this documentation.


Installation.
------------
for installing this application just clone this application with ::

    git clone "https://github.com/cmwaura/Newspade.git"
then cd into the root directory::
    
    cd analyst
    
Requirements needed for the project
-------------------------------------------

you will need the python2.7 interpreter and pip installed in the computer. you will also need the virtualenv or virtualenv wrapper installed in your computer and activated to create your env.
All the requirements have been added on the requirements.txt file in the project. Once you have the project simply::

     pip install -r requirements.txt

and all the requirements will be installed for you. For people using a Linux distro this should be enough for you. However
for people using windows you will need an extra addition of [pywin32.exe](https://sourceforge.net/projects/pywin32/). Install it to your local drive then use easy_install to add it to your environment::
 
    easy_install C:\>path\to\your\pywin32\install

The next few steps from here will be the usual django steps where you prepare the database and create a super user.

    #prepare the db with sqlite3
    python manage.py migrate
    #prepare the superuser.
    python manage.py createsuperuser
    # finally this last step will be for collecting the static files.
    python manage.py collectstatic.
    
One you have done all this just run the server and go to http://127.0.0.1:800/admin and log in and you are good to go for the main steps.

Mysites Application.
--------------------
##### 1) Dynamic_Scraper Settings:

If you got to this point, there are a few things that you have have noticed on the console the Dynamic Scraper application. This is the first portion of actually running the spiders. In order to start the process click on "Scraper object classes" then add an object class.
In this example i will use the "data_obj_bbc" class.

Once you have given the object class a name(data_obj_bbc) then scroll down and you will find a section called scraped obj attrs as show 
below
![alt text](http://i.imgur.com/ksbuK3c.png)

Inorder to understand this step i will refer you to the actual code that represents the next few steps:
open mysites/models.py and you will find this code::

    class NewsWebsite(models.Model):
      	'''
      	in this situation this is the news website that we will be scraping from. So for instance if we are looking for all 
      	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
      	which particular Article. 
      	It borrows from thenm django class models.Model to do the job.
      	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
      	for using scrapy functions to scrape whatever website we desire.
      	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
      	'''

      	title = models.CharField(max_length=250)
      	url = models.URLField()
      	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
    	  scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)



    class BBCNews(models.Model):
      	'''
      	This particular class is concerned with receiving all the scraped material once the job is done. For instance if we are scraping 
      	business analyst positions from a company in mountain view then what we expect is that:
      	title = "Donald Trump wins the Primaries only to be dumped by republicans"
      	url = www.company.com/news.html (or something similar)
      	description = Description|truncated.
      	'''
      
      	news_website = models.ForeignKey(NewsWebsite)
      	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
      	title = models.CharField(max_length=250)
      	url = models.URLField()
      	description = models.TextField(blank=True)
      	date = models.DateTimeField(auto_now=True)
      	company = models.CharField(default="BBC News", max_length=100)

This code is what we are working with more specifically the BBC News. Now back to the admin page, in the Scraped obj attrs, add the following under the name section 
  I) Base:
  The base is essential an nessecary for the spider to run. Think of the base as the core html that the spider will identify inorder to 
  take the elements from that particular core. So for instance, if we are working with scrapy and we have need to get a news website with a html tree of::
      
      <div class= "yellow">
        <ol>
          <li id= "name"> yellow</li>
          <li id="description"> Yellow is a colow</li>
        </ol>
      </div>
    
  the base class will be the
  
        <div class="yellow">
  This is what the spider will be looking for.The order type of this name is 10 and the Attr type will be BASE.
  
  II) title:
  this is from the BBCNews models and in actual fact the rest will all be from the BBCNews models.
  Order = 20
  Attr type = STANDARD
  
  III) url:
  Order = 30
  Attr type = STANDARD OR DETAIL_PAGE_URL
 
 one thing to consider is that you want the id field of the url to be true. This is because it will be used to determine the uniqueness of each individual post. It comes from the logic that no two posts have the same link and if we have an entry like that, then one is a repeat of the other and the spider will delete the former.
  
  IV) Description:
  Order = 40
  Attr type = STANDARD

One last thing to note is that company is a default value so we do not need to add it as an object class. The BBC company will be automatically added. Similar to that, the date is the date the scraper will be run and that too is automatic.

Save that bad boy and we are onto the next challenge.

##### 2)Scrapers
Time to add the scrapers. Well in this Scenario we will be scraping the Rss feeds since its way more easier than the actual page. Click on the scraper and add a scraper with the name of BBC scraper. The Scraped obj class will be what we created earlier "data_obj_bbc"
The status of this scraper is Manual. Once we activate Celery we will turn it to Active though.

Click on the Request pages types and add a page. Then open the page up by clicking the "(show)" link.
You will be presented with the following options that you will change. 
1) Page type: click the drop down and add Main Page.
2) Content type: Change that to 'XML'

And you are done with the request pages portion.

Scroll down until you hit the scraper elems. At this point you need to add the previous options we set in out class. Add
* Base 
* title
* url
* description

Since we are using xml this next part will be relatively simple::

        <item>
            <title> this is just a title </title>
            <link> http://newspade/ </link>
            <description> yea that was a sick burn. Call the paramedics coz someone just got burned! Savage</description>
        </item>

This is an example of the XML structure. So for the Xpath we will have:
Name            X path
* base          //item
* title         .//title/text()
* url           .//link/text()
* description   .//description/text()

X-Path rules apply.

Save your changes and you are almost on the end.

Finally go back to the main page and now go to the mysites app. This will be tilted mysites.

Mysites.
--------

Now with all that i have been doing i havent had the time to rename the "News Websites" to "BBC Website" but by definition based on the code that i had displayed above, the NewsWebsite  Model and the BBCNews Model share a foreign key relationship. So for instance if you look at the AljazeeraWebsites Model and the AljazeeraNews model, you will realize that they have a foreign key relation. 

So  now that we have identified these relationships lets work on the actual links. So pick a link that holds the rss feeds from BBC and copy it. Click on NewsWebsites and create a news website.

Give it the title you want: i.e, BBC RSS
for the url it will be the link that you have copies or the rss page link.
choose the scraper we created 'Scraper bbc'
and under scraper runtime add click the (+) button.  Add the scraper runtime of 1 and click the save button.

Run the Spiders.
----------------

In the command line type::
    
        scrapy crawl news_spider -a id=1 -a do_action=yes
and then open the BBC News page. Voila all the news should be there.

This was a quick run down of how to run the scrapy spider and get the foundation of actually testing the project.

Multiprocessing.
---------------
If you do decide to run a live version of the project on a server, please note that there are about 4 active spiders from BBC, Politico, Aljazeera, Reuters. In the next update i will add 5 more spiders from different news channels. Also feel free to make your own spiders and take them for a spin.

However, when it actually comes to scheduling the spiders, you may face some difficulty since running scrapyd on a server like heroku might not be supported[last time i checked]. so here is a small hack that could help you overcome this process.

        import multiprocessing
        import time
        import os
        
        def processors():
            # Call the spiders to run
            os.system('scrapy crawl news_spider -a id=1 -a do_action=yes')
            time.sleep(60)
            # add other spiders
            # Build the Whoosh index
            os.system("python manage.py rebuild_index")
            
        def main():
            p = multiprocessing.Process(target=processors)
            p.start()
        main()
This will create processes for your spiders to run. Its very simply implemented so if you find something more awesome to use other than this go for it. 
        
Developer Role.
---------------

So you want to contribute to making the spiders and getting more news to the news search website.
Inorder to do this we will add new code to the following files.
* models.py
* admin.py
* views.py
* Spiders.py

1) Models.py
------------
Lets talk about the models required.
Before we begin please note that this project uses [dynamic_scraper](https://django-dynamic-scraper.readthedocs.org/en/latest/) and if you feel that i havent explained something to the fullest, check out the authors doc.

The structure of the models will be:
1) Website where we are scraping the information from. It will inherit from models.Models(Django) and will have the title and url
of the website.
2) The news models where all the scraped information will be stored at. It will also inherit from Django models.
3) the item class. This is the django item class that is described on the scrapy framework for storing your results in the ORM

Example:
        from django.db import models
        from django.db.models.signals import pre_delete
        from scrapy_djangoitem import DjangoItem
        from dynamic_scraper.models import Scraper, SchedulerRuntime
        from django.dispatch import receiver
        
        # here we are implementing the website where we will actually scrape the info from.
        class BBCWebsite(models.Model):
        
            title = models.CharField(max_length=250)
        	url = models.URLField()
        	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
        	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL
        
        # here we are implementing the models where all the information will be stored after we have finished scraping 
        
        class BBCNews(models.Model):
        	news_website = models.ForeignKey(NewsWebsite)
        	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
        	title = models.CharField(max_length=250)
        	url = models.URLField()
        	description = models.TextField(blank=True)
        	date = models.DateTimeField(auto_now=True)
        	company = models.CharField(default="BBC News", max_length=100)
        	
        	def __str__(self):
        		return self.title
        	
        	class Meta:
        		ordering = ['-id']
        		verbose_name_plural = "BBCNews"
        		
        # finally the django item.
        class NewsAdItem(DjangoItem):
        	'''
        	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
        	django database.
        	'''
            django_model = BBCNews

After all is said and done then just run
        ./ manage.py makemigrations mysites
        ./ manage.py migrate 
and it should update with each new model you add.

2) admin.py:
-----------
Admin is what shows up on the admin page of the django models. Now you have alot of freedom on how to implement this however just follow the naming conventions.

for instance::
        admin.site.register(ReutersWebsite, ReutersWebsiteAdmin)
        admin.site.register(ReutersNews, ReutersAdAdmin)
the Ad admin goes with the news.  When implementing the admin, i followed the instructions laid out by the documentation on [dynamic_scraper](https://django-dynamic-scraper.readthedocs.org/en/latest/). However feel free to make changes to your additions as long as it is readable.

3) views.py
-----------
This version of the views is a little bit inefficient and will be improved upon. There are a couple things we need to work on in the views
    1) filters- the filters will be where users can decide to filter all the new information by company OR by date
    2) featured face- this will eventually be then homepage of the application. It will contain the latest news based on either the trends or the admin. so in mind i was thinking of using itertools.chain to create a list of all entries and then filter by greater than or equal todays date::
            #something like this
            def featured(request):
                from itertools import chain
                try:
                    qs1 = BBCNews.objects.filter(date__gte=datetime.date.today)
                    qs2 = ReutersNews.objects.filter(date__gte=datetime.date.today)
                    queryset = list(chain(qs1, qs2)
                    context = {"featured_news":queryset}
                    template_name = "news/featured.html"
                    return render(request, template_name, context)
                except:
                    raise Http404
Most of the views implemented are the basic generic class views but we can go a tad further.

4) Spiders
-----------
Lets talk about the meat of the app:

        class NewsSpider(DjangoSpider):
        
        	name = 'news_spider'
        
        	def __init__(self, *args, **kwargs):
        		self._set_ref_object(BBCWebsite, **kwargs)
        		self.scraper = self.ref_object.scraper
        		self.scrape_url = self.ref_object.url
        		self.scheduler_runtime = self.ref_object.scraper_runtime
        		self.scraped_obj_class = BBCNews
        		self.scraped_obj_item_class = NewsAdItem
        		super(NewsSpider, self).__init__(self, *args, **kwargs)
The above class inherits from DjangoSpider  which is actually found on dynamic_scraper.django_spider
The reference object that you set is the Website were we will scrape all the information from. In our case we used BBCWebsite as the class therefore we will import the model a set it up as shown in::
        
        self._set_ref_object(BBCWebsite, **kwargs)
The scraper is set from the reference scraper in that particular class as as well as the scrape_url  which is from the class itself. Everything else is setting where the scraper will spit out the scraped info as well as the Django item for each specific model. Then declare the super since we are working with the DjangoSpider.

The name is the name we will give the spider when we call it using
        
        scrapy crawl news_spider ....
All this lives in the spiders.py file


        
