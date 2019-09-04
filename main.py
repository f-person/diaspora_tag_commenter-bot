import diaspy, os, time

# Initialize
api = diaspy.connection.Connection(pod=os.getenv('POD'), username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'))
api.login()
guid = os.getenv('GUID')
tag = os.getenv('TAG')
comment_text = os.getenv('COMMENT_TEXT')

while True:
    stream = diaspy.streams.Tag(api, tag=tag)

    for post in stream:
        already_commented = False
        comments = post.comments
        
        print(post.id)

        for comment in comments:
            if comment._data['author']['guid'] == guid:
                already_commented = True
                break

        if not already_commented:
            post.comment(comment_text)
    
    # Sleep for 5 minutes
    time.sleep(300)
