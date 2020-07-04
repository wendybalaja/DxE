for x in range(1, 37):
    # s = "<div class=\"col-3 col-4-medium col-12-small\"><a class=\"image\"target=\"_blank\" href=\"images/ideaNotes/idea-capture-" + str(
    #     x) + ".jpg\"><img src=\"images/ideaNotes/idea-capture-" + str(
    #         x) + ".jpg\" alt=\" \"></a></div>"

    # s = "<div class=\"col-3 col-4-medium col-12-small\"><a class=\"image\"><img src=\"images/eventPhotos/" + str(x) + ".jpg\" data-target=\"#carouselExample\" data-slide-to=" + str(x-1) +"></a></div>"
    
    r = "<div class=\"carousel-item\"><a class=\"image\"><img src=\"images/eventPhotos/" + str(x) +".jpg\"></a></div>"
    print(r)
