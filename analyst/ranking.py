import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analyst.settings")

from articles.models import Articles

def ranker():
	for article in Articles.with_votes.all():
		article.set_rank()

def shower():
	print "\n".join("%10s %0.2f" % (article.title, article.rank_score,
                         ) for article in Articles.with_votes.all())

if __name__ =="__main__":
	while 1:
		print "---"
		ranker()
		shower()
		time.sleep(4)