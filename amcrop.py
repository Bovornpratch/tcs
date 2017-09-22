import numpy
import datetime
import matplotlib.pyplot as plt


def amcrop(time,am,cut):

    ''' 
    crop observation time.
    time = array/list of datetime objects
    am = array/list of airmass
    cut = total observation time
    '''
    time,am = numpy.array(time),numpy.array(am) 
    filt_z = numpy.where(am >= 1.)
    time,am = time[filt_z],am[filt_z]

    cen_in = numpy.where(numpy.amin(am) == am)
    basin_t,basin_am = time[cen_in][0],am[cen_in][0]
    lim = datetime.timedelta(minutes=cut/2.)

    index = numpy.where(numpy.absolute(time-basin_t) < lim)

    return time[index],am[index]


def main():
    base = datetime.datetime(2017,01,01,00,00,00)
    date_list = [base + datetime.timedelta(minutes=x) for x in range(0,600)]
    zenith = numpy.absolute(numpy.linspace(-90,90,600))

    extend = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alt_ext =[-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10] 
    date_list_ext = [date_list[len(date_list)-1] + datetime.timedelta(minutes=x) for x in range(0,len(extend))]
    
    alt = numpy.absolute(zenith - 90.)
    airmass = 1./numpy.cos(numpy.radians(zenith))

    date_list = numpy.append(date_list,date_list_ext)
    alt = numpy.append(alt,alt_ext)
    airmass = numpy.append(airmass,extend)

    plt.plot(date_list[1:],alt[1:],color='r',label='altitude')
    plt.legend()

    plt.twinx()
    plt.plot(date_list[1:],airmass[1:],color='g',label='airmass')
    plt.ylim(0,50)
    new_date,new_am = amcrop(date_list,airmass,240.)
    plt.plot( new_date,new_am ,color='y',label='new airmass')
    plt.axvline(new_date[0])
    plt.axvline(new_date[-1])
    plt.legend()
    plt.show()

    

  
if __name__ ==  "__main__" :
    main()