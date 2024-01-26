from bs4 import BeautifulSoup 

with open('web_with_video.html', 'r') as webv:
    soup = BeautifulSoup(webv, 'lxml')

video = soup.find('div', class_ = 'video-container')

# we put a braces at the end of the statement and accessing the source 
#   inside the iframe like a dictionary. 
video_link = video.find('iframe', class_ = 'youtube-video')['src'] 
print(video_link)

# split the link per slashes. 
vid_id = video_link.split('/')
print(vid_id)

# if we want to get the specific part of the video link 
# just access it like a dictionary just like how we get the main src in 
#   the iframe
vid_id = video_link.split('/')[4]
print(vid_id)

# making a youtube link 
video_yt_link = f'https://www.youtube.com/watch?v={vid_id}'
print(video_yt_link)