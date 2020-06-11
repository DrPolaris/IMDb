import imdb
import io
ia = imdb.IMDb()
#movie = ia.get_movie('0094226')
#print(movie)
#print(movie.get('rating'))
#print(movie)}
Mfile = open("/home/arjun/Documents/PyScripts/MovList5.txt", 'r')
#print(Mfile.read())
Mov = Mfile.read().split('\n')
with io.open("/home/arjun/Documents/PyScripts/RatList5.txt","a",encoding = 'utf8') as fileID:
    for i in range(len(Mov)):
        print(Mov[i])
        GetM = ia.search_movie(Mov[i])
        #if(bool(GetM)==False):
            #print('Search Failed')
            #i = i+1
            #GetM = ia.search_movie(Mov[i])
        mv = GetM[0]
        ID = ia.get_imdbID(mv)
        print(ID)
        movie = ia.get_movie(ID)
        rating = movie.get('rating')
        year = movie.get('year')
        lang = movie.get('languages')
        plot = movie.get('plot')[0]
        print(type(plot))
        #plot = plot.encode('utf-8')
        print(type(plot))
        print((type(Mov[i]),type(year),type(plot)))
        fileID.write("%s \t %s \t %s \t %s \t %s \n" % (Mov[i],year,lang[0],rating,plot))
fileID.close()
