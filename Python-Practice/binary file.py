with open('wallpaper1.jpg','rb') as f:
    with open('wallpaper1_copy.jpg','wb') as wf:
        wf.write(f.read())

