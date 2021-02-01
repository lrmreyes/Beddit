import json
from django.core.management.base import BaseCommand
from beddit.models import Post, Comment

class Command(BaseCommand):
    help = 'Imports data from input file'
    
    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        print(options['filename'])
        with open(options['filename'], encoding="utf8") as data_file:
            data = json.load(data_file)
            posts = data['posts']
            for post in posts:
                date=post['published'][6:] + "-" + post['published'][0:2] + "-" + post['published'][3:5]
                newpost = Post(id=post['id'], title=post['title'], content=post['content'],
                author=post['author'], upvotes=post['upvotes'], downvotes=post['downvotes'],
                published=date)
                newpost.save()
                if post['comments']:
                    for comment in post['comments']:
                        newcomment = Comment(content=comment['content'], author=comment['author'],
                        upvotes=comment['upvotes'], downvotes=comment['downvotes'], post_id=post['id'])
                        newcomment.save()
        self.stdout.write(self.style.SUCCESS('File data successfully imported!'))