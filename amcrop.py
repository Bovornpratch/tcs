import numpy
import datetime
import matplotlib.pyplot as plt


def amcrop(time,am,cut):
    time,am = numpy.array(time),numpy.array(am)
    index = numpy.where(am <= cut)[0]
    time_r,am_r = time[index],am[index]
    return time_r,am_r

def main():
    base = datetime.datetime.now()
    date_list = [base - datetime.timedelta(minutes=x) for x in range(0,300)]
    zenith = numpy.absolute(numpy.linspace(-90,90,300))
    print zenith
    alt = numpy.absolute(zenith - 90.)
    airmass = 1./numpy.cos(numpy.radians(zenith))
    print airmass

    plt.plot(date_list[1:],alt[1:],color='r',label='altitude')
    plt.legend()

    plt.twinx()
    plt.plot(date_list[1:],airmass[1:],color='g',label='airmass')
    plt.ylim(0,50)
    new_date,new_am = amcrop(date_list,airmass,5)
    plt.plot( new_date,new_am ,color='y',label='new airmass')
    plt.axvline(new_date[0])
    plt.axvline(new_date[-1])
    plt.legend()
    plt.show()

    

  
if __name__ ==  "__main__" :
    main()